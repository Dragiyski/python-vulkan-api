import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('inlineUniformBlock', ctypes.c_uint32),
        ('descriptorBindingInlineUniformBlockUpdateAfterBind', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkDeviceCreateInfo',
        'VkPhysicalDeviceFeatures2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_INLINE_UNIFORM_BLOCK_FEATURES', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'inlineUniformBlock': {'python_name': ['inline', 'uniform', 'block']},
        'descriptorBindingInlineUniformBlockUpdateAfterBind': {'python_name': ['descriptor', 'binding', 'inline', 'uniform', 'block', 'update', 'after', 'bind']},
    }
}
