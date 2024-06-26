import ctypes

class VkPhysicalDeviceSampleLocationsPropertiesEXT(ctypes.Structure):
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
        'sampleLocationSampleCounts': 'sample_location_sample_counts',
        'maxSampleLocationGridSize': 'max_sample_location_grid_size',
        'sampleLocationCoordinateRange': 'sample_location_coordinate_range',
        'sampleLocationSubPixelBits': 'sample_location_sub_pixel_bits',
        'variableSampleLocations': 'variable_sample_locations',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_sample_locations',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'sampleLocationSampleCounts': 'VkSampleCountFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SAMPLE_LOCATIONS_PROPERTIES_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SAMPLE_LOCATIONS_PROPERTIES_EXT
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent2D import VkExtent2D

VkPhysicalDeviceSampleLocationsPropertiesEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('sampleLocationSampleCounts', ctypes.c_uint32),
    ('maxSampleLocationGridSize', VkExtent2D),
    ('sampleLocationCoordinateRange', ctypes.ARRAY(ctypes.c_float, 2)),
    ('sampleLocationSubPixelBits', ctypes.c_uint32),
    ('variableSampleLocations', ctypes.c_uint32),
]

VkPhysicalDeviceSampleLocationsPropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'sampleLocationSampleCounts': ctypes.c_uint32,
    'maxSampleLocationGridSize': VkExtent2D,
    'sampleLocationCoordinateRange': ctypes.ARRAY(ctypes.c_float, 2),
    'sampleLocationSubPixelBits': ctypes.c_uint32,
    'variableSampleLocations': ctypes.c_uint32,
}
