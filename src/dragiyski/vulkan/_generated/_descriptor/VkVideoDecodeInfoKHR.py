from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoDecodeInfoKHR'
_member_list_ = ['sType', 'pNext', 'flags', 'srcBuffer', 'srcBufferOffset', 'srcBufferRange', 'dstPictureResource', 'pSetupReferenceSlot', 'referenceSlotCount', 'pReferenceSlots']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_DECODE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkVideoDecodeFlagsKHR',
        'enum': 'VkVideoDecodeFlagsKHR',
        'is_string': False,
    },
    'srcBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'srcBufferOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'srcBufferRange': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'dstPictureResource': {
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
}
_extends_ = set()
_extended_by_ = {
    'VkVideoDecodeAV1PictureInfoKHR',
    'VkVideoDecodeH264PictureInfoKHR',
    'VkVideoDecodeH265PictureInfoKHR',
    'VkVideoInlineQueryInfoKHR',
}
_includes_ = {
    'VkVideoPictureResourceInfoKHR',
    'VkVideoReferenceSlotInfoKHR',
}
_included_in_ = set()
_input_of_ = {
    'vkCmdDecodeVideoKHR',
}
_output_of_ = set()
