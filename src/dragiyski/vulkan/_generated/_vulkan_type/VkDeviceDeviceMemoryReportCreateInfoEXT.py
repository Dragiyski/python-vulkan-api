import ctypes

class CType(ctypes.Structure):
    pass

from ..vulkan_callback import vkDeviceMemoryReportCallbackEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pfnUserCallback', ctypes.POINTER(vkDeviceMemoryReportCallbackEXT)),
    ('pUserData', ctypes.c_void_p),
]
