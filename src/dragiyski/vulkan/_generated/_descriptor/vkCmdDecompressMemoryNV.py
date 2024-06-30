from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdDecompressMemoryNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'decompressRegionCount', 'pDecompressMemoryRegions']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'decompressRegionCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pDecompressMemoryRegions': {
        'type': CPointerType(CComplexType('VkDecompressMemoryRegionNV')),
        'is_string': False,
        'length': [['decompressRegionCount']],
    },
}
_return_type_ = CVoidType()
