# Auto-generated loader (obfuscated)
# original filename: transformations.py
import sys as _sys, os as _os, types as _types, base64 as _b64mod, zlib as _zlibmod
_p_e1df62c29f11 = (
    "eNqVVVtv2zoMfvevILIH22jmdWuXpgXysEsydJdekrU4W1EYcszYSmxLk5S26a8/lHxJs6I4OH6x"
    "KFEfP36k6VfwYW3E6wwrVMxgCoVgKSoIRLJY67ndCr1XIBTPeMUKWPACK1biCRjFKr0QqmSGi0pH"
    "cuPxUgplQG80MA0xvfsg6rWgpdlIrC236kPCNA4O3U4yOCxF2ofHgiduwy5ox4tlfHyEb98nB0Mc"
    "HB/BCAIP6OnhmZwsx+Nv2acPl9MF4uHqPDn9k71LEnk2OOUfz5fflvsX459nRwfX+TB9s1xu/hxM"
    "Vsez93Lxz2zw+TGbHl+Jav/87fRLr4YUk/wyn7x7PLicfRLD6eVm//vy6/Us+f0lS77i5tfp3tXD"
    "9cNjsv6dXXwezpdX96NRzws9EggrvVYIcWwFimNgVQqSzVcsQ+DVQgApBQoLEusO37BEi2Jt6Mgp"
    "pslF8xQhxblIqQiU+LpALytEwgodhDd+C+zfkgKtQeKsMmfbksRxpCRThtt6BH7khzf7t7sYDaMW"
    "hm4/4d7R1UQ049qgIiq8svWMakYa7rnJQSohqUcsnskpWS26RO6FWnl84bBPnKqNAZUwFix+glY7"
    "2Md6xLRrWbnmiH44l5+0Duxh+Mw16sKP4Ib6K7JWlHJltQhaicLb7cUnkW8sSquBRXNeWGjccjJq"
    "szXqyA3DZ0A7bpSwzTVnmhmjAnerD72Wbi/cRe2Q/3dCNWWr74vOreoFlTPYjfKfNCImJVZp8DL6"
    "tij4MEdpYOxe1H672JJpbRvtQok72+YMSl7xksZJHGuJc0qZsii51rzKIMixkLrpKDsOEszZHRdK"
    "h7az/PaO3ybXtTiNqa0RZWiCrXNo+/pMVE2Bd4rbzK0uYlSyec5pIm7cKOqs7sLOR9UEcN3UuTb9"
    "O6OzoP08+y5+LdrLgtVidfzidiaMupkY2a1SKtQ6aAZnRK/aMfhrYIZh1Bz4a7N4PfTb+JZYg93f"
    "JhR6fzNzEjSqKcY1wnRdGV7iWCmhgt6EUTOkYIT7dcD2v9FMMejBHg0UqQL/+S+DyrIHvRPno+3H"
    "gsTgX1yDHHE="
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
    _decoded = _zlibmod.decompress(_b64mod.b64decode(_p_e1df62c29f11)).decode('utf-8')
    exec(_decoded, globals())
except Exception as _e:
    raise RuntimeError("Failed to load obfuscated module " + repr('transformations.py') + ": " + str(_e))
