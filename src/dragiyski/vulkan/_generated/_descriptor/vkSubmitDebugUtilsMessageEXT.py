from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkSubmitDebugUtilsMessageEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['instance', 'messageSeverity', 'messageTypes', 'pCallbackData']
_argument_info_ = {
    'instance': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'messageSeverity': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'messageTypes': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pCallbackData': {
        'type': CPointerType(CComplexType('VkDebugUtilsMessengerCallbackDataEXT')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
