import ctypes

class VkDebugUtilsLabelEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pLabelName', ctypes.c_char_p),
        ('color', ctypes.ARRAY(ctypes.c_float, 4)),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkDebugUtilsMessengerCallbackDataEXT',
    }
    _input_of_ = {
        'vkCmdBeginDebugUtilsLabelEXT',
        'vkCmdInsertDebugUtilsLabelEXT',
        'vkQueueBeginDebugUtilsLabelEXT',
        'vkQueueInsertDebugUtilsLabelEXT',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'pLabelName': 'label_name',
        'color': 'color',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_debug_utils',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DEBUG_UTILS_LABEL_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEBUG_UTILS_LABEL_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkDebugUtilsLabelEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pLabelName': ctypes.c_char_p,
    'color': ctypes.ARRAY(ctypes.c_float, 4),
}
