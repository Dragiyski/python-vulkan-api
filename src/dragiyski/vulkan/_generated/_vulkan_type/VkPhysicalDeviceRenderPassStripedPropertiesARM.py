import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('renderPassStripeGranularity', VkExtent2D),
    ('maxRenderPassStripes', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RENDER_PASS_STRIPED_PROPERTIES_ARM', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'renderPassStripeGranularity': {'python_name': ['render', 'pass', 'stripe', 'granularity'], 'type': 'VkExtent2D'},
        'maxRenderPassStripes': {'python_name': ['max', 'render', 'pass', 'stripes']},
    }
}
