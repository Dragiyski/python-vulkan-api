import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('accelerationStructure', ctypes.c_void_p),
        ('accelerationStructureNV', ctypes.c_void_p),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkGetAccelerationStructureOpaqueCaptureDescriptorDataEXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_CAPTURE_DESCRIPTOR_DATA_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'accelerationStructure': {'python_name': ['acceleration', 'structure']},
        'accelerationStructureNV': {'python_name': ['acceleration', 'structure', 'nv']},
    }
}
