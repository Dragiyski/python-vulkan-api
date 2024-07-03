from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetPhysicalDeviceFragmentShadingRatesKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'pFragmentShadingRateCount', 'pFragmentShadingRates']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pFragmentShadingRateCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'output': True,
    },
    'pFragmentShadingRates': {
        'type': CPointerType(CComplexType('VkPhysicalDeviceFragmentShadingRateKHR')),
        'is_string': False,
        'length': [['pFragmentShadingRateCount']],
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_INCOMPLETE'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY'}
