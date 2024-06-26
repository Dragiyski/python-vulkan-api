import ctypes

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

    _init_ = []
    _extends_ = {
        'VkSubmitInfo',
        'VkSubmitInfo2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'acquireCount': 'acquire_count',
        'pAcquireSyncs': 'acquire_syncs',
        'pAcquireKeys': 'acquire_keys',
        'pAcquireTimeoutMilliseconds': 'acquire_timeout_milliseconds',
        'releaseCount': 'release_count',
        'pReleaseSyncs': 'release_syncs',
        'pReleaseKeys': 'release_keys',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_win32_keyed_mutex',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_WIN32_KEYED_MUTEX_ACQUIRE_RELEASE_INFO_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_WIN32_KEYED_MUTEX_ACQUIRE_RELEASE_INFO_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkWin32KeyedMutexAcquireReleaseInfoNV._type_ = {
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
