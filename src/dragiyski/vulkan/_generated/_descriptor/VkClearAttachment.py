from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkClearAttachment'
_member_list_ = ['aspectMask', 'colorAttachment', 'clearValue']
_member_info_ = {
    'aspectMask': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkImageAspectFlags',
        'enum': 'VkImageAspectFlags',
        'is_string': False,
    },
    'colorAttachment': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'clearValue': {
        'type': CComplexType('VkClearValue'),
        'type_name': 'VkClearValue',
        'union': 'VkClearValue',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkClearValue',
}
_included_in_ = set()
_input_of_ = {
    'vkCmdClearAttachments',
}
_output_of_ = set()
