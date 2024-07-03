from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkEnumerateInstanceVersion'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['pApiVersion']
_argument_info_ = {
    'pApiVersion': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY'}
