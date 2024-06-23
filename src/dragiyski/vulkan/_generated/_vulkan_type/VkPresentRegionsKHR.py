import ctypes

class CType(ctypes.Structure):
    pass

from .VkPresentRegionKHR import CType as VkPresentRegionKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('swapchainCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkPresentRegionKHR)),
]

descriptor = {
    'extends': {
        'VkPresentInfoKHR',
    },
    'extended_by': set(),
    'includes': {
        'VkPresentRegionKHR',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PRESENT_REGIONS_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'swapchainCount': {'python_name': ['swapchain', 'count']},
        'pRegions': {'python_name': ['p', 'regions'], 'len': [['swapchainCount']], 'type': 'VkPresentRegionKHR'},
    }
}
