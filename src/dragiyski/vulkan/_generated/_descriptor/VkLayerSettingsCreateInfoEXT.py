from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkLayerSettingsCreateInfoEXT'
_member_list_ = ['sType', 'pNext', 'settingCount', 'pSettings']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_LAYER_SETTINGS_CREATE_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'settingCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pSettings': {
        'type': CPointerType(CComplexType('VkLayerSettingEXT')),
        'type_name': 'VkLayerSettingEXT',
        'structure': 'VkLayerSettingEXT',
        'length': [['settingCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkInstanceCreateInfo',
}
_extended_by_ = set()
_includes_ = {
    'VkLayerSettingEXT',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
