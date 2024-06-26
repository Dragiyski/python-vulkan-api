import ctypes

class VkPhysicalDeviceFragmentShadingRateKHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkExtent2D',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetPhysicalDeviceFragmentShadingRatesKHR',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'sampleCounts': 'sample_counts',
        'fragmentSize': 'fragment_size',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_fragment_shading_rate',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'sampleCounts': 'VkSampleCountFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADING_RATE_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADING_RATE_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent2D import VkExtent2D

VkPhysicalDeviceFragmentShadingRateKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('sampleCounts', ctypes.c_uint32),
    ('fragmentSize', VkExtent2D),
]

VkPhysicalDeviceFragmentShadingRateKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'sampleCounts': ctypes.c_uint32,
    'fragmentSize': VkExtent2D,
}
