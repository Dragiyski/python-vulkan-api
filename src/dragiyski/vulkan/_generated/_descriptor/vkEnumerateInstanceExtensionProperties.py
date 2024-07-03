from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkEnumerateInstanceExtensionProperties'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['pLayerName', 'pPropertyCount', 'pProperties']
_argument_info_ = {
    'pLayerName': {
        'type': CStringType('c_char_p'),
        'is_string': True,
        'length': [],
        'output': False,
    },
    'pPropertyCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'output': True,
    },
    'pProperties': {
        'type': CPointerType(CComplexType('VkExtensionProperties')),
        'is_string': False,
        'length': [['pPropertyCount']],
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_INCOMPLETE'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_LAYER_NOT_PRESENT'}
