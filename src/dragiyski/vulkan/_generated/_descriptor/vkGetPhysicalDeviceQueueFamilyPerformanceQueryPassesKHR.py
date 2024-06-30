from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetPhysicalDeviceQueueFamilyPerformanceQueryPassesKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'pPerformanceQueryCreateInfo', 'pNumPasses']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pPerformanceQueryCreateInfo': {
        'type': CPointerType(CComplexType('VkQueryPoolPerformanceCreateInfoKHR')),
        'is_string': False,
    },
    'pNumPasses': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
