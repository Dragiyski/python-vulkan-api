from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoEncodeH264CapabilitiesKHR'
_member_list_ = ['sType', 'pNext', 'flags', 'maxLevelIdc', 'maxSliceCount', 'maxPPictureL0ReferenceCount', 'maxBPictureL0ReferenceCount', 'maxL1ReferenceCount', 'maxTemporalLayerCount', 'expectDyadicTemporalLayerPattern', 'minQp', 'maxQp', 'prefersGopRemainingFrames', 'requiresGopRemainingFrames', 'stdSyntaxFlags']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_CAPABILITIES_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkVideoEncodeH264CapabilityFlagsKHR',
        'enum': 'VkVideoEncodeH264CapabilityFlagsKHR',
        'is_string': False,
    },
    'maxLevelIdc': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoH264LevelIdc',
        'enum': 'StdVideoH264LevelIdc',
        'is_string': False,
    },
    'maxSliceCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxPPictureL0ReferenceCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxBPictureL0ReferenceCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxL1ReferenceCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxTemporalLayerCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'expectDyadicTemporalLayerPattern': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'minQp': {
        'type': CIntType('c_int32'),
        'is_string': False,
    },
    'maxQp': {
        'type': CIntType('c_int32'),
        'is_string': False,
    },
    'prefersGopRemainingFrames': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'requiresGopRemainingFrames': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'stdSyntaxFlags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkVideoEncodeH264StdFlagsKHR',
        'enum': 'VkVideoEncodeH264StdFlagsKHR',
        'is_string': False,
    },
}
_extends_ = {
    'VkVideoCapabilitiesKHR',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
