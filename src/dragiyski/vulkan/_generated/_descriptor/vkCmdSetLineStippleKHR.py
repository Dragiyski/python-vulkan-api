from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdSetLineStippleKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'lineStippleFactor', 'lineStipplePattern']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'lineStippleFactor': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'lineStipplePattern': {
        'type': CIntType('c_uint16'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
