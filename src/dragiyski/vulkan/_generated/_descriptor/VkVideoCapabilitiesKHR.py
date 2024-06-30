from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoCapabilitiesKHR'
_member_list_ = ['sType', 'pNext', 'flags', 'minBitstreamBufferOffsetAlignment', 'minBitstreamBufferSizeAlignment', 'pictureAccessGranularity', 'minCodedExtent', 'maxCodedExtent', 'maxDpbSlots', 'maxActiveReferencePictures', 'stdHeaderVersion']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_CAPABILITIES_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkVideoCapabilityFlagsKHR',
        'enum': 'VkVideoCapabilityFlagsKHR',
        'is_string': False,
    },
    'minBitstreamBufferOffsetAlignment': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'minBitstreamBufferSizeAlignment': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'pictureAccessGranularity': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
    'minCodedExtent': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
    'maxCodedExtent': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
    'maxDpbSlots': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxActiveReferencePictures': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'stdHeaderVersion': {
        'type': CComplexType('VkExtensionProperties'),
        'type_name': 'VkExtensionProperties',
        'structure': 'VkExtensionProperties',
        'is_string': False,
    },
}
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
