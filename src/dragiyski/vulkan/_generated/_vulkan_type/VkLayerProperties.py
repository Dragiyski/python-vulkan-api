import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('layerName', ctypes.ARRAY(ctypes.c_char, 256)),
        ('specVersion', ctypes.c_uint32),
        ('implementationVersion', ctypes.c_uint32),
        ('description', ctypes.ARRAY(ctypes.c_char, 256)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkEnumerateDeviceLayerProperties',
        'vkEnumerateInstanceLayerProperties',
    },
    'member_map': {
        'layerName': {'python_name': ['layer', 'name'], 'len': [['null-terminated']]},
        'specVersion': {'python_name': ['spec', 'version']},
        'implementationVersion': {'python_name': ['implementation', 'version']},
        'description': {'python_name': ['description'], 'len': [['null-terminated']]},
    }
}
