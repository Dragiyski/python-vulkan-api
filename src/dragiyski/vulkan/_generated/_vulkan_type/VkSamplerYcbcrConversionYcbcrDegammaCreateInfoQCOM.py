import ctypes

class VkSamplerYcbcrConversionYcbcrDegammaCreateInfoQCOM(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('enableYDegamma', ctypes.c_uint32),
        ('enableCbCrDegamma', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkSamplerYcbcrConversionCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'enableYDegamma': 'enable_ydegamma',
        'enableCbCrDegamma': 'enable_cb_cr_degamma',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_QCOM_ycbcr_degamma',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_YCBCR_DEGAMMA_CREATE_INFO_QCOM'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_YCBCR_DEGAMMA_CREATE_INFO_QCOM
        for function in self._init_:
            function(self, *args, **kwargs)

VkSamplerYcbcrConversionYcbcrDegammaCreateInfoQCOM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'enableYDegamma': ctypes.c_uint32,
    'enableCbCrDegamma': ctypes.c_uint32,
}
