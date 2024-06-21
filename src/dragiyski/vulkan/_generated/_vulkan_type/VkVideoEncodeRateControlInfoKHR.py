import ctypes

class CType(ctypes.Structure):
    pass

from .VkVideoEncodeRateControlLayerInfoKHR import CType as VkVideoEncodeRateControlLayerInfoKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('rateControlMode', ctypes.c_uint32),
    ('layerCount', ctypes.c_uint32),
    ('pLayers', ctypes.POINTER(VkVideoEncodeRateControlLayerInfoKHR)),
    ('virtualBufferSizeInMs', ctypes.c_uint32),
    ('initialVirtualBufferSizeInMs', ctypes.c_uint32),
]
