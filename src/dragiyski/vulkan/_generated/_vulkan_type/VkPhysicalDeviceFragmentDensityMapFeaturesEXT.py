import ctypes

class VkPhysicalDeviceFragmentDensityMapFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('fragmentDensityMap', ctypes.c_uint32),
        ('fragmentDensityMapDynamic', ctypes.c_uint32),
        ('fragmentDensityMapNonSubsampledImages', ctypes.c_uint32),
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
        'fragmentDensityMap': 'fragment_density_map',
        'fragmentDensityMapDynamic': 'fragment_density_map_dynamic',
        'fragmentDensityMapNonSubsampledImages': 'fragment_density_map_non_subsampled_images',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_fragment_density_map',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_DENSITY_MAP_FEATURES_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_DENSITY_MAP_FEATURES_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceFragmentDensityMapFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'fragmentDensityMap': ctypes.c_uint32,
    'fragmentDensityMapDynamic': ctypes.c_uint32,
    'fragmentDensityMapNonSubsampledImages': ctypes.c_uint32,
}
