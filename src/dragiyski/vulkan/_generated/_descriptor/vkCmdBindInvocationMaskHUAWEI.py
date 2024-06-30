from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdBindInvocationMaskHUAWEI'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'imageView', 'imageLayout']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'imageView': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'imageLayout': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
