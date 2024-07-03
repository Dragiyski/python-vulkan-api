from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetLatencyTimingsNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'swapchain', 'pLatencyMarkerInfo']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'swapchain': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pLatencyMarkerInfo': {
        'type': CPointerType(CComplexType('VkGetLatencyMarkerInfoNV')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CVoidType()
