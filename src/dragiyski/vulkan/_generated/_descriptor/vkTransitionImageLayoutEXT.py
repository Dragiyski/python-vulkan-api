from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkTransitionImageLayoutEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'transitionCount', 'pTransitions']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'transitionCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pTransitions': {
        'type': CPointerType(CComplexType('VkHostImageLayoutTransitionInfoEXT')),
        'is_string': False,
        'length': [['transitionCount']],
        'output': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_MEMORY_MAP_FAILED', 'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_INITIALIZATION_FAILED'}
