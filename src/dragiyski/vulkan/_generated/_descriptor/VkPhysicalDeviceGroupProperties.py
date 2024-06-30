from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceGroupProperties'
_member_list_ = ['sType', 'pNext', 'physicalDeviceCount', 'physicalDevices', 'subsetAllocation']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_GROUP_PROPERTIES',
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
    'physicalDevices': {
        'type': CArrayType(CIntType('c_void_p'), 32),
        'length': [['physicalDeviceCount']],
        'is_string': False,
    },
    'subsetAllocation': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkEnumeratePhysicalDeviceGroups',
}
