import ctypes

class VkDecompressMemoryRegionNV(ctypes.Structure):
    _fields_ = [
        ('srcAddress', ctypes.c_uint64),
        ('dstAddress', ctypes.c_uint64),
        ('compressedSize', ctypes.c_uint64),
        ('decompressedSize', ctypes.c_uint64),
        ('decompressionMethod', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCmdDecompressMemoryNV',
    }
    _output_of_ = set()
    _python_name_ = {
        'srcAddress': 'src_address',
        'dstAddress': 'dst_address',
        'compressedSize': 'compressed_size',
        'decompressedSize': 'decompressed_size',
        'decompressionMethod': 'decompression_method',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_memory_decompression',
    }
    _vk_enum_ = {
        'decompressionMethod': 'VkMemoryDecompressionMethodFlagsNV',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkDecompressMemoryRegionNV._type_ = {
    'srcAddress': ctypes.c_uint64,
    'dstAddress': ctypes.c_uint64,
    'compressedSize': ctypes.c_uint64,
    'decompressedSize': ctypes.c_uint64,
    'decompressionMethod': ctypes.c_uint64,
}
