from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkQueueFamilyProperties'
_member_list_ = ['queueFlags', 'queueCount', 'timestampValidBits', 'minImageTransferGranularity']
_member_info_ = {
    'queueFlags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkQueueFlags',
        'enum': 'VkQueueFlags',
        'is_string': False,
    },
    'queueCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'timestampValidBits': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'minImageTransferGranularity': {
        'type': CComplexType('VkExtent3D'),
        'type_name': 'VkExtent3D',
        'structure': 'VkExtent3D',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkExtent3D',
}
_included_in_ = {
    'VkQueueFamilyProperties2',
}
_input_of_ = set()
_output_of_ = {
    'vkGetPhysicalDeviceQueueFamilyProperties',
}
