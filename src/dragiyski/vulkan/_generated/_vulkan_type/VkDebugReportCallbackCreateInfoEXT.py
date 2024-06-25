import ctypes

class VkDebugReportCallbackCreateInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'pfnCallback': vkDebugReportCallbackEXT,
            'pUserData': ctypes.c_void_p,
        }


from .._vulkan_callback.vkDebugReportCallbackEXT import vkDebugReportCallbackEXT

VkDebugReportCallbackCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pfnCallback', vkDebugReportCallbackEXT),
    ('pUserData', ctypes.c_void_p),
]
