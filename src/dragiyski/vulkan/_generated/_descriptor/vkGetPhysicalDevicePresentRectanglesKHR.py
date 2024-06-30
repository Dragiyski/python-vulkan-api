from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetPhysicalDevicePresentRectanglesKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'surface', 'pRectCount', 'pRects']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'surface': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pRectCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
    },
    'pRects': {
        'type': CPointerType(CComplexType('VkRect2D')),
        'is_string': False,
        'length': [['pRectCount']],
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_INCOMPLETE'}
_error_code_list_ = {'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
