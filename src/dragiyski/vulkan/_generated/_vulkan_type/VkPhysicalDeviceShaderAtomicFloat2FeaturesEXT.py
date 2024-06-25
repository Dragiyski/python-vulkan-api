import ctypes

class VkPhysicalDeviceShaderAtomicFloat2FeaturesEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
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
