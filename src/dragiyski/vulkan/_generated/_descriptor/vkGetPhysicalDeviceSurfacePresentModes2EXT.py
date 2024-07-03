from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetPhysicalDeviceSurfacePresentModes2EXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'pSurfaceInfo', 'pPresentModeCount', 'pPresentModes']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pSurfaceInfo': {
        'type': CPointerType(CComplexType('VkPhysicalDeviceSurfaceInfo2KHR')),
        'is_string': False,
        'output': False,
    },
    'pPresentModeCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'output': True,
    },
    'pPresentModes': {
        'type': CPointerType(CIntType('c_int')),
        'is_string': False,
        'length': [['pPresentModeCount']],
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_INCOMPLETE'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_SURFACE_LOST_KHR', 'VK_ERROR_OUT_OF_DEVICE_MEMORY'}
