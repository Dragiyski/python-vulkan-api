from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdResolveImage2'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pResolveImageInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pResolveImageInfo': {
        'type': CPointerType(CComplexType('VkResolveImageInfo2')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
