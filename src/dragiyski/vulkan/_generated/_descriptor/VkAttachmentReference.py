from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkAttachmentReference'
_member_list_ = ['attachment', 'layout']
_member_info_ = {
    'attachment': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'layout': {
        'type': CIntType('c_int'),
        'type_name': 'VkImageLayout',
        'enum': 'VkImageLayout',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkRenderPassFragmentDensityMapCreateInfoEXT',
    'VkSubpassDescription',
}
_input_of_ = set()
_output_of_ = set()
