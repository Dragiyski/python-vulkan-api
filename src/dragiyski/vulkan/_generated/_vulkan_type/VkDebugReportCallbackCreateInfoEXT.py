import ctypes

class VkDebugReportCallbackCreateInfoEXT(ctypes.Structure):
    pass

from .._vulkan_callback.vkDebugReportCallbackEXT import vkDebugReportCallbackEXT

VkDebugReportCallbackCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pfnCallback', vkDebugReportCallbackEXT),
    ('pUserData', ctypes.c_void_p),
]

VkDebugReportCallbackCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'pfnCallback': vkDebugReportCallbackEXT,
    'pUserData': ctypes.c_void_p,
}
