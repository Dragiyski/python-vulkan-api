from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkExternalBufferProperties'
_member_list_ = ['sType', 'pNext', 'externalMemoryProperties']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_EXTERNAL_BUFFER_PROPERTIES',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'externalMemoryProperties': {
        'type': CComplexType('VkExternalMemoryProperties'),
        'type_name': 'VkExternalMemoryProperties',
        'structure': 'VkExternalMemoryProperties',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkExternalMemoryProperties',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetPhysicalDeviceExternalBufferProperties',
}
