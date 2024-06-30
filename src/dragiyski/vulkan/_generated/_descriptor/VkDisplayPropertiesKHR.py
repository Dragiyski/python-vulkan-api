from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDisplayPropertiesKHR'
_member_list_ = ['display', 'displayName', 'physicalDimensions', 'physicalResolution', 'supportedTransforms', 'planeReorderPossible', 'persistentContent']
_member_info_ = {
    'display': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'displayName': {
        'type': CStringType('c_char_p'),
        'length': [],
        'is_string': True,
    },
    'physicalDimensions': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
    'physicalResolution': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
    'supportedTransforms': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSurfaceTransformFlagsKHR',
        'enum': 'VkSurfaceTransformFlagsKHR',
        'is_string': False,
    },
    'planeReorderPossible': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'persistentContent': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkExtent2D',
}
_included_in_ = {
    'VkDisplayProperties2KHR',
}
_input_of_ = set()
_output_of_ = {
    'vkGetPhysicalDeviceDisplayPropertiesKHR',
}
