from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkQueueNotifyOutOfBandNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['queue', 'pQueueTypeInfo']
_argument_info_ = {
    'queue': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pQueueTypeInfo': {
        'type': CPointerType(CComplexType('VkOutOfBandQueueTypeInfoNV')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
