import ctypes

class CType(ctypes.Union):
    _fields_ = [
        ('float32', ctypes.ARRAY(ctypes.c_float, 4)),
        ('int32', ctypes.ARRAY(ctypes.c_int32, 4)),
        ('uint32', ctypes.ARRAY(ctypes.c_uint32, 4)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkClearValue',
        'VkSamplerCustomBorderColorCreateInfoEXT',
    },
    'input_of': {
        'vkCmdClearColorImage',
    },
    'output_of': set(),
    'member_map': {
        'float32': {'python_name': ['float32']},
        'int32': {'python_name': ['int32']},
        'uint32': {'python_name': ['uint32']},
    }
}
