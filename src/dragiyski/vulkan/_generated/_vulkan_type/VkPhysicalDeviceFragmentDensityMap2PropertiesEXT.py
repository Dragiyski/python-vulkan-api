import ctypes

class VkPhysicalDeviceFragmentDensityMap2PropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('subsampledLoads', ctypes.c_uint32),
        ('subsampledCoarseReconstructionEarlyAccess', ctypes.c_uint32),
        ('maxSubsampledArrayLayers', ctypes.c_uint32),
        ('maxDescriptorSetSubsampledSamplers', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkPhysicalDeviceProperties2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'subsampledLoads': 'subsampled_loads',
        'subsampledCoarseReconstructionEarlyAccess': 'subsampled_coarse_reconstruction_early_access',
        'maxSubsampledArrayLayers': 'max_subsampled_array_layers',
        'maxDescriptorSetSubsampledSamplers': 'max_descriptor_set_subsampled_samplers',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_fragment_density_map2',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_DENSITY_MAP_2_PROPERTIES_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_DENSITY_MAP_2_PROPERTIES_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceFragmentDensityMap2PropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'subsampledLoads': ctypes.c_uint32,
    'subsampledCoarseReconstructionEarlyAccess': ctypes.c_uint32,
    'maxSubsampledArrayLayers': ctypes.c_uint32,
    'maxDescriptorSetSubsampledSamplers': ctypes.c_uint32,
}
