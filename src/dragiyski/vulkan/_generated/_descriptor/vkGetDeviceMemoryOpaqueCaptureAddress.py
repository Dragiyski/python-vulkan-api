from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetDeviceMemoryOpaqueCaptureAddress'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pInfo']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pInfo': {
        'type': CPointerType(CComplexType('VkDeviceMemoryOpaqueCaptureAddressInfo')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CIntType('c_uint64')
