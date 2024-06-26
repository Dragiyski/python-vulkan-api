import ctypes

class VkPushDescriptorSetWithTemplateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('descriptorUpdateTemplate', ctypes.c_void_p),
        ('layout', ctypes.c_void_p),
        ('set', ctypes.c_uint32),
        ('pData', ctypes.c_void_p),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkPipelineLayoutCreateInfo',
    }
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCmdPushDescriptorSetWithTemplate2KHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'descriptorUpdateTemplate': 'descriptor_update_template',
        'layout': 'layout',
        'set': 'set',
        'pData': 'data',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_maintenance6',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PUSH_DESCRIPTOR_SET_WITH_TEMPLATE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PUSH_DESCRIPTOR_SET_WITH_TEMPLATE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkPushDescriptorSetWithTemplateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'descriptorUpdateTemplate': ctypes.c_void_p,
    'layout': ctypes.c_void_p,
    'set': ctypes.c_uint32,
    'pData': ctypes.c_void_p,
}
