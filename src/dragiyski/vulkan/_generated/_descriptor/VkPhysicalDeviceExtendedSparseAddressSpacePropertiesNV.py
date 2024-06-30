from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceExtendedSparseAddressSpacePropertiesNV'
_member_list_ = ['sType', 'pNext', 'extendedSparseAddressSpaceSize', 'extendedSparseImageUsageFlags', 'extendedSparseBufferUsageFlags']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTENDED_SPARSE_ADDRESS_SPACE_PROPERTIES_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'extendedSparseAddressSpaceSize': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'extendedSparseImageUsageFlags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkImageUsageFlags',
        'enum': 'VkImageUsageFlags',
        'is_string': False,
    },
    'extendedSparseBufferUsageFlags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkBufferUsageFlags',
        'enum': 'VkBufferUsageFlags',
        'is_string': False,
    },
}
_extends_ = {
    'VkPhysicalDeviceProperties2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
