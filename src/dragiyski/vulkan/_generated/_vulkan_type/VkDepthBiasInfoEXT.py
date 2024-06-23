import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('depthBiasConstantFactor', ctypes.c_float),
        ('depthBiasClamp', ctypes.c_float),
        ('depthBiasSlopeFactor', ctypes.c_float),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkDepthBiasRepresentationInfoEXT',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCmdSetDepthBias2EXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DEPTH_BIAS_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'depthBiasConstantFactor': {'python_name': ['depth', 'bias', 'constant', 'factor']},
        'depthBiasClamp': {'python_name': ['depth', 'bias', 'clamp']},
        'depthBiasSlopeFactor': {'python_name': ['depth', 'bias', 'slope', 'factor']},
    }
}
