from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDeviceFaultAddressInfoEXT'
_member_list_ = ['addressType', 'reportedAddress', 'addressPrecision']
_member_info_ = {
    'addressType': {
        'type': CIntType('c_int'),
        'type_name': 'VkDeviceFaultAddressTypeEXT',
        'enum': 'VkDeviceFaultAddressTypeEXT',
        'is_string': False,
    },
    'reportedAddress': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'addressPrecision': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkDeviceFaultInfoEXT',
}
_input_of_ = set()
_output_of_ = set()
