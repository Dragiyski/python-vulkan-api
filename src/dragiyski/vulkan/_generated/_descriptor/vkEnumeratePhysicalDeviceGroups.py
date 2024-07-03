from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkEnumeratePhysicalDeviceGroups'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['instance', 'pPhysicalDeviceGroupCount', 'pPhysicalDeviceGroupProperties']
_argument_info_ = {
    'instance': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pPhysicalDeviceGroupCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'output': True,
    },
    'pPhysicalDeviceGroupProperties': {
        'type': CPointerType(CComplexType('VkPhysicalDeviceGroupProperties')),
        'is_string': False,
        'length': [['pPhysicalDeviceGroupCount']],
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_INCOMPLETE'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_INITIALIZATION_FAILED'}
