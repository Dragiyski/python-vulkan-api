import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('maxWeightFilterPhases', ctypes.c_uint32),
    ('maxWeightFilterDimension', VkExtent2D),
    ('maxBlockMatchRegion', VkExtent2D),
    ('maxBoxFilterBlockSize', VkExtent2D),
]

descriptor = {
    'extends': {
        'VkPhysicalDeviceProperties2',
    },
    'extended_by': set(),
    'includes': {
        'VkExtent2D',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_PROCESSING_PROPERTIES_QCOM', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'maxWeightFilterPhases': {'python_name': ['max', 'weight', 'filter', 'phases']},
        'maxWeightFilterDimension': {'python_name': ['max', 'weight', 'filter', 'dimension'], 'type': 'VkExtent2D'},
        'maxBlockMatchRegion': {'python_name': ['max', 'block', 'match', 'region'], 'type': 'VkExtent2D'},
        'maxBoxFilterBlockSize': {'python_name': ['max', 'box', 'filter', 'block', 'size'], 'type': 'VkExtent2D'},
    }
}
