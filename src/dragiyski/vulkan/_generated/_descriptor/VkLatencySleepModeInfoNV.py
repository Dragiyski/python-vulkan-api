from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkLatencySleepModeInfoNV'
_member_list_ = ['sType', 'pNext', 'lowLatencyMode', 'lowLatencyBoost', 'minimumIntervalUs']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_LATENCY_SLEEP_MODE_INFO_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'lowLatencyMode': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'lowLatencyBoost': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'minimumIntervalUs': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkSetLatencySleepModeNV',
}
_output_of_ = set()
