import ctypes

class VkPipelineRasterizationStateRasterizationOrderAMD(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('rasterizationOrder', ctypes.c_int),
    ]

VkPipelineRasterizationStateRasterizationOrderAMD._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'rasterizationOrder': ctypes.c_int,
}
