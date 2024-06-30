from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetLineStippleKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'lineStippleFactor', 'lineStipplePattern']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'lineStippleFactor': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'lineStipplePattern': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
