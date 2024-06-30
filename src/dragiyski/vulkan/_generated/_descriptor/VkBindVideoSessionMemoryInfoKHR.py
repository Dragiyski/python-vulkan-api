from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkBindVideoSessionMemoryInfoKHR'
_member_list_ = ['sType', 'pNext', 'memoryBindIndex', 'memory', 'memoryOffset', 'memorySize']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_BIND_VIDEO_SESSION_MEMORY_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'memoryBindIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'memory': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'memoryOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'memorySize': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkBindVideoSessionMemoryKHR',
}
_output_of_ = set()
