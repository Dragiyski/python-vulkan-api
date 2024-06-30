from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoReferenceSlotInfoKHR'
_member_list_ = ['sType', 'pNext', 'slotIndex', 'pPictureResource']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_REFERENCE_SLOT_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'slotIndex': {
        'type': CIntType('c_int32'),
        'is_string': False,
    },
    'pPictureResource': {
        'type': CPointerType(CComplexType('VkVideoPictureResourceInfoKHR')),
        'type_name': 'VkVideoPictureResourceInfoKHR',
        'structure': 'VkVideoPictureResourceInfoKHR',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkVideoDecodeAV1DpbSlotInfoKHR',
    'VkVideoDecodeH264DpbSlotInfoKHR',
    'VkVideoDecodeH265DpbSlotInfoKHR',
    'VkVideoEncodeH264DpbSlotInfoKHR',
    'VkVideoEncodeH265DpbSlotInfoKHR',
}
_includes_ = {
    'VkVideoPictureResourceInfoKHR',
}
_included_in_ = {
    'VkVideoBeginCodingInfoKHR',
    'VkVideoDecodeInfoKHR',
    'VkVideoEncodeInfoKHR',
}
_input_of_ = set()
_output_of_ = set()
