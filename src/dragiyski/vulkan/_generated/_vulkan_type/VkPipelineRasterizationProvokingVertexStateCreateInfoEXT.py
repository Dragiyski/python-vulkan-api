import ctypes

class VkPipelineRasterizationProvokingVertexStateCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('provokingVertexMode', ctypes.c_int),
    ]

VkPipelineRasterizationProvokingVertexStateCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'provokingVertexMode': ctypes.c_int,
}
