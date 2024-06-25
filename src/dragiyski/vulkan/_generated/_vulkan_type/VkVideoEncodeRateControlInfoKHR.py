import ctypes

class VkVideoEncodeRateControlInfoKHR(ctypes.Structure):
    pass

from .VkVideoEncodeRateControlLayerInfoKHR import VkVideoEncodeRateControlLayerInfoKHR

VkVideoEncodeRateControlInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('rateControlMode', ctypes.c_uint32),
    ('layerCount', ctypes.c_uint32),
    ('pLayers', ctypes.POINTER(VkVideoEncodeRateControlLayerInfoKHR)),
    ('virtualBufferSizeInMs', ctypes.c_uint32),
    ('initialVirtualBufferSizeInMs', ctypes.c_uint32),
]

VkVideoEncodeRateControlInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'rateControlMode': ctypes.c_uint32,
    'layerCount': ctypes.c_uint32,
    'pLayers': ctypes.POINTER(VkVideoEncodeRateControlLayerInfoKHR),
    'virtualBufferSizeInMs': ctypes.c_uint32,
    'initialVirtualBufferSizeInMs': ctypes.c_uint32,
}
