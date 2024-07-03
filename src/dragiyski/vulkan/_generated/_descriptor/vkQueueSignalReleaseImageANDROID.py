from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkQueueSignalReleaseImageANDROID'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['queue', 'waitSemaphoreCount', 'pWaitSemaphores', 'image', 'pNativeFenceFd']
_argument_info_ = {
    'queue': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'waitSemaphoreCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pWaitSemaphores': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'length': [['waitSemaphoreCount']],
        'output': False,
    },
    'image': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pNativeFenceFd': {
        'type': CPointerType(CIntType('c_int')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = set()
_error_code_list_ = set()
