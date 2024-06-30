from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDeviceGroupBindSparseInfo'
_member_list_ = ['sType', 'pNext', 'resourceDeviceIndex', 'memoryDeviceIndex']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DEVICE_GROUP_BIND_SPARSE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'resourceDeviceIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'memoryDeviceIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkBindSparseInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
