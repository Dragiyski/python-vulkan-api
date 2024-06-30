from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoEncodeH265CapabilitiesKHR'
_member_list_ = ['sType', 'pNext', 'flags', 'maxLevelIdc', 'maxSliceSegmentCount', 'maxTiles', 'ctbSizes', 'transformBlockSizes', 'maxPPictureL0ReferenceCount', 'maxBPictureL0ReferenceCount', 'maxL1ReferenceCount', 'maxSubLayerCount', 'expectDyadicTemporalSubLayerPattern', 'minQp', 'maxQp', 'prefersGopRemainingFrames', 'requiresGopRemainingFrames', 'stdSyntaxFlags']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_CAPABILITIES_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkVideoEncodeH265CapabilityFlagsKHR',
        'enum': 'VkVideoEncodeH265CapabilityFlagsKHR',
        'is_string': False,
    },
    'maxLevelIdc': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoH265LevelIdc',
        'enum': 'StdVideoH265LevelIdc',
        'is_string': False,
    },
    'maxSliceSegmentCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxTiles': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
    'ctbSizes': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkVideoEncodeH265CtbSizeFlagsKHR',
        'enum': 'VkVideoEncodeH265CtbSizeFlagsKHR',
        'is_string': False,
    },
    'transformBlockSizes': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkVideoEncodeH265TransformBlockSizeFlagsKHR',
        'enum': 'VkVideoEncodeH265TransformBlockSizeFlagsKHR',
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
    'maxSubLayerCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'expectDyadicTemporalSubLayerPattern': {
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
        'type_name': 'VkVideoEncodeH265StdFlagsKHR',
        'enum': 'VkVideoEncodeH265StdFlagsKHR',
        'is_string': False,
    },
}
_extends_ = {
    'VkVideoCapabilitiesKHR',
}
_extended_by_ = set()
_includes_ = {
    'VkExtent2D',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
