import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent3D import CType as VkExtent3D

CType._fields_ = [
    ('queueFlags', ctypes.c_uint32),
    ('queueCount', ctypes.c_uint32),
    ('timestampValidBits', ctypes.c_uint32),
    ('minImageTransferGranularity', VkExtent3D),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkExtent3D',
    },
    'included_in': {
        'VkQueueFamilyProperties2',
    },
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceQueueFamilyProperties',
    },
    'member_map': {
        'queueFlags': {'python_name': ['queue', 'flags'], 'type': 'VkQueueFlags'},
        'queueCount': {'python_name': ['queue', 'count']},
        'timestampValidBits': {'python_name': ['timestamp', 'valid', 'bits']},
        'minImageTransferGranularity': {'python_name': ['min', 'image', 'transfer', 'granularity'], 'type': 'VkExtent3D'},
    }
}
