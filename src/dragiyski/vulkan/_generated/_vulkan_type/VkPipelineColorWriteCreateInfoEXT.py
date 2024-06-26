import ctypes

class VkPipelineColorWriteCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('attachmentCount', ctypes.c_uint32),
        ('pColorWriteEnables', ctypes.POINTER(ctypes.c_uint32)),
    ]

    _init_ = []
    _extends_ = {
        'VkPipelineColorBlendStateCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'attachmentCount': 'attachment_count',
        'pColorWriteEnables': 'color_write_enables',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_color_write_enable',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_COLOR_WRITE_CREATE_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_COLOR_WRITE_CREATE_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPipelineColorWriteCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'attachmentCount': ctypes.c_uint32,
    'pColorWriteEnables': ctypes.POINTER(ctypes.c_uint32),
}
