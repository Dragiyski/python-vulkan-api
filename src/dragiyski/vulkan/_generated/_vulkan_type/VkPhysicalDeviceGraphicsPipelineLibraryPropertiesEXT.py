import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('graphicsPipelineLibraryFastLinking', ctypes.c_uint32),
        ('graphicsPipelineLibraryIndependentInterpolationDecoration', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_GRAPHICS_PIPELINE_LIBRARY_PROPERTIES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'graphicsPipelineLibraryFastLinking': {'python_name': ['graphics', 'pipeline', 'library', 'fast', 'linking']},
        'graphicsPipelineLibraryIndependentInterpolationDecoration': {'python_name': ['graphics', 'pipeline', 'library', 'independent', 'interpolation', 'decoration']},
    }
}
