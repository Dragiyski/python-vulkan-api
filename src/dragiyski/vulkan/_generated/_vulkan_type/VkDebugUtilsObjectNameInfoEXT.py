import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('objectType', ctypes.c_int),
        ('objectHandle', ctypes.c_uint64),
        ('pObjectName', ctypes.c_char_p),
    ]

descriptor = {
    'extends': {
        'VkPipelineShaderStageCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkDebugUtilsMessengerCallbackDataEXT',
    },
    'input_of': {
        'vkSetDebugUtilsObjectNameEXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DEBUG_UTILS_OBJECT_NAME_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'objectType': {'python_name': ['object', 'type'], 'type': 'VkObjectType'},
        'objectHandle': {'python_name': ['object', 'handle']},
        'pObjectName': {'python_name': ['p', 'object', 'name'], 'len': [['null-terminated']]},
    }
}
