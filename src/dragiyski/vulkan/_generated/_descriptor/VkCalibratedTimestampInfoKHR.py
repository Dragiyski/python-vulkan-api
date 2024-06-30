from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkCalibratedTimestampInfoKHR'
_member_list_ = ['sType', 'pNext', 'timeDomain']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_CALIBRATED_TIMESTAMP_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'timeDomain': {
        'type': CIntType('c_int'),
        'type_name': 'VkTimeDomainKHR',
        'enum': 'VkTimeDomainKHR',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkGetCalibratedTimestampsKHR',
}
_output_of_ = set()
