from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkEnumeratePhysicalDevices'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['instance', 'pPhysicalDeviceCount', 'pPhysicalDevices']
_argument_info_ = {
    'instance': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pPhysicalDeviceCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
    },
    'pPhysicalDevices': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'length': [['pPhysicalDeviceCount']],
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_INCOMPLETE'}
_error_code_list_ = {'VK_ERROR_INITIALIZATION_FAILED', 'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
