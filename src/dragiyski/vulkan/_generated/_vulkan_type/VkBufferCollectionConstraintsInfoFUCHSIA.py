import ctypes

class VkBufferCollectionConstraintsInfoFUCHSIA(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'minBufferCount': ctypes.c_uint32,
            'maxBufferCount': ctypes.c_uint32,
            'minBufferCountForCamping': ctypes.c_uint32,
            'minBufferCountForDedicatedSlack': ctypes.c_uint32,
            'minBufferCountForSharedSlack': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('minBufferCount', ctypes.c_uint32),
        ('maxBufferCount', ctypes.c_uint32),
        ('minBufferCountForCamping', ctypes.c_uint32),
        ('minBufferCountForDedicatedSlack', ctypes.c_uint32),
        ('minBufferCountForSharedSlack', ctypes.c_uint32),
    ]
