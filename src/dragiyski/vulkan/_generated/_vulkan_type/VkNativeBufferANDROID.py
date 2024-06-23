import ctypes

class CType(ctypes.Structure):
    pass

from .VkNativeBufferUsage2ANDROID import CType as VkNativeBufferUsage2ANDROID

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('handle', ctypes.c_void_p),
    ('stride', ctypes.c_int),
    ('format', ctypes.c_int),
    ('usage', ctypes.c_int),
    ('usage2', VkNativeBufferUsage2ANDROID),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkNativeBufferUsage2ANDROID',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_NATIVE_BUFFER_ANDROID', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'handle': {'python_name': ['handle']},
        'stride': {'python_name': ['stride']},
        'format': {'python_name': ['format']},
        'usage': {'python_name': ['usage']},
        'usage2': {'python_name': ['usage2'], 'type': 'VkNativeBufferUsage2ANDROID'},
    }
}
