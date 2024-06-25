import ctypes

class VkRayTracingPipelineInterfaceCreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxPipelineRayPayloadSize', ctypes.c_uint32),
        ('maxPipelineRayHitAttributeSize', ctypes.c_uint32),
    ]

VkRayTracingPipelineInterfaceCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxPipelineRayPayloadSize': ctypes.c_uint32,
    'maxPipelineRayHitAttributeSize': ctypes.c_uint32,
}
