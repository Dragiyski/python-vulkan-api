import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('pLayerName', ctypes.c_char_p),
        ('pSettingName', ctypes.c_char_p),
        ('type', ctypes.c_int),
        ('valueCount', ctypes.c_uint32),
        ('pValues', ctypes.c_void_p),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkLayerSettingsCreateInfoEXT',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'pLayerName': {'python_name': ['p', 'layer', 'name'], 'len': [['null-terminated']]},
        'pSettingName': {'python_name': ['p', 'setting', 'name'], 'len': [['null-terminated']]},
        'type': {'python_name': ['type'], 'type': 'VkLayerSettingTypeEXT'},
        'valueCount': {'python_name': ['value', 'count']},
        'pValues': {'python_name': ['p', 'values'], 'len': [['valueCount']]},
    }
}
