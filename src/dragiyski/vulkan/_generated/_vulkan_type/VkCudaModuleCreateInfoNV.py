import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('dataSize', ctypes.c_size_t),
        ('pData', ctypes.c_void_p),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCreateCudaModuleNV',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_CUDA_MODULE_CREATE_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'dataSize': {'python_name': ['data', 'size']},
        'pData': {'python_name': ['p', 'data'], 'len': [['dataSize']]},
    }
}
