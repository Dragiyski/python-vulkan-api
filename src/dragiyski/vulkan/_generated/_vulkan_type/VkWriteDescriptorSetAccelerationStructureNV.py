import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('accelerationStructureCount', ctypes.c_uint32),
        ('pAccelerationStructures', ctypes.POINTER(ctypes.c_void_p)),
    ]

descriptor = {
    'extends': {
        'VkWriteDescriptorSet',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET_ACCELERATION_STRUCTURE_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'accelerationStructureCount': {'python_name': ['acceleration', 'structure', 'count']},
        'pAccelerationStructures': {'python_name': ['p', 'acceleration', 'structures'], 'len': [['accelerationStructureCount']]},
    }
}
