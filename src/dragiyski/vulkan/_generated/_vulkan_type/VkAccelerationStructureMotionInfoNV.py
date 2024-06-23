import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxInstances', ctypes.c_uint32),
        ('flags', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkAccelerationStructureCreateInfoKHR',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_MOTION_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'maxInstances': {'python_name': ['max', 'instances']},
        'flags': {'python_name': ['flags'], 'type': 'VkAccelerationStructureMotionInfoFlagsNV'},
    }
}
