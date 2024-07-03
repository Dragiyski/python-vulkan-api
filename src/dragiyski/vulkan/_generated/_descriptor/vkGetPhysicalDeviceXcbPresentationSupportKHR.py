from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetPhysicalDeviceXcbPresentationSupportKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'queueFamilyIndex', 'connection', 'visual_id']
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
    'connection': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'visual_id': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CIntType('c_uint32')
