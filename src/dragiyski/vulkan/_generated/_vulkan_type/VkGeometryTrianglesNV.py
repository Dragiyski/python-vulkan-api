import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('vertexData', ctypes.c_void_p),
        ('vertexOffset', ctypes.c_uint64),
        ('vertexCount', ctypes.c_uint32),
        ('vertexStride', ctypes.c_uint64),
        ('vertexFormat', ctypes.c_int),
        ('indexData', ctypes.c_void_p),
        ('indexOffset', ctypes.c_uint64),
        ('indexCount', ctypes.c_uint32),
        ('indexType', ctypes.c_int),
        ('transformData', ctypes.c_void_p),
        ('transformOffset', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkGeometryDataNV',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_GEOMETRY_TRIANGLES_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'vertexData': {'python_name': ['vertex', 'data']},
        'vertexOffset': {'python_name': ['vertex', 'offset']},
        'vertexCount': {'python_name': ['vertex', 'count']},
        'vertexStride': {'python_name': ['vertex', 'stride']},
        'vertexFormat': {'python_name': ['vertex', 'format'], 'type': 'VkFormat'},
        'indexData': {'python_name': ['index', 'data']},
        'indexOffset': {'python_name': ['index', 'offset']},
        'indexCount': {'python_name': ['index', 'count']},
        'indexType': {'python_name': ['index', 'type'], 'type': 'VkIndexType'},
        'transformData': {'python_name': ['transform', 'data']},
        'transformOffset': {'python_name': ['transform', 'offset']},
    }
}
