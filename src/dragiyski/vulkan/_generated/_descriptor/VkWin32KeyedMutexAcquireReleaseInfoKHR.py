from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkWin32KeyedMutexAcquireReleaseInfoKHR'
_member_list_ = ['sType', 'pNext', 'acquireCount', 'pAcquireSyncs', 'pAcquireKeys', 'pAcquireTimeouts', 'releaseCount', 'pReleaseSyncs', 'pReleaseKeys']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_WIN32_KEYED_MUTEX_ACQUIRE_RELEASE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'acquireCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pAcquireSyncs': {
        'type': CPointerType(CIntType('c_void_p')),
        'length': [['acquireCount']],
        'is_string': False,
    },
    'pAcquireKeys': {
        'type': CPointerType(CIntType('c_uint64')),
        'length': [['acquireCount']],
        'is_string': False,
    },
    'pAcquireTimeouts': {
        'type': CPointerType(CIntType('c_uint32')),
        'length': [['acquireCount']],
        'is_string': False,
    },
    'releaseCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pReleaseSyncs': {
        'type': CPointerType(CIntType('c_void_p')),
        'length': [['releaseCount']],
        'is_string': False,
    },
    'pReleaseKeys': {
        'type': CPointerType(CIntType('c_uint64')),
        'length': [['releaseCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkSubmitInfo',
    'VkSubmitInfo2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
