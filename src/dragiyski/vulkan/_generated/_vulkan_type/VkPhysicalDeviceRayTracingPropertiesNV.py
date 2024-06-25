import ctypes

class VkPhysicalDeviceRayTracingPropertiesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderGroupHandleSize', ctypes.c_uint32),
        ('maxRecursionDepth', ctypes.c_uint32),
        ('maxShaderGroupStride', ctypes.c_uint32),
        ('shaderGroupBaseAlignment', ctypes.c_uint32),
        ('maxGeometryCount', ctypes.c_uint64),
        ('maxInstanceCount', ctypes.c_uint64),
        ('maxTriangleCount', ctypes.c_uint64),
        ('maxDescriptorSetAccelerationStructures', ctypes.c_uint32),
    ]

VkPhysicalDeviceRayTracingPropertiesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderGroupHandleSize': ctypes.c_uint32,
    'maxRecursionDepth': ctypes.c_uint32,
    'maxShaderGroupStride': ctypes.c_uint32,
    'shaderGroupBaseAlignment': ctypes.c_uint32,
    'maxGeometryCount': ctypes.c_uint64,
    'maxInstanceCount': ctypes.c_uint64,
    'maxTriangleCount': ctypes.c_uint64,
    'maxDescriptorSetAccelerationStructures': ctypes.c_uint32,
}
