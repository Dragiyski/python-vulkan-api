import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('count', ctypes.c_uint32),
        ('subdivisionLevel', ctypes.c_uint32),
        ('format', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkAccelerationStructureTrianglesDisplacementMicromapNV',
        'VkAccelerationStructureTrianglesOpacityMicromapEXT',
        'VkMicromapBuildInfoEXT',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'count': {'python_name': ['count']},
        'subdivisionLevel': {'python_name': ['subdivision', 'level']},
        'format': {'python_name': ['format']},
    }
}
