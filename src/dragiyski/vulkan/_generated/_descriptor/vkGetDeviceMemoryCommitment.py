from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetDeviceMemoryCommitment'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'memory', 'pCommittedMemoryInBytes']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'memory': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pCommittedMemoryInBytes': {
        'type': CPointerType(CIntType('c_uint64')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CVoidType()
