import ctypes

class CType(ctypes.Structure):
    pass

from .VkDebugUtilsLabelEXT import CType as VkDebugUtilsLabelEXT
from .VkDebugUtilsObjectNameInfoEXT import CType as VkDebugUtilsObjectNameInfoEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pMessageIdName', ctypes.c_char_p),
    ('messageIdNumber', ctypes.c_int32),
    ('pMessage', ctypes.c_char_p),
    ('queueLabelCount', ctypes.c_uint32),
    ('pQueueLabels', ctypes.POINTER(VkDebugUtilsLabelEXT)),
    ('cmdBufLabelCount', ctypes.c_uint32),
    ('pCmdBufLabels', ctypes.POINTER(VkDebugUtilsLabelEXT)),
    ('objectCount', ctypes.c_uint32),
    ('pObjects', ctypes.POINTER(VkDebugUtilsObjectNameInfoEXT)),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkDeviceAddressBindingCallbackDataEXT',
    },
    'includes': {
        'VkDebugUtilsLabelEXT',
        'VkDebugUtilsObjectNameInfoEXT',
    },
    'included_in': set(),
    'input_of': {
        'vkSubmitDebugUtilsMessageEXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DEBUG_UTILS_MESSENGER_CALLBACK_DATA_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkDebugUtilsMessengerCallbackDataFlagsEXT'},
        'pMessageIdName': {'python_name': ['p', 'message', 'id', 'name'], 'len': [['null-terminated']]},
        'messageIdNumber': {'python_name': ['message', 'id', 'number']},
        'pMessage': {'python_name': ['p', 'message'], 'len': [['null-terminated']]},
        'queueLabelCount': {'python_name': ['queue', 'label', 'count']},
        'pQueueLabels': {'python_name': ['p', 'queue', 'labels'], 'len': [['queueLabelCount']], 'type': 'VkDebugUtilsLabelEXT'},
        'cmdBufLabelCount': {'python_name': ['cmd', 'buf', 'label', 'count']},
        'pCmdBufLabels': {'python_name': ['p', 'cmd', 'buf', 'labels'], 'len': [['cmdBufLabelCount']], 'type': 'VkDebugUtilsLabelEXT'},
        'objectCount': {'python_name': ['object', 'count']},
        'pObjects': {'python_name': ['p', 'objects'], 'len': [['objectCount']], 'type': 'VkDebugUtilsObjectNameInfoEXT'},
    }
}
