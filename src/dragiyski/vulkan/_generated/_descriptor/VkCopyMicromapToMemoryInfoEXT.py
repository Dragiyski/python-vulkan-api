from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkCopyMicromapToMemoryInfoEXT'
_member_list_ = ['sType', 'pNext', 'src', 'dst', 'mode']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_COPY_MICROMAP_TO_MEMORY_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'src': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'dst': {
        'type': CComplexType('VkDeviceOrHostAddressKHR'),
        'type_name': 'VkDeviceOrHostAddressKHR',
        'union': 'VkDeviceOrHostAddressKHR',
        'is_string': False,
    },
    'mode': {
        'type': CIntType('c_int'),
        'type_name': 'VkCopyMicromapModeEXT',
        'enum': 'VkCopyMicromapModeEXT',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkDeviceOrHostAddressKHR',
}
_included_in_ = set()
_input_of_ = {
    'vkCmdCopyMicromapToMemoryEXT',
    'vkCopyMicromapToMemoryEXT',
}
_output_of_ = set()
