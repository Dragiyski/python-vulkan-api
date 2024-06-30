from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetPhysicalDeviceWaylandPresentationSupportKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'queueFamilyIndex', 'display']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'queueFamilyIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'display': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_uint32')
