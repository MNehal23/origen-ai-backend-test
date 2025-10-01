# Auto-generated loader (obfuscated)
# original filename: data_loader.py
import sys as _sys, os as _os, types as _types, base64 as _b64mod, zlib as _zlibmod
_p_3bc5b7e330c4 = (
    "eNpLSU1TyMlPTIlPSSxJ1NC04lIAAmWF3My8zNzEHIWU1Nx8BZAUWLwotaS0KE8h2lDPQEfBCEQY"
    "gwgTPYNYLgAj6xPZ"
)

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
    _decoded = _zlibmod.decompress(_b64mod.b64decode(_p_3bc5b7e330c4)).decode('utf-8')
    exec(_decoded, globals())
except Exception as _e:
    raise RuntimeError("Failed to load obfuscated module " + repr('data_loader.py') + ": " + str(_e))
