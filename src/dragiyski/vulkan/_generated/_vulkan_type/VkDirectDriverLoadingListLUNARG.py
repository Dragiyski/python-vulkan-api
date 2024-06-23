import ctypes

class CType(ctypes.Structure):
    pass

from .VkDirectDriverLoadingInfoLUNARG import CType as VkDirectDriverLoadingInfoLUNARG

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('mode', ctypes.c_int),
    ('driverCount', ctypes.c_uint32),
    ('pDrivers', ctypes.POINTER(VkDirectDriverLoadingInfoLUNARG)),
]

descriptor = {
    'extends': {
        'VkInstanceCreateInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkDirectDriverLoadingInfoLUNARG',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DIRECT_DRIVER_LOADING_LIST_LUNARG', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'mode': {'python_name': ['mode'], 'type': 'VkDirectDriverLoadingModeLUNARG'},
        'driverCount': {'python_name': ['driver', 'count']},
        'pDrivers': {'python_name': ['p', 'drivers'], 'len': [['driverCount']], 'type': 'VkDirectDriverLoadingInfoLUNARG'},
    }
}
