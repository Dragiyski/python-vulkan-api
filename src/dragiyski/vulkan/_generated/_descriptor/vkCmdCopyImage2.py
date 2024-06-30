from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdCopyImage2'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pCopyImageInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pCopyImageInfo': {
        'type': CPointerType(CComplexType('VkCopyImageInfo2')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
