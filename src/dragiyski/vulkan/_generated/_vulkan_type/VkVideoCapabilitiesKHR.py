import ctypes

class VkVideoCapabilitiesKHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkVideoDecodeAV1CapabilitiesKHR',
        'VkVideoDecodeCapabilitiesKHR',
        'VkVideoDecodeH264CapabilitiesKHR',
        'VkVideoDecodeH265CapabilitiesKHR',
        'VkVideoEncodeCapabilitiesKHR',
        'VkVideoEncodeH264CapabilitiesKHR',
        'VkVideoEncodeH265CapabilitiesKHR',
    }
    _includes_ = {
        'VkExtensionProperties',
        'VkExtent2D',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetPhysicalDeviceVideoCapabilitiesKHR',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'minBitstreamBufferOffsetAlignment': 'min_bitstream_buffer_offset_alignment',
        'minBitstreamBufferSizeAlignment': 'min_bitstream_buffer_size_alignment',
        'pictureAccessGranularity': 'picture_access_granularity',
        'minCodedExtent': 'min_coded_extent',
        'maxCodedExtent': 'max_coded_extent',
        'maxDpbSlots': 'max_dpb_slots',
        'maxActiveReferencePictures': 'max_active_reference_pictures',
        'stdHeaderVersion': 'std_header_version',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_queue',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkVideoCapabilityFlagsKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_CAPABILITIES_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_CAPABILITIES_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtensionProperties import VkExtensionProperties
from .VkExtent2D import VkExtent2D

VkVideoCapabilitiesKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('minBitstreamBufferOffsetAlignment', ctypes.c_uint64),
    ('minBitstreamBufferSizeAlignment', ctypes.c_uint64),
    ('pictureAccessGranularity', VkExtent2D),
    ('minCodedExtent', VkExtent2D),
    ('maxCodedExtent', VkExtent2D),
    ('maxDpbSlots', ctypes.c_uint32),
    ('maxActiveReferencePictures', ctypes.c_uint32),
    ('stdHeaderVersion', VkExtensionProperties),
]

VkVideoCapabilitiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'minBitstreamBufferOffsetAlignment': ctypes.c_uint64,
    'minBitstreamBufferSizeAlignment': ctypes.c_uint64,
    'pictureAccessGranularity': VkExtent2D,
    'minCodedExtent': VkExtent2D,
    'maxCodedExtent': VkExtent2D,
    'maxDpbSlots': ctypes.c_uint32,
    'maxActiveReferencePictures': ctypes.c_uint32,
    'stdHeaderVersion': VkExtensionProperties,
}
