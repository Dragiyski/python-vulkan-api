from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetEvent2'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'event', 'pDependencyInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'event': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pDependencyInfo': {
        'type': CPointerType(CComplexType('VkDependencyInfo')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
