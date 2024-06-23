import ctypes

class CType(ctypes.Structure):
    pass

from .VkPhysicalDeviceLimits import CType as VkPhysicalDeviceLimits
from .VkPhysicalDeviceSparseProperties import CType as VkPhysicalDeviceSparseProperties

CType._fields_ = [
    ('apiVersion', ctypes.c_uint32),
    ('driverVersion', ctypes.c_uint32),
    ('vendorID', ctypes.c_uint32),
    ('deviceID', ctypes.c_uint32),
    ('deviceType', ctypes.c_int),
    ('deviceName', ctypes.ARRAY(ctypes.c_char, 256)),
    ('pipelineCacheUUID', ctypes.ARRAY(ctypes.c_uint8, 16)),
    ('limits', VkPhysicalDeviceLimits),
    ('sparseProperties', VkPhysicalDeviceSparseProperties),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkPhysicalDeviceLimits',
        'VkPhysicalDeviceSparseProperties',
    },
    'included_in': {
        'VkPhysicalDeviceProperties2',
    },
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceProperties',
    },
    'member_map': {
        'apiVersion': {'python_name': ['api', 'version']},
        'driverVersion': {'python_name': ['driver', 'version']},
        'vendorID': {'python_name': ['vendor', 'id']},
        'deviceID': {'python_name': ['device', 'id']},
        'deviceType': {'python_name': ['device', 'type'], 'type': 'VkPhysicalDeviceType'},
        'deviceName': {'python_name': ['device', 'name'], 'len': [['null-terminated']]},
        'pipelineCacheUUID': {'python_name': ['pipeline', 'cache', 'uuid']},
        'limits': {'python_name': ['limits'], 'type': 'VkPhysicalDeviceLimits'},
        'sparseProperties': {'python_name': ['sparse', 'properties'], 'type': 'VkPhysicalDeviceSparseProperties'},
    }
}
