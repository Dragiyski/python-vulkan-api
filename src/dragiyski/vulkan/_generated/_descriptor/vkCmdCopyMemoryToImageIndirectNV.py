from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdCopyMemoryToImageIndirectNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'copyBufferAddress', 'copyCount', 'stride', 'dstImage', 'dstImageLayout', 'pImageSubresources']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'copyBufferAddress': {
        'type': CIntType('c_uint64'),
        'is_string': False,
        'output': False,
    },
    'copyCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'stride': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'dstImage': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'dstImageLayout': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
    'pImageSubresources': {
        'type': CPointerType(CComplexType('VkImageSubresourceLayers')),
        'is_string': False,
        'length': [['copyCount']],
        'output': False,
    },
}
_return_type_ = CVoidType()
