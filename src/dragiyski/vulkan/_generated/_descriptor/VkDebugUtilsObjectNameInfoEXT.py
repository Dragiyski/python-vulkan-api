from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDebugUtilsObjectNameInfoEXT'
_member_list_ = ['sType', 'pNext', 'objectType', 'objectHandle', 'pObjectName']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DEBUG_UTILS_OBJECT_NAME_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'objectType': {
        'type': CIntType('c_int'),
        'type_name': 'VkObjectType',
        'enum': 'VkObjectType',
        'is_string': False,
    },
    'objectHandle': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'pObjectName': {
        'type': CStringType('c_char_p'),
        'length': [],
        'is_string': True,
    },
}
_extends_ = {
    'VkPipelineShaderStageCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkDebugUtilsMessengerCallbackDataEXT',
}
_input_of_ = {
    'vkSetDebugUtilsObjectNameEXT',
}
_output_of_ = set()
