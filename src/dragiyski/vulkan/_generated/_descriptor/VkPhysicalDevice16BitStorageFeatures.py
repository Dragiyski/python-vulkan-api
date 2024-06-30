from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDevice16BitStorageFeatures'
_member_list_ = ['sType', 'pNext', 'storageBuffer16BitAccess', 'uniformAndStorageBuffer16BitAccess', 'storagePushConstant16', 'storageInputOutput16']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_16BIT_STORAGE_FEATURES',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'storageBuffer16BitAccess': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'uniformAndStorageBuffer16BitAccess': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'storagePushConstant16': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'storageInputOutput16': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkDeviceCreateInfo',
    'VkPhysicalDeviceFeatures2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
