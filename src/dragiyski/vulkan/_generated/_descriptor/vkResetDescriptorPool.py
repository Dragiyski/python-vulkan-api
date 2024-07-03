from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkResetDescriptorPool'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'descriptorPool', 'flags']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'descriptorPool': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = set()
