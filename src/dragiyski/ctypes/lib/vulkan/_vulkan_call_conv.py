import ctypes

if hasattr(ctypes, 'WINFUNCTYPE'):
    VKAPI_CALL = ctypes.WINFUNCTYPE
    VKAPI_PTR = ctypes.WINFUNCTYPE
else:
    VKAPI_CALL = ctypes.CFUNCTYPE
    VKAPI_PTR = ctypes.CFUNCTYPE
