import ctypes

class CType(ctypes.Structure):
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

descriptor = {
    'extends': {
        'VkSubmitInfo',
        'VkSubmitInfo2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_WIN32_KEYED_MUTEX_ACQUIRE_RELEASE_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'acquireCount': {'python_name': ['acquire', 'count']},
        'pAcquireSyncs': {'python_name': ['p', 'acquire', 'syncs'], 'len': [['acquireCount']]},
        'pAcquireKeys': {'python_name': ['p', 'acquire', 'keys'], 'len': [['acquireCount']]},
        'pAcquireTimeoutMilliseconds': {'python_name': ['p', 'acquire', 'timeout', 'milliseconds'], 'len': [['acquireCount']]},
        'releaseCount': {'python_name': ['release', 'count']},
        'pReleaseSyncs': {'python_name': ['p', 'release', 'syncs'], 'len': [['releaseCount']]},
        'pReleaseKeys': {'python_name': ['p', 'release', 'keys'], 'len': [['releaseCount']]},
    }
}
