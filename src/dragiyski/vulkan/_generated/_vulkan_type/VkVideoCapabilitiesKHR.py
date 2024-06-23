import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtensionProperties import CType as VkExtensionProperties
from .VkExtent2D import CType as VkExtent2D

CType._fields_ = [
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

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkVideoDecodeAV1CapabilitiesKHR',
        'VkVideoDecodeCapabilitiesKHR',
        'VkVideoDecodeH264CapabilitiesKHR',
        'VkVideoDecodeH265CapabilitiesKHR',
        'VkVideoEncodeCapabilitiesKHR',
        'VkVideoEncodeH264CapabilitiesKHR',
        'VkVideoEncodeH265CapabilitiesKHR',
    },
    'includes': {
        'VkExtensionProperties',
        'VkExtent2D',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceVideoCapabilitiesKHR',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_CAPABILITIES_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkVideoCapabilityFlagsKHR'},
        'minBitstreamBufferOffsetAlignment': {'python_name': ['min', 'bitstream', 'buffer', 'offset', 'alignment']},
        'minBitstreamBufferSizeAlignment': {'python_name': ['min', 'bitstream', 'buffer', 'size', 'alignment']},
        'pictureAccessGranularity': {'python_name': ['picture', 'access', 'granularity'], 'type': 'VkExtent2D'},
        'minCodedExtent': {'python_name': ['min', 'coded', 'extent'], 'type': 'VkExtent2D'},
        'maxCodedExtent': {'python_name': ['max', 'coded', 'extent'], 'type': 'VkExtent2D'},
        'maxDpbSlots': {'python_name': ['max', 'dpb', 'slots']},
        'maxActiveReferencePictures': {'python_name': ['max', 'active', 'reference', 'pictures']},
        'stdHeaderVersion': {'python_name': ['std', 'header', 'version'], 'type': 'VkExtensionProperties'},
    }
}
