import ctypes

class VkPhysicalDeviceRayTracingMotionBlurFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('rayTracingMotionBlur', ctypes.c_uint32),
        ('rayTracingMotionBlurPipelineTraceRaysIndirect', ctypes.c_uint32),
    ]

VkPhysicalDeviceRayTracingMotionBlurFeaturesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'rayTracingMotionBlur': ctypes.c_uint32,
    'rayTracingMotionBlurPipelineTraceRaysIndirect': ctypes.c_uint32,
}
