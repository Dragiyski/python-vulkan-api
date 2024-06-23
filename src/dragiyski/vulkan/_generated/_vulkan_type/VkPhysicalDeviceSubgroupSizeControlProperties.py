import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('minSubgroupSize', ctypes.c_uint32),
        ('maxSubgroupSize', ctypes.c_uint32),
        ('maxComputeWorkgroupSubgroups', ctypes.c_uint32),
        ('requiredSubgroupSizeStages', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkPhysicalDeviceProperties2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SUBGROUP_SIZE_CONTROL_PROPERTIES', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'minSubgroupSize': {'python_name': ['min', 'subgroup', 'size']},
        'maxSubgroupSize': {'python_name': ['max', 'subgroup', 'size']},
        'maxComputeWorkgroupSubgroups': {'python_name': ['max', 'compute', 'workgroup', 'subgroups']},
        'requiredSubgroupSizeStages': {'python_name': ['required', 'subgroup', 'size', 'stages'], 'type': 'VkShaderStageFlags'},
    }
}
