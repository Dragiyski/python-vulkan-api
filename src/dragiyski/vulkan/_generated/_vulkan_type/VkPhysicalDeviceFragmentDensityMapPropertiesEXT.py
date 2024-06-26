import ctypes

class VkPhysicalDeviceFragmentDensityMapPropertiesEXT(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkPhysicalDeviceProperties2',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkExtent2D',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'minFragmentDensityTexelSize': 'min_fragment_density_texel_size',
        'maxFragmentDensityTexelSize': 'max_fragment_density_texel_size',
        'fragmentDensityInvocations': 'fragment_density_invocations',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_fragment_density_map',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_DENSITY_MAP_PROPERTIES_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_DENSITY_MAP_PROPERTIES_EXT
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent2D import VkExtent2D

VkPhysicalDeviceFragmentDensityMapPropertiesEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('minFragmentDensityTexelSize', VkExtent2D),
    ('maxFragmentDensityTexelSize', VkExtent2D),
    ('fragmentDensityInvocations', ctypes.c_uint32),
]

VkPhysicalDeviceFragmentDensityMapPropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'minFragmentDensityTexelSize': VkExtent2D,
    'maxFragmentDensityTexelSize': VkExtent2D,
    'fragmentDensityInvocations': ctypes.c_uint32,
}
