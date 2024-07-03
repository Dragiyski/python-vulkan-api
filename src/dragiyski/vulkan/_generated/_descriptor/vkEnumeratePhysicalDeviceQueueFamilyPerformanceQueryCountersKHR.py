from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkEnumeratePhysicalDeviceQueueFamilyPerformanceQueryCountersKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'queueFamilyIndex', 'pCounterCount', 'pCounters', 'pCounterDescriptions']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'queueFamilyIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pCounterCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'output': True,
    },
    'pCounters': {
        'type': CPointerType(CComplexType('VkPerformanceCounterKHR')),
        'is_string': False,
        'length': [['pCounterCount']],
        'output': True,
    },
    'pCounterDescriptions': {
        'type': CPointerType(CComplexType('VkPerformanceCounterDescriptionKHR')),
        'is_string': False,
        'length': [['pCounterCount']],
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_INCOMPLETE'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_INITIALIZATION_FAILED'}
