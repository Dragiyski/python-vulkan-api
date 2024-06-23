import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderTileImageColorReadAccess', ctypes.c_uint32),
        ('shaderTileImageDepthReadAccess', ctypes.c_uint32),
        ('shaderTileImageStencilReadAccess', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_TILE_IMAGE_FEATURES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'shaderTileImageColorReadAccess': {'python_name': ['shader', 'tile', 'image', 'color', 'read', 'access']},
        'shaderTileImageDepthReadAccess': {'python_name': ['shader', 'tile', 'image', 'depth', 'read', 'access']},
        'shaderTileImageStencilReadAccess': {'python_name': ['shader', 'tile', 'image', 'stencil', 'read', 'access']},
    }
}
