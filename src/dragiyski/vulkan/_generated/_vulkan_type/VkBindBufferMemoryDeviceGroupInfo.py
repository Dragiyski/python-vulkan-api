import ctypes

class VkBindBufferMemoryDeviceGroupInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('deviceIndexCount', ctypes.c_uint32),
        ('pDeviceIndices', ctypes.POINTER(ctypes.c_uint32)),
    ]

VkBindBufferMemoryDeviceGroupInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'deviceIndexCount': ctypes.c_uint32,
    'pDeviceIndices': ctypes.POINTER(ctypes.c_uint32),
}
