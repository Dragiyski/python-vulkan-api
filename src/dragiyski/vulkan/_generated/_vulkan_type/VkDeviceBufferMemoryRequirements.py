import ctypes

class CType(ctypes.Structure):
    pass

from .VkBufferCreateInfo import CType as VkBufferCreateInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pCreateInfo', ctypes.POINTER(VkBufferCreateInfo)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkBufferCreateInfo',
    },
    'included_in': set(),
    'input_of': {
        'vkGetDeviceBufferMemoryRequirements',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DEVICE_BUFFER_MEMORY_REQUIREMENTS', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pCreateInfo': {'python_name': ['p', 'create', 'info'], 'type': 'VkBufferCreateInfo'},
    }
}
