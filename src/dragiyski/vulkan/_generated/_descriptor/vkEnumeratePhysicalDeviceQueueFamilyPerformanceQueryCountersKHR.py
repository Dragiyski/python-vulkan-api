from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkEnumeratePhysicalDeviceQueueFamilyPerformanceQueryCountersKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'queueFamilyIndex', 'pCounterCount', 'pCounters', 'pCounterDescriptions']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'queueFamilyIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pCounterCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
    },
    'pCounters': {
        'type': CPointerType(CComplexType('VkPerformanceCounterKHR')),
        'is_string': False,
        'length': [['pCounterCount']],
    },
    'pCounterDescriptions': {
        'type': CPointerType(CComplexType('VkPerformanceCounterDescriptionKHR')),
        'is_string': False,
        'length': [['pCounterCount']],
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_INCOMPLETE'}
_error_code_list_ = {'VK_ERROR_INITIALIZATION_FAILED', 'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
