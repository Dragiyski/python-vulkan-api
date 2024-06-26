import ctypes

class VkPipelineRasterizationProvokingVertexStateCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('provokingVertexMode', ctypes.c_int),
    ]

    _init_ = []
    _extends_ = {
        'VkPipelineRasterizationStateCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'provokingVertexMode': 'provoking_vertex_mode',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_provoking_vertex',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'provokingVertexMode': 'VkProvokingVertexModeEXT',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_PROVOKING_VERTEX_STATE_CREATE_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_PROVOKING_VERTEX_STATE_CREATE_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPipelineRasterizationProvokingVertexStateCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'provokingVertexMode': ctypes.c_int,
}
