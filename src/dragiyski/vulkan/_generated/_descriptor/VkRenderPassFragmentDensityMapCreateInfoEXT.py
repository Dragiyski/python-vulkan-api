from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkRenderPassFragmentDensityMapCreateInfoEXT'
_member_list_ = ['sType', 'pNext', 'fragmentDensityMapAttachment']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_RENDER_PASS_FRAGMENT_DENSITY_MAP_CREATE_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'fragmentDensityMapAttachment': {
        'type': CComplexType('VkAttachmentReference'),
        'type_name': 'VkAttachmentReference',
        'structure': 'VkAttachmentReference',
        'is_string': False,
    },
}
_extends_ = {
    'VkRenderPassCreateInfo',
    'VkRenderPassCreateInfo2',
}
_extended_by_ = set()
_includes_ = {
    'VkAttachmentReference',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
