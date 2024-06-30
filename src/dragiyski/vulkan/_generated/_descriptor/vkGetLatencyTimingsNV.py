from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetLatencyTimingsNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'swapchain', 'pLatencyMarkerInfo']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'swapchain': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pLatencyMarkerInfo': {
        'type': CPointerType(CComplexType('VkGetLatencyMarkerInfoNV')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
