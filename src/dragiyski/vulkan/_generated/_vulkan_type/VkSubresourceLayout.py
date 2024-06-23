import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('offset', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
        ('rowPitch', ctypes.c_uint64),
        ('arrayPitch', ctypes.c_uint64),
        ('depthPitch', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkImageDrmFormatModifierExplicitCreateInfoEXT',
        'VkSubresourceLayout2KHR',
    },
    'input_of': set(),
    'output_of': {
        'vkGetImageSubresourceLayout',
    },
    'member_map': {
        'offset': {'python_name': ['offset']},
        'size': {'python_name': ['size']},
        'rowPitch': {'python_name': ['row', 'pitch']},
        'arrayPitch': {'python_name': ['array', 'pitch']},
        'depthPitch': {'python_name': ['depth', 'pitch']},
    }
}
