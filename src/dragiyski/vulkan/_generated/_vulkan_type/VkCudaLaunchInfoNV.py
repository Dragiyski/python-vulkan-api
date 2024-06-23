import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('function', ctypes.c_void_p),
        ('gridDimX', ctypes.c_uint32),
        ('gridDimY', ctypes.c_uint32),
        ('gridDimZ', ctypes.c_uint32),
        ('blockDimX', ctypes.c_uint32),
        ('blockDimY', ctypes.c_uint32),
        ('blockDimZ', ctypes.c_uint32),
        ('sharedMemBytes', ctypes.c_uint32),
        ('paramCount', ctypes.c_size_t),
        ('pParams', ctypes.POINTER(ctypes.c_void_p)),
        ('extraCount', ctypes.c_size_t),
        ('pExtras', ctypes.POINTER(ctypes.c_void_p)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCmdCudaLaunchKernelNV',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_CUDA_LAUNCH_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'function': {'python_name': ['function']},
        'gridDimX': {'python_name': ['grid', 'dim', 'x']},
        'gridDimY': {'python_name': ['grid', 'dim', 'y']},
        'gridDimZ': {'python_name': ['grid', 'dim', 'z']},
        'blockDimX': {'python_name': ['block', 'dim', 'x']},
        'blockDimY': {'python_name': ['block', 'dim', 'y']},
        'blockDimZ': {'python_name': ['block', 'dim', 'z']},
        'sharedMemBytes': {'python_name': ['shared', 'mem', 'bytes']},
        'paramCount': {'python_name': ['param', 'count']},
        'pParams': {'python_name': ['p', 'params'], 'len': [['paramCount']]},
        'extraCount': {'python_name': ['extra', 'count']},
        'pExtras': {'python_name': ['p', 'extras'], 'len': [['extraCount']]},
    }
}
