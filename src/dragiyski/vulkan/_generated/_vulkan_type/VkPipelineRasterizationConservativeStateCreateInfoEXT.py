import ctypes

class VkPipelineRasterizationConservativeStateCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('conservativeRasterizationMode', ctypes.c_int),
        ('extraPrimitiveOverestimationSize', ctypes.c_float),
    ]

VkPipelineRasterizationConservativeStateCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'conservativeRasterizationMode': ctypes.c_int,
    'extraPrimitiveOverestimationSize': ctypes.c_float,
}
