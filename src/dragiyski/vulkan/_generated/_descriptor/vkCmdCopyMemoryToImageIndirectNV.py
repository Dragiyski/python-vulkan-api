from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdCopyMemoryToImageIndirectNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'copyBufferAddress', 'copyCount', 'stride', 'dstImage', 'dstImageLayout', 'pImageSubresources']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'copyBufferAddress': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'copyCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'stride': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'dstImage': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'dstImageLayout': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
    'pImageSubresources': {
        'type': CPointerType(CComplexType('VkImageSubresourceLayers')),
        'is_string': False,
        'length': [['copyCount']],
    },
}
_return_type_ = CVoidType()
