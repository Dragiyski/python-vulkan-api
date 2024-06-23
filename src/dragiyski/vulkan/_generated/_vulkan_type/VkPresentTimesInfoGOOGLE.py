import ctypes

class CType(ctypes.Structure):
    pass

from .VkPresentTimeGOOGLE import CType as VkPresentTimeGOOGLE

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('swapchainCount', ctypes.c_uint32),
    ('pTimes', ctypes.POINTER(VkPresentTimeGOOGLE)),
]

descriptor = {
    'extends': {
        'VkPresentInfoKHR',
    },
    'extended_by': set(),
    'includes': {
        'VkPresentTimeGOOGLE',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PRESENT_TIMES_INFO_GOOGLE', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'swapchainCount': {'python_name': ['swapchain', 'count']},
        'pTimes': {'python_name': ['p', 'times'], 'len': [['swapchainCount']], 'type': 'VkPresentTimeGOOGLE'},
    }
}
