from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetPhysicalDeviceXlibPresentationSupportKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'queueFamilyIndex', 'dpy', 'visualID']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'queueFamilyIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'dpy': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'visualID': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_uint32')
