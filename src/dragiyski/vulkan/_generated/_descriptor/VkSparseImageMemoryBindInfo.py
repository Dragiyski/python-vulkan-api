from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSparseImageMemoryBindInfo'
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
        'type': CPointerType(CComplexType('VkSparseImageMemoryBind')),
        'type_name': 'VkSparseImageMemoryBind',
        'structure': 'VkSparseImageMemoryBind',
        'length': [['bindCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkSparseImageMemoryBind',
}
_included_in_ = {
    'VkBindSparseInfo',
}
_input_of_ = set()
_output_of_ = set()
