import ctypes

class VkDebugUtilsObjectNameInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('objectType', ctypes.c_int),
        ('objectHandle', ctypes.c_uint64),
        ('pObjectName', ctypes.c_char_p),
    ]

    _init_ = []
    _extends_ = {
        'VkPipelineShaderStageCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkDebugUtilsMessengerCallbackDataEXT',
    }
    _input_of_ = {
        'vkSetDebugUtilsObjectNameEXT',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'objectType': 'object_type',
        'objectHandle': 'object_handle',
        'pObjectName': 'object_name',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_debug_utils',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'objectType': 'VkObjectType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DEBUG_UTILS_OBJECT_NAME_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEBUG_UTILS_OBJECT_NAME_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkDebugUtilsObjectNameInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'objectType': ctypes.c_int,
    'objectHandle': ctypes.c_uint64,
    'pObjectName': ctypes.c_char_p,
}
