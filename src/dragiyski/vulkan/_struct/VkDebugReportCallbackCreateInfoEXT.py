import ctypes, sys

class VkDebugReportCallbackCreateInfoEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkDebugReportCallbackCreateInfoEXT

from .._vulkan_callback import vkDebugReportCallbackEXT

VkDebugReportCallbackCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pfnCallback', ctypes.POINTER(vkDebugReportCallbackEXT)),
    ('pUserData', ctypes.c_void_p),
]
