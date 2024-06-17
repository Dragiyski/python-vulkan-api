import ctypes, sys

class VkDeviceFaultVendorBinaryHeaderVersionOneEXT(ctypes.Structure):
    _fields_ = [
        ('headerSize', ctypes.c_uint32),
        ('headerVersion', ctypes.c_int),
        ('vendorID', ctypes.c_uint32),
        ('deviceID', ctypes.c_uint32),
        ('driverVersion', ctypes.c_uint32),
        ('pipelineCacheUUID', ctypes.ARRAY(ctypes.c_uint8, 16)),
        ('applicationNameOffset', ctypes.c_uint32),
        ('applicationVersion', ctypes.c_uint32),
        ('engineNameOffset', ctypes.c_uint32),
        ('engineVersion', ctypes.c_uint32),
        ('apiVersion', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkDeviceFaultVendorBinaryHeaderVersionOneEXT
