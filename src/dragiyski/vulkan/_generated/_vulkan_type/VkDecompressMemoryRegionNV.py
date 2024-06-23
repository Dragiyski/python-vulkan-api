import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('srcAddress', ctypes.c_uint64),
        ('dstAddress', ctypes.c_uint64),
        ('compressedSize', ctypes.c_uint64),
        ('decompressedSize', ctypes.c_uint64),
        ('decompressionMethod', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCmdDecompressMemoryNV',
    },
    'output_of': set(),
    'member_map': {
        'srcAddress': {'python_name': ['src', 'address']},
        'dstAddress': {'python_name': ['dst', 'address']},
        'compressedSize': {'python_name': ['compressed', 'size']},
        'decompressedSize': {'python_name': ['decompressed', 'size']},
        'decompressionMethod': {'python_name': ['decompression', 'method'], 'type': 'VkMemoryDecompressionMethodFlagsNV'},
    }
}
