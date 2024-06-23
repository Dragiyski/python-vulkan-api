import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('clientType', ctypes.c_int),
        ('primitiveType', ctypes.c_int),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkGetPhysicalDeviceSciSyncAttributesNV',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SCI_SYNC_ATTRIBUTES_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'clientType': {'python_name': ['client', 'type'], 'type': 'VkSciSyncClientTypeNV'},
        'primitiveType': {'python_name': ['primitive', 'type'], 'type': 'VkSciSyncPrimitiveTypeNV'},
    }
}
