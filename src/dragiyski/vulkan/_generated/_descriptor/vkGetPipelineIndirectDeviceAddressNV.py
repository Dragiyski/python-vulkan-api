from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetPipelineIndirectDeviceAddressNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pInfo']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pInfo': {
        'type': CPointerType(CComplexType('VkPipelineIndirectDeviceAddressInfoNV')),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_uint64')
