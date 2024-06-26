import ctypes

class VkDebugReportCallbackCreateInfoEXT(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkInstanceCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCreateDebugReportCallbackEXT',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'pfnCallback': 'pfn_callback',
        'pUserData': 'user_data',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_debug_report',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkDebugReportFlagsEXT',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DEBUG_REPORT_CALLBACK_CREATE_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEBUG_REPORT_CALLBACK_CREATE_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)


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
