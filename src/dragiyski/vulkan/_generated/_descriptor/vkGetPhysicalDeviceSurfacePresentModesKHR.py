from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetPhysicalDeviceSurfacePresentModesKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'surface', 'pPresentModeCount', 'pPresentModes']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'surface': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pPresentModeCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
    },
    'pPresentModes': {
        'type': CPointerType(CIntType('c_int')),
        'is_string': False,
        'length': [['pPresentModeCount']],
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_INCOMPLETE'}
_error_code_list_ = {'VK_ERROR_SURFACE_LOST_KHR', 'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
