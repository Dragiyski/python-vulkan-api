from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkBuildMicromapsEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'deferredOperation', 'infoCount', 'pInfos']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'deferredOperation': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'infoCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pInfos': {
        'type': CPointerType(CComplexType('VkMicromapBuildInfoEXT')),
        'is_string': False,
        'length': [['infoCount']],
        'output': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_OPERATION_NOT_DEFERRED_KHR', 'VK_SUCCESS', 'VK_OPERATION_DEFERRED_KHR'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_OUT_OF_DEVICE_MEMORY'}
