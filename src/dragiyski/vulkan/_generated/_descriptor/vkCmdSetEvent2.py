from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdSetEvent2'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'event', 'pDependencyInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'event': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pDependencyInfo': {
        'type': CPointerType(CComplexType('VkDependencyInfo')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
