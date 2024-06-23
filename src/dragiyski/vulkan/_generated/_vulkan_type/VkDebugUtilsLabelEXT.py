import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pLabelName', ctypes.c_char_p),
        ('color', ctypes.ARRAY(ctypes.c_float, 4)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkDebugUtilsMessengerCallbackDataEXT',
    },
    'input_of': {
        'vkCmdBeginDebugUtilsLabelEXT',
        'vkCmdInsertDebugUtilsLabelEXT',
        'vkQueueBeginDebugUtilsLabelEXT',
        'vkQueueInsertDebugUtilsLabelEXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DEBUG_UTILS_LABEL_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pLabelName': {'python_name': ['p', 'label', 'name'], 'len': [['null-terminated']]},
        'color': {'python_name': ['color']},
    }
}
