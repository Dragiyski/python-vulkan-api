from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkImageViewMinLodCreateInfoEXT'
_member_list_ = ['sType', 'pNext', 'minLod']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_IMAGE_VIEW_MIN_LOD_CREATE_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'minLod': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
}
_extends_ = {
    'VkImageViewCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
