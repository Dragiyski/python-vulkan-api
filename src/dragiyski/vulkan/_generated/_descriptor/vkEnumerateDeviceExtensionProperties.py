from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkEnumerateDeviceExtensionProperties'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'pLayerName', 'pPropertyCount', 'pProperties']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pLayerName': {
        'type': CStringType('c_char_p'),
        'is_string': True,
        'length': [],
    },
    'pPropertyCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
    },
    'pProperties': {
        'type': CPointerType(CComplexType('VkExtensionProperties')),
        'is_string': False,
        'length': [['pPropertyCount']],
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_INCOMPLETE'}
_error_code_list_ = {'VK_ERROR_LAYER_NOT_PRESENT', 'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
