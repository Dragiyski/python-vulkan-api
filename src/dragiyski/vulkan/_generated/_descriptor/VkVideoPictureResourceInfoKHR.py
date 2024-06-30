from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoPictureResourceInfoKHR'
_member_list_ = ['sType', 'pNext', 'codedOffset', 'codedExtent', 'baseArrayLayer', 'imageViewBinding']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_PICTURE_RESOURCE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'codedOffset': {
        'type': CComplexType('VkOffset2D'),
        'type_name': 'VkOffset2D',
        'structure': 'VkOffset2D',
        'is_string': False,
    },
    'codedExtent': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
    'baseArrayLayer': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'imageViewBinding': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkExtent2D',
    'VkOffset2D',
}
_included_in_ = {
    'VkVideoDecodeInfoKHR',
    'VkVideoEncodeInfoKHR',
    'VkVideoReferenceSlotInfoKHR',
}
_input_of_ = set()
_output_of_ = set()
