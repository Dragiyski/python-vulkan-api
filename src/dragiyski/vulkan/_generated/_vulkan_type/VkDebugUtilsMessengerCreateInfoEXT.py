import ctypes

class CType(ctypes.Structure):
    pass

from ..vulkan_callback import vkDebugUtilsMessengerCallbackEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('messageSeverity', ctypes.c_uint32),
    ('messageType', ctypes.c_uint32),
    ('pfnUserCallback', vkDebugUtilsMessengerCallbackEXT),
    ('pUserData', ctypes.c_void_p),
]
