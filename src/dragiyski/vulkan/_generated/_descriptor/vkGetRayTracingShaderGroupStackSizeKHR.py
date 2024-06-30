from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetRayTracingShaderGroupStackSizeKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pipeline', 'group', 'groupShader']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pipeline': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'group': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'groupShader': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_uint64')
