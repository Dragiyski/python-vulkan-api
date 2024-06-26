import ctypes

class VkSamplerYcbcrConversionCreateInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkExternalFormatANDROID',
        'VkExternalFormatQNX',
        'VkSamplerYcbcrConversionYcbcrDegammaCreateInfoQCOM',
    }
    _includes_ = {
        'VkComponentMapping',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCreateSamplerYcbcrConversion',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'format': 'format',
        'ycbcrModel': 'ycbcr_model',
        'ycbcrRange': 'ycbcr_range',
        'components': 'components',
        'xChromaOffset': 'x_chroma_offset',
        'yChromaOffset': 'y_chroma_offset',
        'chromaFilter': 'chroma_filter',
        'forceExplicitReconstruction': 'force_explicit_reconstruction',
    }
    _vk_versions_ = {
        (1, 1),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'format': 'VkFormat',
        'ycbcrModel': 'VkSamplerYcbcrModelConversion',
        'ycbcrRange': 'VkSamplerYcbcrRange',
        'xChromaOffset': 'VkChromaLocation',
        'yChromaOffset': 'VkChromaLocation',
        'chromaFilter': 'VkFilter',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkComponentMapping import VkComponentMapping

VkSamplerYcbcrConversionCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('format', ctypes.c_int),
    ('ycbcrModel', ctypes.c_int),
    ('ycbcrRange', ctypes.c_int),
    ('components', VkComponentMapping),
    ('xChromaOffset', ctypes.c_int),
    ('yChromaOffset', ctypes.c_int),
    ('chromaFilter', ctypes.c_int),
    ('forceExplicitReconstruction', ctypes.c_uint32),
]

VkSamplerYcbcrConversionCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'format': ctypes.c_int,
    'ycbcrModel': ctypes.c_int,
    'ycbcrRange': ctypes.c_int,
    'components': VkComponentMapping,
    'xChromaOffset': ctypes.c_int,
    'yChromaOffset': ctypes.c_int,
    'chromaFilter': ctypes.c_int,
    'forceExplicitReconstruction': ctypes.c_uint32,
}
