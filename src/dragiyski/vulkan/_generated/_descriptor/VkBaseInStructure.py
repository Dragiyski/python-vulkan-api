from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkBaseInStructure'
_member_list_ = ['sType', 'pNext']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'is_string': False,
    },
    'pNext': {
        'type': CPointerType(CComplexType('VkBaseInStructure')),
        'type_name': 'VkBaseInStructure',
        'structure': 'VkBaseInStructure',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkBaseInStructure',
}
_included_in_ = {
    'VkBaseInStructure',
}
_input_of_ = set()
_output_of_ = set()
