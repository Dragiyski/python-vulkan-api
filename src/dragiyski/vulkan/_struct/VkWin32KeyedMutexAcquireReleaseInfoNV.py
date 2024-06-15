import ctypes, sys

class VkWin32KeyedMutexAcquireReleaseInfoNV(ctypes.Structure):
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

sys.modules[__name__] = VkWin32KeyedMutexAcquireReleaseInfoNV
