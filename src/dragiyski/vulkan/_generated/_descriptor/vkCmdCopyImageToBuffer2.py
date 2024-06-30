from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdCopyImageToBuffer2'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pCopyImageToBufferInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pCopyImageToBufferInfo': {
        'type': CPointerType(CComplexType('VkCopyImageToBufferInfo2')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
