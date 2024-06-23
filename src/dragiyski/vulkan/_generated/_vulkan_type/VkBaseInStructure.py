import ctypes

class CType(ctypes.Structure):
    pass


VkBaseInStructure = CType
CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.POINTER(VkBaseInStructure)),
]
del VkBaseInStructure

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkBaseInStructure',
    },
    'included_in': {
        'VkBaseInStructure',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next'], 'type': 'VkBaseInStructure'},
    }
}
