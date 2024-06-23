import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('maxSampleLocationGridSize', VkExtent2D),
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
        'vkGetPhysicalDeviceMultisamplePropertiesEXT',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_MULTISAMPLE_PROPERTIES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'maxSampleLocationGridSize': {'python_name': ['max', 'sample', 'location', 'grid', 'size'], 'type': 'VkExtent2D'},
    }
}
