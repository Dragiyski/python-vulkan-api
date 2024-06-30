from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetRenderingAreaGranularityKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pRenderingAreaInfo', 'pGranularity']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pRenderingAreaInfo': {
        'type': CPointerType(CComplexType('VkRenderingAreaInfoKHR')),
        'is_string': False,
    },
    'pGranularity': {
        'type': CPointerType(CComplexType('VkExtent2D')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
