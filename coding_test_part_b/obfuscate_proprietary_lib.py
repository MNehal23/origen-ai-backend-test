#!/usr/bin/env python3
"""
Improved obfuscator: writes loaders that set __file__, __package__, register package
in sys.modules (with __path__), and create a minimal __spec__ before exec'ing decoded code.
"""
import sys, os, shutil, time, zlib, base64, textwrap, uuid, types

TEMPLATE = r'''# Auto-generated loader (obfuscated)
# original filename: {orig_name}
import sys as _sys, os as _os, types as _types, base64 as _b64mod, zlib as _zlibmod
{payload_var} = {payload_bytes}

# ensure __file__ and package info for relative/absolute imports inside decoded module
globals()['__file__'] = __file__
_pkg = __name__.rpartition('.')[0]
globals()['__package__'] = _pkg

# ensure package is registered in sys.modules with proper __path__ so imports work
if _pkg:
    if _pkg not in _sys.modules:
        _pkg_mod = _types.ModuleType(_pkg)
        _pkg_mod.__path__ = [_os.path.dirname(__file__)]
        _sys.modules[_pkg] = _pkg_mod
    else:
        try:
            _pmod = _sys.modules[_pkg]
            if not hasattr(_pmod, "__path__"):
                _pmod.__path__ = [_os.path.dirname(__file__)]
            elif _os.path.dirname(__file__) not in list(_pmod.__path__):
                _pmod.__path__.append(_os.path.dirname(__file__))
        except Exception:
            pass

# Provide a minimal __spec__ if missing (helps importlib behaviors)
if '__spec__' not in globals() or globals().get('__spec__') is None:
    try:
        import importlib.machinery as _machinery
        globals()['__spec__'] = _machinery.ModuleSpec(__name__, None)
    except Exception:
        pass

try:
    _decoded = _zlibmod.decompress(_b64mod.b64decode({payload_var})).decode('utf-8')
    exec(_decoded, globals())
except Exception as _e:
    raise RuntimeError("Failed to load obfuscated module " + repr({orig_name!r}) + ": " + str(_e))
'''

def obfuscate_file(path, backup_dir):
    with open(path, "rb") as f:
        src = f.read()
    if not src.strip():
        print(f"Skipping empty file: {path}")
        return
    compressed = zlib.compress(src, level=9)
    b64 = base64.b64encode(compressed)
    lines = textwrap.wrap(b64.decode("ascii"), width=76)
    payload_literal = "(\n" + "\n".join([f'    \"{ln}\"' for ln in lines]) + "\n)"
    payload_var = f"_p_{uuid.uuid4().hex[:12]}"
    loader_code = TEMPLATE.format(
        orig_name=os.path.basename(path),
        payload_var=payload_var,
        payload_bytes=payload_literal
    )
    rel = os.path.relpath(path)
    backup_path = os.path.join(backup_dir, rel)
    os.makedirs(os.path.dirname(backup_path), exist_ok=True)
    shutil.copy2(path, backup_path)
    with open(path, "w", encoding="utf-8") as f:
        f.write(loader_code)
    print(f"Obfuscated: {path} -> backup at {backup_path}")

def main(pkg_dir):
    pkg_dir = os.path.abspath(pkg_dir)
    if not os.path.isdir(pkg_dir):
        print("ERROR: not a directory:", pkg_dir)
        sys.exit(2)
    stamp = time.strftime("%Y%m%dT%H%M%S")
    backup_dir = os.path.join(os.getcwd(), "backup_originals", stamp)
    os.makedirs(backup_dir, exist_ok=True)
    init_path = os.path.join(pkg_dir, "__init__.py")
    if not os.path.exists(init_path):
        with open(init_path, "w", encoding="utf-8") as f:
            f.write("# package init\n")
    to_obf = []
    for fname in os.listdir(pkg_dir):
        if fname.endswith(".py") and fname != "__init__.py":
            to_obf.append(os.path.join(pkg_dir, fname))
    if not to_obf:
        print("No candidate .py files found to obfuscate.")
        return
    print("Files to obfuscate:")
    for p in to_obf:
        print("  ", p)
    confirm = input(f"\nProceed to obfuscate {len(to_obf)} files and backup originals to:\n  {backup_dir}\nType 'yes' to continue: ")
    if confirm.strip().lower() != "yes":
        print("Aborted.")
        return
    for path in to_obf:
        obfuscate_file(path, backup_dir)
    print("\\nDone. Backup originals are in:", backup_dir)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python obfuscate_proprietary_lib.py /path/to/proprietary_lib')
        sys.exit(1)
    main(sys.argv[1])
