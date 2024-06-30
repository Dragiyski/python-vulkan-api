from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkTilePropertiesQCOM'
_member_list_ = ['sType', 'pNext', 'tileSize', 'apronSize', 'origin']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_TILE_PROPERTIES_QCOM',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'tileSize': {
        'type': CComplexType('VkExtent3D'),
        'type_name': 'VkExtent3D',
        'structure': 'VkExtent3D',
        'is_string': False,
    },
    'apronSize': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
    'origin': {
        'type': CComplexType('VkOffset2D'),
        'type_name': 'VkOffset2D',
        'structure': 'VkOffset2D',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkExtent2D',
    'VkExtent3D',
    'VkOffset2D',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetDynamicRenderingTilePropertiesQCOM',
    'vkGetFramebufferTilePropertiesQCOM',
}
