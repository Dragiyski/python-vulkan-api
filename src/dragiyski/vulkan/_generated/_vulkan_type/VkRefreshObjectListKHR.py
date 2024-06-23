import ctypes

class CType(ctypes.Structure):
    pass

from .VkRefreshObjectKHR import CType as VkRefreshObjectKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('objectCount', ctypes.c_uint32),
    ('pObjects', ctypes.POINTER(VkRefreshObjectKHR)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkRefreshObjectKHR',
    },
    'included_in': set(),
    'input_of': {
        'vkCmdRefreshObjectsKHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_REFRESH_OBJECT_LIST_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'objectCount': {'python_name': ['object', 'count']},
        'pObjects': {'python_name': ['p', 'objects'], 'len': [['objectCount']], 'type': 'VkRefreshObjectKHR'},
    }
}
