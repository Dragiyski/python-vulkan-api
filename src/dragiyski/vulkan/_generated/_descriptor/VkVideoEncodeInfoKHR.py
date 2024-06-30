from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoEncodeInfoKHR'
_member_list_ = ['sType', 'pNext', 'flags', 'dstBuffer', 'dstBufferOffset', 'dstBufferRange', 'srcPictureResource', 'pSetupReferenceSlot', 'referenceSlotCount', 'pReferenceSlots', 'precedingExternallyEncodedBytes']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkVideoEncodeFlagsKHR',
        'enum': 'VkVideoEncodeFlagsKHR',
        'is_string': False,
    },
    'dstBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'dstBufferOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'dstBufferRange': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'srcPictureResource': {
        'type': CComplexType('VkVideoPictureResourceInfoKHR'),
        'type_name': 'VkVideoPictureResourceInfoKHR',
        'structure': 'VkVideoPictureResourceInfoKHR',
        'is_string': False,
    },
    'pSetupReferenceSlot': {
        'type': CPointerType(CComplexType('VkVideoReferenceSlotInfoKHR')),
        'type_name': 'VkVideoReferenceSlotInfoKHR',
        'structure': 'VkVideoReferenceSlotInfoKHR',
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
    'precedingExternallyEncodedBytes': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkVideoEncodeH264PictureInfoKHR',
    'VkVideoEncodeH265PictureInfoKHR',
    'VkVideoInlineQueryInfoKHR',
}
_includes_ = {
    'VkVideoPictureResourceInfoKHR',
    'VkVideoReferenceSlotInfoKHR',
}
_included_in_ = set()
_input_of_ = {
    'vkCmdEncodeVideoKHR',
}
_output_of_ = set()
