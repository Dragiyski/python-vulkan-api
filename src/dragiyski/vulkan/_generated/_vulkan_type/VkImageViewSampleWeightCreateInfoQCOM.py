import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D
from .VkOffset2D import CType as VkOffset2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('filterCenter', VkOffset2D),
    ('filterSize', VkExtent2D),
    ('numPhases', ctypes.c_uint32),
]

descriptor = {
    'extends': {
        'VkImageViewCreateInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkExtent2D',
        'VkOffset2D',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_IMAGE_VIEW_SAMPLE_WEIGHT_CREATE_INFO_QCOM', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'filterCenter': {'python_name': ['filter', 'center'], 'type': 'VkOffset2D'},
        'filterSize': {'python_name': ['filter', 'size'], 'type': 'VkExtent2D'},
        'numPhases': {'python_name': ['num', 'phases']},
    }
}
