from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkOutOfBandQueueTypeInfoNV'
_member_list_ = ['sType', 'pNext', 'queueType']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_OUT_OF_BAND_QUEUE_TYPE_INFO_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'queueType': {
        'type': CIntType('c_int'),
        'type_name': 'VkOutOfBandQueueTypeNV',
        'enum': 'VkOutOfBandQueueTypeNV',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkQueueNotifyOutOfBandNV',
}
_output_of_ = set()
