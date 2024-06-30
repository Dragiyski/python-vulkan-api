from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkFormatProperties2'
_member_list_ = ['sType', 'pNext', 'formatProperties']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_FORMAT_PROPERTIES_2',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'formatProperties': {
        'type': CComplexType('VkFormatProperties'),
        'type_name': 'VkFormatProperties',
        'structure': 'VkFormatProperties',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkDrmFormatModifierPropertiesList2EXT',
    'VkDrmFormatModifierPropertiesListEXT',
    'VkFormatProperties3',
    'VkSubpassResolvePerformanceQueryEXT',
}
_includes_ = {
    'VkFormatProperties',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetPhysicalDeviceFormatProperties2',
}
