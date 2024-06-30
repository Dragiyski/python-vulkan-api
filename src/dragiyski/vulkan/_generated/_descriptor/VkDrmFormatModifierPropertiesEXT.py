from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDrmFormatModifierPropertiesEXT'
_member_list_ = ['drmFormatModifier', 'drmFormatModifierPlaneCount', 'drmFormatModifierTilingFeatures']
_member_info_ = {
    'drmFormatModifier': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'drmFormatModifierPlaneCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'drmFormatModifierTilingFeatures': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkFormatFeatureFlags',
        'enum': 'VkFormatFeatureFlags',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkDrmFormatModifierPropertiesListEXT',
}
_input_of_ = set()
_output_of_ = set()
