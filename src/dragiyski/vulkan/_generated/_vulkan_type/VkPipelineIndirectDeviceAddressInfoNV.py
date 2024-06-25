import ctypes

class VkPipelineIndirectDeviceAddressInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pipelineBindPoint', ctypes.c_int),
        ('pipeline', ctypes.c_void_p),
    ]

VkPipelineIndirectDeviceAddressInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pipelineBindPoint': ctypes.c_int,
    'pipeline': ctypes.c_void_p,
}
