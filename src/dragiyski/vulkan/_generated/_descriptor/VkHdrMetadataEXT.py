from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkHdrMetadataEXT'
_member_list_ = ['sType', 'pNext', 'displayPrimaryRed', 'displayPrimaryGreen', 'displayPrimaryBlue', 'whitePoint', 'maxLuminance', 'minLuminance', 'maxContentLightLevel', 'maxFrameAverageLightLevel']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_HDR_METADATA_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'displayPrimaryRed': {
        'type': CComplexType('VkXYColorEXT'),
        'type_name': 'VkXYColorEXT',
        'structure': 'VkXYColorEXT',
        'is_string': False,
    },
    'displayPrimaryGreen': {
        'type': CComplexType('VkXYColorEXT'),
        'type_name': 'VkXYColorEXT',
        'structure': 'VkXYColorEXT',
        'is_string': False,
    },
    'displayPrimaryBlue': {
        'type': CComplexType('VkXYColorEXT'),
        'type_name': 'VkXYColorEXT',
        'structure': 'VkXYColorEXT',
        'is_string': False,
    },
    'whitePoint': {
        'type': CComplexType('VkXYColorEXT'),
        'type_name': 'VkXYColorEXT',
        'structure': 'VkXYColorEXT',
        'is_string': False,
    },
    'maxLuminance': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'minLuminance': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'maxContentLightLevel': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'maxFrameAverageLightLevel': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkXYColorEXT',
}
_included_in_ = set()
_input_of_ = {
    'vkSetHdrMetadataEXT',
}
_output_of_ = set()
