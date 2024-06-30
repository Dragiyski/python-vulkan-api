from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkQueueBeginDebugUtilsLabelEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['queue', 'pLabelInfo']
_argument_info_ = {
    'queue': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pLabelInfo': {
        'type': CPointerType(CComplexType('VkDebugUtilsLabelEXT')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
