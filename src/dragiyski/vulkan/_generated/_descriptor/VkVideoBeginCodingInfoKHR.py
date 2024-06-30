from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoBeginCodingInfoKHR'
_member_list_ = ['sType', 'pNext', 'flags', 'videoSession', 'videoSessionParameters', 'referenceSlotCount', 'pReferenceSlots']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_BEGIN_CODING_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkVideoBeginCodingFlagsKHR',
        'enum': 'VkVideoBeginCodingFlagsKHR',
        'is_string': False,
    },
    'videoSession': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'videoSessionParameters': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'referenceSlotCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pReferenceSlots': {
        'type': CPointerType(CComplexType('VkVideoReferenceSlotInfoKHR')),
        'type_name': 'VkVideoReferenceSlotInfoKHR',
        'structure': 'VkVideoReferenceSlotInfoKHR',
        'length': [['referenceSlotCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkVideoEncodeH264GopRemainingFrameInfoKHR',
    'VkVideoEncodeH264RateControlInfoKHR',
    'VkVideoEncodeH265GopRemainingFrameInfoKHR',
    'VkVideoEncodeH265RateControlInfoKHR',
    'VkVideoEncodeRateControlInfoKHR',
}
_includes_ = {
    'VkVideoReferenceSlotInfoKHR',
}
_included_in_ = set()
_input_of_ = {
    'vkCmdBeginVideoCodingKHR',
}
_output_of_ = set()
