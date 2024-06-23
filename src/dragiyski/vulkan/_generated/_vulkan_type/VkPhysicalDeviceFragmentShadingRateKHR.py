import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('sampleCounts', ctypes.c_uint32),
    ('fragmentSize', VkExtent2D),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkExtent2D',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceFragmentShadingRatesKHR',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADING_RATE_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'sampleCounts': {'python_name': ['sample', 'counts'], 'type': 'VkSampleCountFlags'},
        'fragmentSize': {'python_name': ['fragment', 'size'], 'type': 'VkExtent2D'},
    }
}
