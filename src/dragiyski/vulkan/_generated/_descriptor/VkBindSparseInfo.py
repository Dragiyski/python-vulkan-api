from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkBindSparseInfo'
_member_list_ = ['sType', 'pNext', 'waitSemaphoreCount', 'pWaitSemaphores', 'bufferBindCount', 'pBufferBinds', 'imageOpaqueBindCount', 'pImageOpaqueBinds', 'imageBindCount', 'pImageBinds', 'signalSemaphoreCount', 'pSignalSemaphores']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_BIND_SPARSE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'waitSemaphoreCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pWaitSemaphores': {
        'type': CPointerType(CIntType('c_void_p')),
        'length': [['waitSemaphoreCount']],
        'is_string': False,
    },
    'bufferBindCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pBufferBinds': {
        'type': CPointerType(CComplexType('VkSparseBufferMemoryBindInfo')),
        'type_name': 'VkSparseBufferMemoryBindInfo',
        'structure': 'VkSparseBufferMemoryBindInfo',
        'length': [['bufferBindCount']],
        'is_string': False,
    },
    'imageOpaqueBindCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pImageOpaqueBinds': {
        'type': CPointerType(CComplexType('VkSparseImageOpaqueMemoryBindInfo')),
        'type_name': 'VkSparseImageOpaqueMemoryBindInfo',
        'structure': 'VkSparseImageOpaqueMemoryBindInfo',
        'length': [['imageOpaqueBindCount']],
        'is_string': False,
    },
    'imageBindCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pImageBinds': {
        'type': CPointerType(CComplexType('VkSparseImageMemoryBindInfo')),
        'type_name': 'VkSparseImageMemoryBindInfo',
        'structure': 'VkSparseImageMemoryBindInfo',
        'length': [['imageBindCount']],
        'is_string': False,
    },
    'signalSemaphoreCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pSignalSemaphores': {
        'type': CPointerType(CIntType('c_void_p')),
        'length': [['signalSemaphoreCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkDeviceGroupBindSparseInfo',
    'VkFrameBoundaryEXT',
    'VkTimelineSemaphoreSubmitInfo',
}
_includes_ = {
    'VkSparseBufferMemoryBindInfo',
    'VkSparseImageMemoryBindInfo',
    'VkSparseImageOpaqueMemoryBindInfo',
}
_included_in_ = set()
_input_of_ = {
    'vkQueueBindSparse',
}
_output_of_ = set()
