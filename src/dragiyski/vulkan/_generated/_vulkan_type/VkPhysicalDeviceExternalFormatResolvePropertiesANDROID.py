import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('nullColorAttachmentWithExternalFormatResolve', ctypes.c_uint32),
        ('externalFormatResolveChromaOffsetX', ctypes.c_int),
        ('externalFormatResolveChromaOffsetY', ctypes.c_int),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_FORMAT_RESOLVE_PROPERTIES_ANDROID', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'nullColorAttachmentWithExternalFormatResolve': {'python_name': ['null', 'color', 'attachment', 'with', 'external', 'format', 'resolve']},
        'externalFormatResolveChromaOffsetX': {'python_name': ['external', 'format', 'resolve', 'chroma', 'offset', 'x'], 'type': 'VkChromaLocation'},
        'externalFormatResolveChromaOffsetY': {'python_name': ['external', 'format', 'resolve', 'chroma', 'offset', 'y'], 'type': 'VkChromaLocation'},
    }
}
