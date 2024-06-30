from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSparseImageOpaqueMemoryBindInfo'
_member_list_ = ['image', 'bindCount', 'pBinds']
_member_info_ = {
    'image': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'bindCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pBinds': {
        'type': CPointerType(CComplexType('VkSparseMemoryBind')),
        'type_name': 'VkSparseMemoryBind',
        'structure': 'VkSparseMemoryBind',
        'length': [['bindCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkSparseMemoryBind',
}
_included_in_ = {
    'VkBindSparseInfo',
}
_input_of_ = set()
_output_of_ = set()
