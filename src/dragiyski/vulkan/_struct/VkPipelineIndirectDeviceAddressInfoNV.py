import ctypes, sys

class VkPipelineIndirectDeviceAddressInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pipelineBindPoint', ctypes.c_int),
        ('pipeline', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkPipelineIndirectDeviceAddressInfoNV
