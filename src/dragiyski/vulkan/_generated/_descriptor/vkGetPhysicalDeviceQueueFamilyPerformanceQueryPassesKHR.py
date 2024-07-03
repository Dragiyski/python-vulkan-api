from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetPhysicalDeviceQueueFamilyPerformanceQueryPassesKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'pPerformanceQueryCreateInfo', 'pNumPasses']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pPerformanceQueryCreateInfo': {
        'type': CPointerType(CComplexType('VkQueryPoolPerformanceCreateInfoKHR')),
        'is_string': False,
        'output': False,
    },
    'pNumPasses': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CVoidType()
