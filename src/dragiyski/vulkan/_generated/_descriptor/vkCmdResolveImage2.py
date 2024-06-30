from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdResolveImage2'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pResolveImageInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pResolveImageInfo': {
        'type': CPointerType(CComplexType('VkResolveImageInfo2')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
