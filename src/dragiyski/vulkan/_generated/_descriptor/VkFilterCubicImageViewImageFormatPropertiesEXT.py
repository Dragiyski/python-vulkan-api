from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkFilterCubicImageViewImageFormatPropertiesEXT'
_member_list_ = ['sType', 'pNext', 'filterCubic', 'filterCubicMinmax']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_FILTER_CUBIC_IMAGE_VIEW_IMAGE_FORMAT_PROPERTIES_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'filterCubic': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'filterCubicMinmax': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkImageFormatProperties2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
