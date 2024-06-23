import ctypes

class CType(ctypes.Structure):
    pass

from .VkSemaphoreSubmitInfo import CType as VkSemaphoreSubmitInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stripeSemaphoreInfoCount', ctypes.c_uint32),
    ('pStripeSemaphoreInfos', ctypes.POINTER(VkSemaphoreSubmitInfo)),
]

descriptor = {
    'extends': {
        'VkCommandBufferSubmitInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkSemaphoreSubmitInfo',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_RENDER_PASS_STRIPE_SUBMIT_INFO_ARM', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'stripeSemaphoreInfoCount': {'python_name': ['stripe', 'semaphore', 'info', 'count']},
        'pStripeSemaphoreInfos': {'python_name': ['p', 'stripe', 'semaphore', 'infos'], 'len': [['stripeSemaphoreInfoCount']], 'type': 'VkSemaphoreSubmitInfo'},
    }
}
