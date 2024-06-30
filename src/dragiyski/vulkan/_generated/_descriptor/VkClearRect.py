from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkClearRect'
_member_list_ = ['rect', 'baseArrayLayer', 'layerCount']
_member_info_ = {
    'rect': {
        'type': CComplexType('VkRect2D'),
        'type_name': 'VkRect2D',
        'structure': 'VkRect2D',
        'is_string': False,
    },
    'baseArrayLayer': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'layerCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkRect2D',
}
_included_in_ = set()
_input_of_ = {
    'vkCmdClearAttachments',
}
_output_of_ = set()
