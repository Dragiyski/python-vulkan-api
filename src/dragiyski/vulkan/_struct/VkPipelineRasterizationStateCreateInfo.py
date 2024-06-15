import ctypes, sys

class VkPipelineRasterizationStateCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('depthClampEnable', ctypes.c_uint32),
        ('rasterizerDiscardEnable', ctypes.c_uint32),
        ('polygonMode', ctypes.c_int),
        ('cullMode', ctypes.c_uint32),
        ('frontFace', ctypes.c_int),
        ('depthBiasEnable', ctypes.c_uint32),
        ('depthBiasConstantFactor', ctypes.c_float),
        ('depthBiasClamp', ctypes.c_float),
        ('depthBiasSlopeFactor', ctypes.c_float),
        ('lineWidth', ctypes.c_float),
    ]

sys.modules[__name__] = VkPipelineRasterizationStateCreateInfo
