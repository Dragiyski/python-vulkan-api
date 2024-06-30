from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdTraceRaysIndirect2KHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'indirectDeviceAddress']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'indirectDeviceAddress': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
