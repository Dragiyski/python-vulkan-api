import ctypes

class VkPipelineCacheHeaderVersionOne(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'headerSize': ctypes.c_uint32,
            'headerVersion': ctypes.c_int,
            'vendorID': ctypes.c_uint32,
            'deviceID': ctypes.c_uint32,
            'pipelineCacheUUID': ctypes.ARRAY(ctypes.c_uint8, 16),
        }

    _fields_ = [
        ('headerSize', ctypes.c_uint32),
        ('headerVersion', ctypes.c_int),
        ('vendorID', ctypes.c_uint32),
        ('deviceID', ctypes.c_uint32),
        ('pipelineCacheUUID', ctypes.ARRAY(ctypes.c_uint8, 16)),
    ]
