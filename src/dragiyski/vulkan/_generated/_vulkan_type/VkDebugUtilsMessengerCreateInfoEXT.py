import ctypes

class VkDebugUtilsMessengerCreateInfoEXT(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkInstanceCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCreateDebugUtilsMessengerEXT',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'messageSeverity': 'message_severity',
        'messageType': 'message_type',
        'pfnUserCallback': 'pfn_user_callback',
        'pUserData': 'user_data',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_debug_utils',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkDebugUtilsMessengerCreateFlagsEXT',
        'messageSeverity': 'VkDebugUtilsMessageSeverityFlagsEXT',
        'messageType': 'VkDebugUtilsMessageTypeFlagsEXT',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DEBUG_UTILS_MESSENGER_CREATE_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEBUG_UTILS_MESSENGER_CREATE_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)


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

VkDebugUtilsMessengerCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'messageSeverity': ctypes.c_uint32,
    'messageType': ctypes.c_uint32,
    'pfnUserCallback': vkDebugUtilsMessengerCallbackEXT,
    'pUserData': ctypes.c_void_p,
}
