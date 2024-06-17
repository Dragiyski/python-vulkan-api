import ctypes, sys

class VkRayTracingShaderGroupCreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('type', ctypes.c_int),
        ('generalShader', ctypes.c_uint32),
        ('closestHitShader', ctypes.c_uint32),
        ('anyHitShader', ctypes.c_uint32),
        ('intersectionShader', ctypes.c_uint32),
        ('pShaderGroupCaptureReplayHandle', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkRayTracingShaderGroupCreateInfoKHR
