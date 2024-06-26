import ctypes

class VkPhysicalDeviceShaderAtomicFloatFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderBufferFloat32Atomics', ctypes.c_uint32),
        ('shaderBufferFloat32AtomicAdd', ctypes.c_uint32),
        ('shaderBufferFloat64Atomics', ctypes.c_uint32),
        ('shaderBufferFloat64AtomicAdd', ctypes.c_uint32),
        ('shaderSharedFloat32Atomics', ctypes.c_uint32),
        ('shaderSharedFloat32AtomicAdd', ctypes.c_uint32),
        ('shaderSharedFloat64Atomics', ctypes.c_uint32),
        ('shaderSharedFloat64AtomicAdd', ctypes.c_uint32),
        ('shaderImageFloat32Atomics', ctypes.c_uint32),
        ('shaderImageFloat32AtomicAdd', ctypes.c_uint32),
        ('sparseImageFloat32Atomics', ctypes.c_uint32),
        ('sparseImageFloat32AtomicAdd', ctypes.c_uint32),
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
        'shaderBufferFloat32Atomics': 'shader_buffer_float32_atomics',
        'shaderBufferFloat32AtomicAdd': 'shader_buffer_float32_atomic_add',
        'shaderBufferFloat64Atomics': 'shader_buffer_float64_atomics',
        'shaderBufferFloat64AtomicAdd': 'shader_buffer_float64_atomic_add',
        'shaderSharedFloat32Atomics': 'shader_shared_float32_atomics',
        'shaderSharedFloat32AtomicAdd': 'shader_shared_float32_atomic_add',
        'shaderSharedFloat64Atomics': 'shader_shared_float64_atomics',
        'shaderSharedFloat64AtomicAdd': 'shader_shared_float64_atomic_add',
        'shaderImageFloat32Atomics': 'shader_image_float32_atomics',
        'shaderImageFloat32AtomicAdd': 'shader_image_float32_atomic_add',
        'sparseImageFloat32Atomics': 'sparse_image_float32_atomics',
        'sparseImageFloat32AtomicAdd': 'sparse_image_float32_atomic_add',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_shader_atomic_float',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_ATOMIC_FLOAT_FEATURES_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_ATOMIC_FLOAT_FEATURES_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceShaderAtomicFloatFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderBufferFloat32Atomics': ctypes.c_uint32,
    'shaderBufferFloat32AtomicAdd': ctypes.c_uint32,
    'shaderBufferFloat64Atomics': ctypes.c_uint32,
    'shaderBufferFloat64AtomicAdd': ctypes.c_uint32,
    'shaderSharedFloat32Atomics': ctypes.c_uint32,
    'shaderSharedFloat32AtomicAdd': ctypes.c_uint32,
    'shaderSharedFloat64Atomics': ctypes.c_uint32,
    'shaderSharedFloat64AtomicAdd': ctypes.c_uint32,
    'shaderImageFloat32Atomics': ctypes.c_uint32,
    'shaderImageFloat32AtomicAdd': ctypes.c_uint32,
    'sparseImageFloat32Atomics': ctypes.c_uint32,
    'sparseImageFloat32AtomicAdd': ctypes.c_uint32,
}
