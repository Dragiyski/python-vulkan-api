import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('raygenShaderRecordAddress', ctypes.c_uint64),
        ('raygenShaderRecordSize', ctypes.c_uint64),
        ('missShaderBindingTableAddress', ctypes.c_uint64),
        ('missShaderBindingTableSize', ctypes.c_uint64),
        ('missShaderBindingTableStride', ctypes.c_uint64),
        ('hitShaderBindingTableAddress', ctypes.c_uint64),
        ('hitShaderBindingTableSize', ctypes.c_uint64),
        ('hitShaderBindingTableStride', ctypes.c_uint64),
        ('callableShaderBindingTableAddress', ctypes.c_uint64),
        ('callableShaderBindingTableSize', ctypes.c_uint64),
        ('callableShaderBindingTableStride', ctypes.c_uint64),
        ('width', ctypes.c_uint32),
        ('height', ctypes.c_uint32),
        ('depth', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'raygenShaderRecordAddress': {'python_name': ['raygen', 'shader', 'record', 'address']},
        'raygenShaderRecordSize': {'python_name': ['raygen', 'shader', 'record', 'size']},
        'missShaderBindingTableAddress': {'python_name': ['miss', 'shader', 'binding', 'table', 'address']},
        'missShaderBindingTableSize': {'python_name': ['miss', 'shader', 'binding', 'table', 'size']},
        'missShaderBindingTableStride': {'python_name': ['miss', 'shader', 'binding', 'table', 'stride']},
        'hitShaderBindingTableAddress': {'python_name': ['hit', 'shader', 'binding', 'table', 'address']},
        'hitShaderBindingTableSize': {'python_name': ['hit', 'shader', 'binding', 'table', 'size']},
        'hitShaderBindingTableStride': {'python_name': ['hit', 'shader', 'binding', 'table', 'stride']},
        'callableShaderBindingTableAddress': {'python_name': ['callable', 'shader', 'binding', 'table', 'address']},
        'callableShaderBindingTableSize': {'python_name': ['callable', 'shader', 'binding', 'table', 'size']},
        'callableShaderBindingTableStride': {'python_name': ['callable', 'shader', 'binding', 'table', 'stride']},
        'width': {'python_name': ['width']},
        'height': {'python_name': ['height']},
        'depth': {'python_name': ['depth']},
    }
}
