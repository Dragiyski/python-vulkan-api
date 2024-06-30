from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDebugUtilsMessengerCallbackDataEXT'
_member_list_ = ['sType', 'pNext', 'flags', 'pMessageIdName', 'messageIdNumber', 'pMessage', 'queueLabelCount', 'pQueueLabels', 'cmdBufLabelCount', 'pCmdBufLabels', 'objectCount', 'pObjects']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DEBUG_UTILS_MESSENGER_CALLBACK_DATA_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkDebugUtilsMessengerCallbackDataFlagsEXT',
        'enum': 'VkDebugUtilsMessengerCallbackDataFlagsEXT',
        'is_string': False,
    },
    'pMessageIdName': {
        'type': CStringType('c_char_p'),
        'length': [],
        'is_string': True,
    },
    'messageIdNumber': {
        'type': CIntType('c_int32'),
        'is_string': False,
    },
    'pMessage': {
        'type': CStringType('c_char_p'),
        'length': [],
        'is_string': True,
    },
    'queueLabelCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pQueueLabels': {
        'type': CPointerType(CComplexType('VkDebugUtilsLabelEXT')),
        'type_name': 'VkDebugUtilsLabelEXT',
        'structure': 'VkDebugUtilsLabelEXT',
        'length': [['queueLabelCount']],
        'is_string': False,
    },
    'cmdBufLabelCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pCmdBufLabels': {
        'type': CPointerType(CComplexType('VkDebugUtilsLabelEXT')),
        'type_name': 'VkDebugUtilsLabelEXT',
        'structure': 'VkDebugUtilsLabelEXT',
        'length': [['cmdBufLabelCount']],
        'is_string': False,
    },
    'objectCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pObjects': {
        'type': CPointerType(CComplexType('VkDebugUtilsObjectNameInfoEXT')),
        'type_name': 'VkDebugUtilsObjectNameInfoEXT',
        'structure': 'VkDebugUtilsObjectNameInfoEXT',
        'length': [['objectCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkDeviceAddressBindingCallbackDataEXT',
}
_includes_ = {
    'VkDebugUtilsLabelEXT',
    'VkDebugUtilsObjectNameInfoEXT',
}
_included_in_ = set()
_input_of_ = {
    'vkSubmitDebugUtilsMessageEXT',
}
_output_of_ = set()
