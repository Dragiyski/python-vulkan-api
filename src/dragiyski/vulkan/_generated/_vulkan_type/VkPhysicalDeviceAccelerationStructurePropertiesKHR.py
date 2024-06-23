import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxGeometryCount', ctypes.c_uint64),
        ('maxInstanceCount', ctypes.c_uint64),
        ('maxPrimitiveCount', ctypes.c_uint64),
        ('maxPerStageDescriptorAccelerationStructures', ctypes.c_uint32),
        ('maxPerStageDescriptorUpdateAfterBindAccelerationStructures', ctypes.c_uint32),
        ('maxDescriptorSetAccelerationStructures', ctypes.c_uint32),
        ('maxDescriptorSetUpdateAfterBindAccelerationStructures', ctypes.c_uint32),
        ('minAccelerationStructureScratchOffsetAlignment', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ACCELERATION_STRUCTURE_PROPERTIES_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'maxGeometryCount': {'python_name': ['max', 'geometry', 'count']},
        'maxInstanceCount': {'python_name': ['max', 'instance', 'count']},
        'maxPrimitiveCount': {'python_name': ['max', 'primitive', 'count']},
        'maxPerStageDescriptorAccelerationStructures': {'python_name': ['max', 'per', 'stage', 'descriptor', 'acceleration', 'structures']},
        'maxPerStageDescriptorUpdateAfterBindAccelerationStructures': {'python_name': ['max', 'per', 'stage', 'descriptor', 'update', 'after', 'bind', 'acceleration', 'structures']},
        'maxDescriptorSetAccelerationStructures': {'python_name': ['max', 'descriptor', 'set', 'acceleration', 'structures']},
        'maxDescriptorSetUpdateAfterBindAccelerationStructures': {'python_name': ['max', 'descriptor', 'set', 'update', 'after', 'bind', 'acceleration', 'structures']},
        'minAccelerationStructureScratchOffsetAlignment': {'python_name': ['min', 'acceleration', 'structure', 'scratch', 'offset', 'alignment']},
    }
}
