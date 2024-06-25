import ctypes

class VkWin32KeyedMutexAcquireReleaseInfoNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'acquireCount': ctypes.c_uint32,
            'pAcquireSyncs': ctypes.POINTER(ctypes.c_void_p),
            'pAcquireKeys': ctypes.POINTER(ctypes.c_uint64),
            'pAcquireTimeoutMilliseconds': ctypes.POINTER(ctypes.c_uint32),
            'releaseCount': ctypes.c_uint32,
            'pReleaseSyncs': ctypes.POINTER(ctypes.c_void_p),
            'pReleaseKeys': ctypes.POINTER(ctypes.c_uint64),
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('acquireCount', ctypes.c_uint32),
        ('pAcquireSyncs', ctypes.POINTER(ctypes.c_void_p)),
        ('pAcquireKeys', ctypes.POINTER(ctypes.c_uint64)),
        ('pAcquireTimeoutMilliseconds', ctypes.POINTER(ctypes.c_uint32)),
        ('releaseCount', ctypes.c_uint32),
        ('pReleaseSyncs', ctypes.POINTER(ctypes.c_void_p)),
        ('pReleaseKeys', ctypes.POINTER(ctypes.c_uint64)),
    ]
