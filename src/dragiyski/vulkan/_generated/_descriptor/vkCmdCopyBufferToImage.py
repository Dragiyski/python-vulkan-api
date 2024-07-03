from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdCopyBufferToImage'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'srcBuffer', 'dstImage', 'dstImageLayout', 'regionCount', 'pRegions']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'srcBuffer': {
        'type': CIntType('c_void_p'),
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
    'regionCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pRegions': {
        'type': CPointerType(CComplexType('VkBufferImageCopy')),
        'is_string': False,
        'length': [['regionCount']],
        'output': False,
    },
}
_return_type_ = CVoidType()
