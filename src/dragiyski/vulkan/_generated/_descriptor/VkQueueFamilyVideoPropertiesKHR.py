from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkQueueFamilyVideoPropertiesKHR'
_member_list_ = ['sType', 'pNext', 'videoCodecOperations']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_QUEUE_FAMILY_VIDEO_PROPERTIES_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'videoCodecOperations': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkVideoCodecOperationFlagsKHR',
        'enum': 'VkVideoCodecOperationFlagsKHR',
        'is_string': False,
    },
}
_extends_ = {
    'VkQueueFamilyProperties2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
