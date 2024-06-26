import ctypes

class VkPhysicalDeviceShaderCorePropertiesAMD(ctypes.Structure):
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

    _init_ = []
    _extends_ = {
        'VkPhysicalDeviceProperties2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'shaderEngineCount': 'shader_engine_count',
        'shaderArraysPerEngineCount': 'shader_arrays_per_engine_count',
        'computeUnitsPerShaderArray': 'compute_units_per_shader_array',
        'simdPerComputeUnit': 'simd_per_compute_unit',
        'wavefrontsPerSimd': 'wavefronts_per_simd',
        'wavefrontSize': 'wavefront_size',
        'sgprsPerSimd': 'sgprs_per_simd',
        'minSgprAllocation': 'min_sgpr_allocation',
        'maxSgprAllocation': 'max_sgpr_allocation',
        'sgprAllocationGranularity': 'sgpr_allocation_granularity',
        'vgprsPerSimd': 'vgprs_per_simd',
        'minVgprAllocation': 'min_vgpr_allocation',
        'maxVgprAllocation': 'max_vgpr_allocation',
        'vgprAllocationGranularity': 'vgpr_allocation_granularity',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_AMD_shader_core_properties',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_CORE_PROPERTIES_AMD'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_CORE_PROPERTIES_AMD
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceShaderCorePropertiesAMD._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderEngineCount': ctypes.c_uint32,
    'shaderArraysPerEngineCount': ctypes.c_uint32,
    'computeUnitsPerShaderArray': ctypes.c_uint32,
    'simdPerComputeUnit': ctypes.c_uint32,
    'wavefrontsPerSimd': ctypes.c_uint32,
    'wavefrontSize': ctypes.c_uint32,
    'sgprsPerSimd': ctypes.c_uint32,
    'minSgprAllocation': ctypes.c_uint32,
    'maxSgprAllocation': ctypes.c_uint32,
    'sgprAllocationGranularity': ctypes.c_uint32,
    'vgprsPerSimd': ctypes.c_uint32,
    'minVgprAllocation': ctypes.c_uint32,
    'maxVgprAllocation': ctypes.c_uint32,
    'vgprAllocationGranularity': ctypes.c_uint32,
}
