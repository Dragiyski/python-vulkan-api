import ctypes

class VkPipelinePropertiesIdentifierEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pipelineIdentifier', ctypes.ARRAY(ctypes.c_uint8, 16)),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'pipelineIdentifier': 'pipeline_identifier',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_pipeline_properties',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_PROPERTIES_IDENTIFIER_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_PROPERTIES_IDENTIFIER_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPipelinePropertiesIdentifierEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pipelineIdentifier': ctypes.ARRAY(ctypes.c_uint8, 16),
}
