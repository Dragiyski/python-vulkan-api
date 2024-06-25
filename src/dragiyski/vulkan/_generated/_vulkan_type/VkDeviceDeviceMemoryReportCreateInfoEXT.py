import ctypes

class VkDeviceDeviceMemoryReportCreateInfoEXT(ctypes.Structure):
    pass

from .._vulkan_callback.vkDeviceMemoryReportCallbackEXT import vkDeviceMemoryReportCallbackEXT

VkDeviceDeviceMemoryReportCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pfnUserCallback', vkDeviceMemoryReportCallbackEXT),
    ('pUserData', ctypes.c_void_p),
]

VkDeviceDeviceMemoryReportCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'pfnUserCallback': vkDeviceMemoryReportCallbackEXT,
    'pUserData': ctypes.c_void_p,
}
