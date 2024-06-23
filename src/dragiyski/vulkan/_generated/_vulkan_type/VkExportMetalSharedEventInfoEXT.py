import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('semaphore', ctypes.c_void_p),
        ('event', ctypes.c_void_p),
        ('mtlSharedEvent', ctypes.c_void_p),
    ]

descriptor = {
    'extends': {
        'VkExportMetalObjectsInfoEXT',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_EXPORT_METAL_SHARED_EVENT_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'semaphore': {'python_name': ['semaphore']},
        'event': {'python_name': ['event']},
        'mtlSharedEvent': {'python_name': ['mtl', 'shared', 'event']},
    }
}
