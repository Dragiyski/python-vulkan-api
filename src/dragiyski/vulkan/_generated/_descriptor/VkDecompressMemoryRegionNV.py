from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDecompressMemoryRegionNV'
_member_list_ = ['srcAddress', 'dstAddress', 'compressedSize', 'decompressedSize', 'decompressionMethod']
_member_info_ = {
    'srcAddress': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'dstAddress': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'compressedSize': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'decompressedSize': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'decompressionMethod': {
        'type': CIntType('c_uint64'),
        'type_name': 'VkMemoryDecompressionMethodFlagsNV',
        'enum': 'VkMemoryDecompressionMethodFlagsNV',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCmdDecompressMemoryNV',
}
_output_of_ = set()
