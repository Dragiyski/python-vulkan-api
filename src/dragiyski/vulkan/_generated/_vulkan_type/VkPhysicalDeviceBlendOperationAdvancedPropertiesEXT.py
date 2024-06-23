import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('advancedBlendMaxColorAttachments', ctypes.c_uint32),
        ('advancedBlendIndependentBlend', ctypes.c_uint32),
        ('advancedBlendNonPremultipliedSrcColor', ctypes.c_uint32),
        ('advancedBlendNonPremultipliedDstColor', ctypes.c_uint32),
        ('advancedBlendCorrelatedOverlap', ctypes.c_uint32),
        ('advancedBlendAllOperations', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_BLEND_OPERATION_ADVANCED_PROPERTIES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'advancedBlendMaxColorAttachments': {'python_name': ['advanced', 'blend', 'max', 'color', 'attachments']},
        'advancedBlendIndependentBlend': {'python_name': ['advanced', 'blend', 'independent', 'blend']},
        'advancedBlendNonPremultipliedSrcColor': {'python_name': ['advanced', 'blend', 'non', 'premultiplied', 'src', 'color']},
        'advancedBlendNonPremultipliedDstColor': {'python_name': ['advanced', 'blend', 'non', 'premultiplied', 'dst', 'color']},
        'advancedBlendCorrelatedOverlap': {'python_name': ['advanced', 'blend', 'correlated', 'overlap']},
        'advancedBlendAllOperations': {'python_name': ['advanced', 'blend', 'all', 'operations']},
    }
}
