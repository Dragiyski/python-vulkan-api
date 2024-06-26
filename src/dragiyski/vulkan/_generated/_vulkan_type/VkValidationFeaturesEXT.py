import ctypes

class VkValidationFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('enabledValidationFeatureCount', ctypes.c_uint32),
        ('pEnabledValidationFeatures', ctypes.POINTER(ctypes.c_int)),
        ('disabledValidationFeatureCount', ctypes.c_uint32),
        ('pDisabledValidationFeatures', ctypes.POINTER(ctypes.c_int)),
    ]

    _init_ = []
    _extends_ = {
        'VkInstanceCreateInfo',
        'VkShaderCreateInfoEXT',
        'VkShaderModuleCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'enabledValidationFeatureCount': 'enabled_validation_feature_count',
        'pEnabledValidationFeatures': 'enabled_validation_features',
        'disabledValidationFeatureCount': 'disabled_validation_feature_count',
        'pDisabledValidationFeatures': 'disabled_validation_features',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_validation_features',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'pEnabledValidationFeatures': 'VkValidationFeatureEnableEXT',
        'pDisabledValidationFeatures': 'VkValidationFeatureDisableEXT',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VALIDATION_FEATURES_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VALIDATION_FEATURES_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkValidationFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'enabledValidationFeatureCount': ctypes.c_uint32,
    'pEnabledValidationFeatures': ctypes.POINTER(ctypes.c_int),
    'disabledValidationFeatureCount': ctypes.c_uint32,
    'pDisabledValidationFeatures': ctypes.POINTER(ctypes.c_int),
}
