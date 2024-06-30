from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDisplayPlanePropertiesKHR'
_member_list_ = ['currentDisplay', 'currentStackIndex']
_member_info_ = {
    'currentDisplay': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'currentStackIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkDisplayPlaneProperties2KHR',
}
_input_of_ = set()
_output_of_ = {
    'vkGetPhysicalDeviceDisplayPlanePropertiesKHR',
}
