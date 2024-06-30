from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDebugReportCallbackCreateInfoEXT'
_member_list_ = ['sType', 'pNext', 'flags', 'pfnCallback', 'pUserData']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DEBUG_REPORT_CALLBACK_CREATE_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkDebugReportFlagsEXT',
        'enum': 'VkDebugReportFlagsEXT',
        'is_string': False,
    },
    'pfnCallback': {
        'type': CFunctionType('vkDebugReportCallbackEXT'),
        'callback': 'vkDebugReportCallbackEXT',
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
    'vkCreateDebugReportCallbackEXT',
}
_output_of_ = set()
