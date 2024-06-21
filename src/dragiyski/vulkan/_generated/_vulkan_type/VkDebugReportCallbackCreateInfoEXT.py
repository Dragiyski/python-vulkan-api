import ctypes

class CType(ctypes.Structure):
    pass

from ..vulkan_callback import vkDebugReportCallbackEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pfnCallback', ctypes.POINTER(vkDebugReportCallbackEXT)),
    ('pUserData', ctypes.c_void_p),
]
