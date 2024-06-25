import ctypes

class VkComputePipelineIndirectBufferInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('deviceAddress', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
        ('pipelineDeviceAddressCaptureReplay', ctypes.c_uint64),
    ]

VkComputePipelineIndirectBufferInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'deviceAddress': ctypes.c_uint64,
    'size': ctypes.c_uint64,
    'pipelineDeviceAddressCaptureReplay': ctypes.c_uint64,
}
