import ctypes

class VkPipelineOfflineCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pipelineIdentifier', ctypes.ARRAY(ctypes.c_uint8, 16)),
        ('matchControl', ctypes.c_int),
        ('poolEntrySize', ctypes.c_uint64),
    ]

VkPipelineOfflineCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pipelineIdentifier': ctypes.ARRAY(ctypes.c_uint8, 16),
    'matchControl': ctypes.c_int,
    'poolEntrySize': ctypes.c_uint64,
}
