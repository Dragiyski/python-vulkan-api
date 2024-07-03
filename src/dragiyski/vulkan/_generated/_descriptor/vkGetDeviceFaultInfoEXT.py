from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetDeviceFaultInfoEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pFaultCounts', 'pFaultInfo']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pFaultCounts': {
        'type': CPointerType(CComplexType('VkDeviceFaultCountsEXT')),
        'is_string': False,
        'output': True,
    },
    'pFaultInfo': {
        'type': CPointerType(CComplexType('VkDeviceFaultInfoEXT')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_INCOMPLETE'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY'}
