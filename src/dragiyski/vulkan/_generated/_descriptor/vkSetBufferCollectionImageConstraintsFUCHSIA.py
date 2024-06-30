from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkSetBufferCollectionImageConstraintsFUCHSIA'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'collection', 'pImageConstraintsInfo']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'collection': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pImageConstraintsInfo': {
        'type': CPointerType(CComplexType('VkImageConstraintsInfoFUCHSIA')),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_INITIALIZATION_FAILED', 'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_FORMAT_NOT_SUPPORTED'}
