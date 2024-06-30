from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkCopyMemoryToAccelerationStructureInfoKHR'
_member_list_ = ['sType', 'pNext', 'src', 'dst', 'mode']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_COPY_MEMORY_TO_ACCELERATION_STRUCTURE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'src': {
        'type': CComplexType('VkDeviceOrHostAddressConstKHR'),
        'type_name': 'VkDeviceOrHostAddressConstKHR',
        'union': 'VkDeviceOrHostAddressConstKHR',
        'is_string': False,
    },
    'dst': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'mode': {
        'type': CIntType('c_int'),
        'type_name': 'VkCopyAccelerationStructureModeKHR',
        'enum': 'VkCopyAccelerationStructureModeKHR',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkDeviceOrHostAddressConstKHR',
}
_included_in_ = set()
_input_of_ = {
    'vkCmdCopyMemoryToAccelerationStructureKHR',
    'vkCopyMemoryToAccelerationStructureKHR',
}
_output_of_ = set()
