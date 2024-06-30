from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkMutableDescriptorTypeListEXT'
_member_list_ = ['descriptorTypeCount', 'pDescriptorTypes']
_member_info_ = {
    'descriptorTypeCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pDescriptorTypes': {
        'type': CPointerType(CIntType('c_int')),
        'type_name': 'VkDescriptorType',
        'enum': 'VkDescriptorType',
        'length': [['descriptorTypeCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkMutableDescriptorTypeCreateInfoEXT',
}
_input_of_ = set()
_output_of_ = set()
