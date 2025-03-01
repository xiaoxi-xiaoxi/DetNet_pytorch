
# from torch.utils.ffi import _wrap_function
from ....ffiext import _wrap_function
# from .._roi_crop import lib as _lib, ffi as _ffi

import lib as _lib
import cffi as _ffi

__all__ = []
def _import_symbols(locals):
    for symbol in dir(_lib):
        fn = getattr(_lib, symbol)
        locals[symbol] = _wrap_function(fn, _ffi)
        __all__.append(symbol)

_import_symbols(locals())
