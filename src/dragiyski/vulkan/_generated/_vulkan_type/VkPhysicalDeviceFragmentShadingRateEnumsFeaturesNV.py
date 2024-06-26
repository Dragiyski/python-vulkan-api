import ctypes

class VkPhysicalDeviceFragmentShadingRateEnumsFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('fragmentShadingRateEnums', ctypes.c_uint32),
        ('supersampleFragmentShadingRates', ctypes.c_uint32),
        ('noInvocationFragmentShadingRates', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkDeviceCreateInfo',
        'VkPhysicalDeviceFeatures2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'fragmentShadingRateEnums': 'fragment_shading_rate_enums',
        'supersampleFragmentShadingRates': 'supersample_fragment_shading_rates',
        'noInvocationFragmentShadingRates': 'no_invocation_fragment_shading_rates',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_fragment_shading_rate_enums',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADING_RATE_ENUMS_FEATURES_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADING_RATE_ENUMS_FEATURES_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceFragmentShadingRateEnumsFeaturesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'fragmentShadingRateEnums': ctypes.c_uint32,
    'supersampleFragmentShadingRates': ctypes.c_uint32,
    'noInvocationFragmentShadingRates': ctypes.c_uint32,
}
