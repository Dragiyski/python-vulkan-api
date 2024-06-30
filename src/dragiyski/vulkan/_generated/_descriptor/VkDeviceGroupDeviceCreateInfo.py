from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDeviceGroupDeviceCreateInfo'
_member_list_ = ['sType', 'pNext', 'physicalDeviceCount', 'pPhysicalDevices']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DEVICE_GROUP_DEVICE_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'physicalDeviceCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pPhysicalDevices': {
        'type': CPointerType(CIntType('c_void_p')),
        'length': [['physicalDeviceCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkDeviceCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
