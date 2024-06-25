import ctypes

class VkWin32KeyedMutexAcquireReleaseInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('acquireCount', ctypes.c_uint32),
        ('pAcquireSyncs', ctypes.POINTER(ctypes.c_void_p)),
        ('pAcquireKeys', ctypes.POINTER(ctypes.c_uint64)),
        ('pAcquireTimeouts', ctypes.POINTER(ctypes.c_uint32)),
        ('releaseCount', ctypes.c_uint32),
        ('pReleaseSyncs', ctypes.POINTER(ctypes.c_void_p)),
        ('pReleaseKeys', ctypes.POINTER(ctypes.c_uint64)),
    ]

VkWin32KeyedMutexAcquireReleaseInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'acquireCount': ctypes.c_uint32,
    'pAcquireSyncs': ctypes.POINTER(ctypes.c_void_p),
    'pAcquireKeys': ctypes.POINTER(ctypes.c_uint64),
    'pAcquireTimeouts': ctypes.POINTER(ctypes.c_uint32),
    'releaseCount': ctypes.c_uint32,
    'pReleaseSyncs': ctypes.POINTER(ctypes.c_void_p),
    'pReleaseKeys': ctypes.POINTER(ctypes.c_uint64),
}
