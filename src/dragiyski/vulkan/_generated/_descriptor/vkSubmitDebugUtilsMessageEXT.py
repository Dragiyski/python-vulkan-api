from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkSubmitDebugUtilsMessageEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['instance', 'messageSeverity', 'messageTypes', 'pCallbackData']
_argument_info_ = {
    'instance': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'messageSeverity': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'messageTypes': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pCallbackData': {
        'type': CPointerType(CComplexType('VkDebugUtilsMessengerCallbackDataEXT')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
