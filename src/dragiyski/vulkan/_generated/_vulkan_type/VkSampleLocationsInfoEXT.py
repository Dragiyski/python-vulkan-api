import ctypes

class VkSampleLocationsInfoEXT(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkImageMemoryBarrier',
        'VkImageMemoryBarrier2',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkExtent2D',
        'VkSampleLocationEXT',
    }
    _included_in_ = {
        'VkAttachmentSampleLocationsEXT',
        'VkPipelineSampleLocationsStateCreateInfoEXT',
        'VkSubpassSampleLocationsEXT',
    }
    _input_of_ = {
        'vkCmdSetSampleLocationsEXT',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'sampleLocationsPerPixel': 'sample_locations_per_pixel',
        'sampleLocationGridSize': 'sample_location_grid_size',
        'sampleLocationsCount': 'sample_locations_count',
        'pSampleLocations': 'sample_locations',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_sample_locations',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SAMPLE_LOCATIONS_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SAMPLE_LOCATIONS_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent2D import VkExtent2D
from .VkSampleLocationEXT import VkSampleLocationEXT

VkSampleLocationsInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('sampleLocationsPerPixel', ctypes.c_uint32),
    ('sampleLocationGridSize', VkExtent2D),
    ('sampleLocationsCount', ctypes.c_uint32),
    ('pSampleLocations', ctypes.POINTER(VkSampleLocationEXT)),
]

VkSampleLocationsInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'sampleLocationsPerPixel': ctypes.c_uint32,
    'sampleLocationGridSize': VkExtent2D,
    'sampleLocationsCount': ctypes.c_uint32,
    'pSampleLocations': ctypes.POINTER(VkSampleLocationEXT),
}
