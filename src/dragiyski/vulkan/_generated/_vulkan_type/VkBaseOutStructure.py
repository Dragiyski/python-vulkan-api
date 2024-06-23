import ctypes

class CType(ctypes.Structure):
    pass


VkBaseOutStructure = CType
CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.POINTER(VkBaseOutStructure)),
]
del VkBaseOutStructure

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkBaseOutStructure',
    },
    'included_in': {
        'VkBaseOutStructure',
    },
    'input_of': set(),
    'output_of': {
        'vkGetPipelinePropertiesEXT',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next'], 'type': 'VkBaseOutStructure'},
    }
}
