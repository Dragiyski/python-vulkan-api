import ctypes

class CType(ctypes.Structure):
    pass

from ..vulkan_callback import vkFaultCallbackFunction
from .VkFaultData import CType as VkFaultData

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('faultCount', ctypes.c_uint32),
    ('pFaults', ctypes.POINTER(VkFaultData)),
    ('pfnFaultCallback', vkFaultCallbackFunction),
]

descriptor = {
    'extends': {
        'VkDeviceCreateInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkFaultData',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_FAULT_CALLBACK_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'faultCount': {'python_name': ['fault', 'count']},
        'pFaults': {'python_name': ['p', 'faults'], 'len': [['faultCount']], 'type': 'VkFaultData'},
        'pfnFaultCallback': {'python_name': ['pfn', 'fault', 'callback']},
    }
}
