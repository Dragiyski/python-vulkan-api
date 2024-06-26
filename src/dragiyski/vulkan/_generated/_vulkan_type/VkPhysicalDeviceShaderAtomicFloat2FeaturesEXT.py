import ctypes

class VkPhysicalDeviceShaderAtomicFloat2FeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderBufferFloat16Atomics', ctypes.c_uint32),
        ('shaderBufferFloat16AtomicAdd', ctypes.c_uint32),
        ('shaderBufferFloat16AtomicMinMax', ctypes.c_uint32),
        ('shaderBufferFloat32AtomicMinMax', ctypes.c_uint32),
        ('shaderBufferFloat64AtomicMinMax', ctypes.c_uint32),
        ('shaderSharedFloat16Atomics', ctypes.c_uint32),
        ('shaderSharedFloat16AtomicAdd', ctypes.c_uint32),
        ('shaderSharedFloat16AtomicMinMax', ctypes.c_uint32),
        ('shaderSharedFloat32AtomicMinMax', ctypes.c_uint32),
        ('shaderSharedFloat64AtomicMinMax', ctypes.c_uint32),
        ('shaderImageFloat32AtomicMinMax', ctypes.c_uint32),
        ('sparseImageFloat32AtomicMinMax', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkDeviceCreateInfo',
        'VkPhysicalDeviceFeatures2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'shaderBufferFloat16Atomics': 'shader_buffer_float16_atomics',
        'shaderBufferFloat16AtomicAdd': 'shader_buffer_float16_atomic_add',
        'shaderBufferFloat16AtomicMinMax': 'shader_buffer_float16_atomic_min_max',
        'shaderBufferFloat32AtomicMinMax': 'shader_buffer_float32_atomic_min_max',
        'shaderBufferFloat64AtomicMinMax': 'shader_buffer_float64_atomic_min_max',
        'shaderSharedFloat16Atomics': 'shader_shared_float16_atomics',
        'shaderSharedFloat16AtomicAdd': 'shader_shared_float16_atomic_add',
        'shaderSharedFloat16AtomicMinMax': 'shader_shared_float16_atomic_min_max',
        'shaderSharedFloat32AtomicMinMax': 'shader_shared_float32_atomic_min_max',
        'shaderSharedFloat64AtomicMinMax': 'shader_shared_float64_atomic_min_max',
        'shaderImageFloat32AtomicMinMax': 'shader_image_float32_atomic_min_max',
        'sparseImageFloat32AtomicMinMax': 'sparse_image_float32_atomic_min_max',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_shader_atomic_float2',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_ATOMIC_FLOAT_2_FEATURES_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_ATOMIC_FLOAT_2_FEATURES_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceShaderAtomicFloat2FeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderBufferFloat16Atomics': ctypes.c_uint32,
    'shaderBufferFloat16AtomicAdd': ctypes.c_uint32,
    'shaderBufferFloat16AtomicMinMax': ctypes.c_uint32,
    'shaderBufferFloat32AtomicMinMax': ctypes.c_uint32,
    'shaderBufferFloat64AtomicMinMax': ctypes.c_uint32,
    'shaderSharedFloat16Atomics': ctypes.c_uint32,
    'shaderSharedFloat16AtomicAdd': ctypes.c_uint32,
    'shaderSharedFloat16AtomicMinMax': ctypes.c_uint32,
    'shaderSharedFloat32AtomicMinMax': ctypes.c_uint32,
    'shaderSharedFloat64AtomicMinMax': ctypes.c_uint32,
    'shaderImageFloat32AtomicMinMax': ctypes.c_uint32,
    'sparseImageFloat32AtomicMinMax': ctypes.c_uint32,
}
