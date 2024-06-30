from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkUnmapMemory2KHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pMemoryUnmapInfo']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pMemoryUnmapInfo': {
        'type': CPointerType(CComplexType('VkMemoryUnmapInfoKHR')),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_MEMORY_MAP_FAILED'}
