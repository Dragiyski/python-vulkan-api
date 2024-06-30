from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineExecutablePropertiesKHR'
_member_list_ = ['sType', 'pNext', 'stages', 'name', 'description', 'subgroupSize']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_EXECUTABLE_PROPERTIES_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'stages': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkShaderStageFlags',
        'enum': 'VkShaderStageFlags',
        'is_string': False,
    },
    'name': {
        'type': CArrayType(CCharType('c_char'), 256),
        'length': [],
        'is_string': True,
    },
    'description': {
        'type': CArrayType(CCharType('c_char'), 256),
        'length': [],
        'is_string': True,
    },
    'subgroupSize': {
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
    'vkGetPipelineExecutablePropertiesKHR',
}
