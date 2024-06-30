from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetPhysicalDeviceSurfaceCapabilities2KHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'pSurfaceInfo', 'pSurfaceCapabilities']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pSurfaceInfo': {
        'type': CPointerType(CComplexType('VkPhysicalDeviceSurfaceInfo2KHR')),
        'is_string': False,
    },
    'pSurfaceCapabilities': {
        'type': CPointerType(CComplexType('VkSurfaceCapabilities2KHR')),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_SURFACE_LOST_KHR', 'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
