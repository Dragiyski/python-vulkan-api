import ctypes

class CType(ctypes.Structure):
    pass

from .VkCommandBufferInheritanceInfo import CType as VkCommandBufferInheritanceInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pInheritanceInfo', ctypes.POINTER(VkCommandBufferInheritanceInfo)),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkDeviceGroupCommandBufferBeginInfo',
    },
    'includes': {
        'VkCommandBufferInheritanceInfo',
    },
    'included_in': set(),
    'input_of': {
        'vkBeginCommandBuffer',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_COMMAND_BUFFER_BEGIN_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkCommandBufferUsageFlags'},
        'pInheritanceInfo': {'python_name': ['p', 'inheritance', 'info'], 'type': 'VkCommandBufferInheritanceInfo'},
    }
}
