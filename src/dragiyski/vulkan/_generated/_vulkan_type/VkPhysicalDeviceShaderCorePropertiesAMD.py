import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderEngineCount', ctypes.c_uint32),
        ('shaderArraysPerEngineCount', ctypes.c_uint32),
        ('computeUnitsPerShaderArray', ctypes.c_uint32),
        ('simdPerComputeUnit', ctypes.c_uint32),
        ('wavefrontsPerSimd', ctypes.c_uint32),
        ('wavefrontSize', ctypes.c_uint32),
        ('sgprsPerSimd', ctypes.c_uint32),
        ('minSgprAllocation', ctypes.c_uint32),
        ('maxSgprAllocation', ctypes.c_uint32),
        ('sgprAllocationGranularity', ctypes.c_uint32),
        ('vgprsPerSimd', ctypes.c_uint32),
        ('minVgprAllocation', ctypes.c_uint32),
        ('maxVgprAllocation', ctypes.c_uint32),
        ('vgprAllocationGranularity', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_CORE_PROPERTIES_AMD', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'shaderEngineCount': {'python_name': ['shader', 'engine', 'count']},
        'shaderArraysPerEngineCount': {'python_name': ['shader', 'arrays', 'per', 'engine', 'count']},
        'computeUnitsPerShaderArray': {'python_name': ['compute', 'units', 'per', 'shader', 'array']},
        'simdPerComputeUnit': {'python_name': ['simd', 'per', 'compute', 'unit']},
        'wavefrontsPerSimd': {'python_name': ['wavefronts', 'per', 'simd']},
        'wavefrontSize': {'python_name': ['wavefront', 'size']},
        'sgprsPerSimd': {'python_name': ['sgprs', 'per', 'simd']},
        'minSgprAllocation': {'python_name': ['min', 'sgpr', 'allocation']},
        'maxSgprAllocation': {'python_name': ['max', 'sgpr', 'allocation']},
        'sgprAllocationGranularity': {'python_name': ['sgpr', 'allocation', 'granularity']},
        'vgprsPerSimd': {'python_name': ['vgprs', 'per', 'simd']},
        'minVgprAllocation': {'python_name': ['min', 'vgpr', 'allocation']},
        'maxVgprAllocation': {'python_name': ['max', 'vgpr', 'allocation']},
        'vgprAllocationGranularity': {'python_name': ['vgpr', 'allocation', 'granularity']},
    }
}
