import ctypes

class CType(ctypes.Structure):
    pass

from ..vulkan_callback import vkGetInstanceProcAddrLUNARG

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pfnGetInstanceProcAddr', vkGetInstanceProcAddrLUNARG),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkDirectDriverLoadingListLUNARG',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DIRECT_DRIVER_LOADING_INFO_LUNARG', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkDirectDriverLoadingFlagsLUNARG'},
        'pfnGetInstanceProcAddr': {'python_name': ['pfn', 'get', 'instance', 'proc', 'addr']},
    }
}
