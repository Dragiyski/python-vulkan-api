from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDeviceFaultCountsEXT'
_member_list_ = ['sType', 'pNext', 'addressInfoCount', 'vendorInfoCount', 'vendorBinarySize']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DEVICE_FAULT_COUNTS_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'addressInfoCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'vendorInfoCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'vendorBinarySize': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetDeviceFaultInfoEXT',
}
