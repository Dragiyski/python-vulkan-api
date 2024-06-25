import ctypes

class VkDebugUtilsMessengerCreateInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'messageSeverity': ctypes.c_uint32,
            'messageType': ctypes.c_uint32,
            'pfnUserCallback': vkDebugUtilsMessengerCallbackEXT,
            'pUserData': ctypes.c_void_p,
        }


from .._vulkan_callback.vkDebugUtilsMessengerCallbackEXT import vkDebugUtilsMessengerCallbackEXT

VkDebugUtilsMessengerCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('messageSeverity', ctypes.c_uint32),
    ('messageType', ctypes.c_uint32),
    ('pfnUserCallback', vkDebugUtilsMessengerCallbackEXT),
    ('pUserData', ctypes.c_void_p),
]
