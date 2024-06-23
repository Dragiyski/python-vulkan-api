import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderTileImageCoherentReadAccelerated', ctypes.c_uint32),
        ('shaderTileImageReadSampleFromPixelRateInvocation', ctypes.c_uint32),
        ('shaderTileImageReadFromHelperInvocation', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkPhysicalDeviceProperties2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_TILE_IMAGE_PROPERTIES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'shaderTileImageCoherentReadAccelerated': {'python_name': ['shader', 'tile', 'image', 'coherent', 'read', 'accelerated']},
        'shaderTileImageReadSampleFromPixelRateInvocation': {'python_name': ['shader', 'tile', 'image', 'read', 'sample', 'from', 'pixel', 'rate', 'invocation']},
        'shaderTileImageReadFromHelperInvocation': {'python_name': ['shader', 'tile', 'image', 'read', 'from', 'helper', 'invocation']},
    }
}
