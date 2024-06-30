from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkStridedDeviceAddressRegionKHR'
_member_list_ = ['deviceAddress', 'stride', 'size']
_member_info_ = {
    'deviceAddress': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'stride': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'size': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCmdTraceRaysIndirectKHR',
    'vkCmdTraceRaysKHR',
}
_output_of_ = set()
