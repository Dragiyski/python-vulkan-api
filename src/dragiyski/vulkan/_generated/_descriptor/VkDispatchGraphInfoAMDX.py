from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDispatchGraphInfoAMDX'
_member_list_ = ['nodeIndex', 'payloadCount', 'payloads', 'payloadStride']
_member_info_ = {
    'nodeIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'payloadCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'payloads': {
        'type': CComplexType('VkDeviceOrHostAddressConstAMDX'),
        'type_name': 'VkDeviceOrHostAddressConstAMDX',
        'union': 'VkDeviceOrHostAddressConstAMDX',
        'is_string': False,
    },
    'payloadStride': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkDeviceOrHostAddressConstAMDX',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
