from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDebugUtilsMessengerCreateInfoEXT'
_member_list_ = ['sType', 'pNext', 'flags', 'messageSeverity', 'messageType', 'pfnUserCallback', 'pUserData']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DEBUG_UTILS_MESSENGER_CREATE_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkDebugUtilsMessengerCreateFlagsEXT',
        'enum': 'VkDebugUtilsMessengerCreateFlagsEXT',
        'is_string': False,
    },
    'messageSeverity': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkDebugUtilsMessageSeverityFlagsEXT',
        'enum': 'VkDebugUtilsMessageSeverityFlagsEXT',
        'is_string': False,
    },
    'messageType': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkDebugUtilsMessageTypeFlagsEXT',
        'enum': 'VkDebugUtilsMessageTypeFlagsEXT',
        'is_string': False,
    },
    'pfnUserCallback': {
        'type': CFunctionType('vkDebugUtilsMessengerCallbackEXT'),
        'callback': 'vkDebugUtilsMessengerCallbackEXT',
        'is_string': False,
    },
    'pUserData': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = {
    'VkInstanceCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCreateDebugUtilsMessengerEXT',
}
_output_of_ = set()
