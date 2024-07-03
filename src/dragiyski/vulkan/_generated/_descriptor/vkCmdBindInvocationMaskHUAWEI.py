from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdBindInvocationMaskHUAWEI'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'imageView', 'imageLayout']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'imageView': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'imageLayout': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
