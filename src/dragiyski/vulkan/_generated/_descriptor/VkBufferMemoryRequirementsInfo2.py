from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkBufferMemoryRequirementsInfo2'
_member_list_ = ['sType', 'pNext', 'buffer']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_BUFFER_MEMORY_REQUIREMENTS_INFO_2',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'buffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkGetBufferMemoryRequirements2',
}
_output_of_ = set()
