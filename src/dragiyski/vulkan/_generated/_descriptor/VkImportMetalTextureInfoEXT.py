from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkImportMetalTextureInfoEXT'
_member_list_ = ['sType', 'pNext', 'plane', 'mtlTexture']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_IMPORT_METAL_TEXTURE_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'plane': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkImageAspectFlagBits',
        'is_string': False,
    },
    'mtlTexture': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = {
    'VkImageCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
