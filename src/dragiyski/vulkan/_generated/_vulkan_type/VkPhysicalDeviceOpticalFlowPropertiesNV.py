import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('supportedOutputGridSizes', ctypes.c_uint32),
        ('supportedHintGridSizes', ctypes.c_uint32),
        ('hintSupported', ctypes.c_uint32),
        ('costSupported', ctypes.c_uint32),
        ('bidirectionalFlowSupported', ctypes.c_uint32),
        ('globalFlowSupported', ctypes.c_uint32),
        ('minWidth', ctypes.c_uint32),
        ('minHeight', ctypes.c_uint32),
        ('maxWidth', ctypes.c_uint32),
        ('maxHeight', ctypes.c_uint32),
        ('maxNumRegionsOfInterest', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_OPTICAL_FLOW_PROPERTIES_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'supportedOutputGridSizes': {'python_name': ['supported', 'output', 'grid', 'sizes'], 'type': 'VkOpticalFlowGridSizeFlagsNV'},
        'supportedHintGridSizes': {'python_name': ['supported', 'hint', 'grid', 'sizes'], 'type': 'VkOpticalFlowGridSizeFlagsNV'},
        'hintSupported': {'python_name': ['hint', 'supported']},
        'costSupported': {'python_name': ['cost', 'supported']},
        'bidirectionalFlowSupported': {'python_name': ['bidirectional', 'flow', 'supported']},
        'globalFlowSupported': {'python_name': ['global', 'flow', 'supported']},
        'minWidth': {'python_name': ['min', 'width']},
        'minHeight': {'python_name': ['min', 'height']},
        'maxWidth': {'python_name': ['max', 'width']},
        'maxHeight': {'python_name': ['max', 'height']},
        'maxNumRegionsOfInterest': {'python_name': ['max', 'num', 'regions', 'of', 'interest']},
    }
}
