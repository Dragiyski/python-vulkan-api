from ..._ctypes import *

_category_ = 'callback'
_name_ = 'vkDebugUtilsMessengerCallbackEXT'
_constructor_ = 'VKAPI_PTR'
_argument_list_ = ['messageSeverity', 'messageTypes', 'pCallbackData', 'pUserData']
_argument_info_ = {
    'messageSeverity': {
        'type': CIntType('c_uint32'),
    },
    'messageTypes': {
        'type': CIntType('c_uint32'),
    },
    'pCallbackData': {
        'type': CPointerType(CComplexType('VkDebugUtilsMessengerCallbackDataEXT')),
    },
    'pUserData': {
        'type': CIntType('c_void_p'),
    },
}
_return_type_ = CIntType('c_uint32')
