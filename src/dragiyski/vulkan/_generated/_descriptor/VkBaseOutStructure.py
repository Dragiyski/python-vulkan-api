from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkBaseOutStructure'
_member_list_ = ['sType', 'pNext']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'is_string': False,
    },
    'pNext': {
        'type': CPointerType(CComplexType('VkBaseOutStructure')),
        'type_name': 'VkBaseOutStructure',
        'structure': 'VkBaseOutStructure',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkBaseOutStructure',
}
_included_in_ = {
    'VkBaseOutStructure',
}
_input_of_ = set()
_output_of_ = {
    'vkGetPipelinePropertiesEXT',
}
