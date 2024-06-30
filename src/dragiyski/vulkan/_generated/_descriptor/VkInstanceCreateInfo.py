from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkInstanceCreateInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'pApplicationInfo', 'enabledLayerCount', 'ppEnabledLayerNames', 'enabledExtensionCount', 'ppEnabledExtensionNames']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkInstanceCreateFlags',
        'enum': 'VkInstanceCreateFlags',
        'is_string': False,
    },
    'pApplicationInfo': {
        'type': CPointerType(CComplexType('VkApplicationInfo')),
        'type_name': 'VkApplicationInfo',
        'structure': 'VkApplicationInfo',
        'is_string': False,
    },
    'enabledLayerCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'ppEnabledLayerNames': {
        'type': CPointerType(CStringType('c_char_p')),
        'length': [['enabledLayerCount']],
        'is_string': True,
    },
    'enabledExtensionCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'ppEnabledExtensionNames': {
        'type': CPointerType(CStringType('c_char_p')),
        'length': [['enabledExtensionCount']],
        'is_string': True,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkDebugReportCallbackCreateInfoEXT',
    'VkDebugUtilsMessengerCreateInfoEXT',
    'VkDirectDriverLoadingListLUNARG',
    'VkExportMetalObjectCreateInfoEXT',
    'VkLayerSettingsCreateInfoEXT',
    'VkValidationFeaturesEXT',
    'VkValidationFlagsEXT',
}
_includes_ = {
    'VkApplicationInfo',
}
_included_in_ = set()
_input_of_ = {
    'vkCreateInstance',
}
_output_of_ = set()
