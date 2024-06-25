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
