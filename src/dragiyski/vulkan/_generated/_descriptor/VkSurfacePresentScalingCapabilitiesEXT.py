from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSurfacePresentScalingCapabilitiesEXT'
_member_list_ = ['sType', 'pNext', 'supportedPresentScaling', 'supportedPresentGravityX', 'supportedPresentGravityY', 'minScaledImageExtent', 'maxScaledImageExtent']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SURFACE_PRESENT_SCALING_CAPABILITIES_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'supportedPresentScaling': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkPresentScalingFlagsEXT',
        'enum': 'VkPresentScalingFlagsEXT',
        'is_string': False,
    },
    'supportedPresentGravityX': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkPresentGravityFlagsEXT',
        'enum': 'VkPresentGravityFlagsEXT',
        'is_string': False,
    },
    'supportedPresentGravityY': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkPresentGravityFlagsEXT',
        'enum': 'VkPresentGravityFlagsEXT',
        'is_string': False,
    },
    'minScaledImageExtent': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
    'maxScaledImageExtent': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
}
_extends_ = {
    'VkSurfaceCapabilities2KHR',
}
_extended_by_ = set()
_includes_ = {
    'VkExtent2D',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
