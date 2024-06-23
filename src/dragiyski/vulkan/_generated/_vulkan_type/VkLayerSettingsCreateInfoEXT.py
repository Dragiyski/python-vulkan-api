import ctypes

class CType(ctypes.Structure):
    pass

from .VkLayerSettingEXT import CType as VkLayerSettingEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('settingCount', ctypes.c_uint32),
    ('pSettings', ctypes.POINTER(VkLayerSettingEXT)),
]

descriptor = {
    'extends': {
        'VkInstanceCreateInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkLayerSettingEXT',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_LAYER_SETTINGS_CREATE_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'settingCount': {'python_name': ['setting', 'count']},
        'pSettings': {'python_name': ['p', 'settings'], 'len': [['settingCount']], 'type': 'VkLayerSettingEXT'},
    }
}
