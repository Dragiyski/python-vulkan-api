from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDispatchGraphCountInfoAMDX'
_member_list_ = ['count', 'infos', 'stride']
_member_info_ = {
    'count': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'infos': {
        'type': CComplexType('VkDeviceOrHostAddressConstAMDX'),
        'type_name': 'VkDeviceOrHostAddressConstAMDX',
        'union': 'VkDeviceOrHostAddressConstAMDX',
        'is_string': False,
    },
    'stride': {
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
_input_of_ = {
    'vkCmdDispatchGraphAMDX',
    'vkCmdDispatchGraphIndirectAMDX',
}
_output_of_ = set()
