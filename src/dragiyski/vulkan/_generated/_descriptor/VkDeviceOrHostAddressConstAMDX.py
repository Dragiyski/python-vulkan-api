from ..._ctypes import *

_category_ = 'union'
_name_ = 'VkDeviceOrHostAddressConstAMDX'
_member_list_ = ['deviceAddress', 'hostAddress']
_member_info_ = {
    'deviceAddress': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'hostAddress': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkDispatchGraphCountInfoAMDX',
    'VkDispatchGraphInfoAMDX',
}
_input_of_ = set()
_output_of_ = set()
