from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkRenderPassSubpassFeedbackInfoEXT'
_member_list_ = ['subpassMergeStatus', 'description', 'postMergeIndex']
_member_info_ = {
    'subpassMergeStatus': {
        'type': CIntType('c_int'),
        'type_name': 'VkSubpassMergeStatusEXT',
        'enum': 'VkSubpassMergeStatusEXT',
        'is_string': False,
    },
    'description': {
        'type': CArrayType(CCharType('c_char'), 256),
        'length': [],
        'is_string': True,
    },
    'postMergeIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkRenderPassSubpassFeedbackCreateInfoEXT',
}
_input_of_ = set()
_output_of_ = set()
