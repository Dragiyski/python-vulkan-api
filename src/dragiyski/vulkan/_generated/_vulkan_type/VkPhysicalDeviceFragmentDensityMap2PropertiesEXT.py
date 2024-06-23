import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('subsampledLoads', ctypes.c_uint32),
        ('subsampledCoarseReconstructionEarlyAccess', ctypes.c_uint32),
        ('maxSubsampledArrayLayers', ctypes.c_uint32),
        ('maxDescriptorSetSubsampledSamplers', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_DENSITY_MAP_2_PROPERTIES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'subsampledLoads': {'python_name': ['subsampled', 'loads']},
        'subsampledCoarseReconstructionEarlyAccess': {'python_name': ['subsampled', 'coarse', 'reconstruction', 'early', 'access']},
        'maxSubsampledArrayLayers': {'python_name': ['max', 'subsampled', 'array', 'layers']},
        'maxDescriptorSetSubsampledSamplers': {'python_name': ['max', 'descriptor', 'set', 'subsampled', 'samplers']},
    }
}
