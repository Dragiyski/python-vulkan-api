import ctypes, sys

class VkDeviceDeviceMemoryReportCreateInfoEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkDeviceDeviceMemoryReportCreateInfoEXT

from ..vulkan_callback import vkDeviceMemoryReportCallbackEXT

VkDeviceDeviceMemoryReportCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pfnUserCallback', ctypes.POINTER(vkDeviceMemoryReportCallbackEXT)),
    ('pUserData', ctypes.c_void_p),
]
