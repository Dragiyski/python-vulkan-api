import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderCoreFeatures', ctypes.c_uint32),
        ('activeComputeUnitCount', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_CORE_PROPERTIES_2_AMD', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'shaderCoreFeatures': {'python_name': ['shader', 'core', 'features'], 'type': 'VkShaderCorePropertiesFlagsAMD'},
        'activeComputeUnitCount': {'python_name': ['active', 'compute', 'unit', 'count']},
    }
}
