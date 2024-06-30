from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkEnumeratePhysicalDeviceGroups'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['instance', 'pPhysicalDeviceGroupCount', 'pPhysicalDeviceGroupProperties']
_argument_info_ = {
    'instance': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pPhysicalDeviceGroupCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
    },
    'pPhysicalDeviceGroupProperties': {
        'type': CPointerType(CComplexType('VkPhysicalDeviceGroupProperties')),
        'is_string': False,
        'length': [['pPhysicalDeviceGroupCount']],
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_INCOMPLETE'}
_error_code_list_ = {'VK_ERROR_INITIALIZATION_FAILED', 'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
