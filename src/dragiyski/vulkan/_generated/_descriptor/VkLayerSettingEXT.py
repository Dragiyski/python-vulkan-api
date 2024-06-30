from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkLayerSettingEXT'
_member_list_ = ['pLayerName', 'pSettingName', 'type', 'valueCount', 'pValues']
_member_info_ = {
    'pLayerName': {
        'type': CStringType('c_char_p'),
        'length': [],
        'is_string': True,
    },
    'pSettingName': {
        'type': CStringType('c_char_p'),
        'length': [],
        'is_string': True,
    },
    'type': {
        'type': CIntType('c_int'),
        'type_name': 'VkLayerSettingTypeEXT',
        'enum': 'VkLayerSettingTypeEXT',
        'is_string': False,
    },
    'valueCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pValues': {
        'type': CIntType('c_void_p'),
        'length': [['valueCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkLayerSettingsCreateInfoEXT',
}
_input_of_ = set()
_output_of_ = set()
