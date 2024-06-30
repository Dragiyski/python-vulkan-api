from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetPhysicalDeviceRefreshableObjectTypesKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'pRefreshableObjectTypeCount', 'pRefreshableObjectTypes']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pRefreshableObjectTypeCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
    },
    'pRefreshableObjectTypes': {
        'type': CPointerType(CIntType('c_int')),
        'is_string': False,
        'length': [['pRefreshableObjectTypeCount']],
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_INCOMPLETE'}
_error_code_list_ = set()
