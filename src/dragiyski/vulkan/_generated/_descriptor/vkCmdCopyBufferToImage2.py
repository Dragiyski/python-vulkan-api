from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdCopyBufferToImage2'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pCopyBufferToImageInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pCopyBufferToImageInfo': {
        'type': CPointerType(CComplexType('VkCopyBufferToImageInfo2')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
