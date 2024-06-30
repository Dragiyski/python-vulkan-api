from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDependencyInfo'
_member_list_ = ['sType', 'pNext', 'dependencyFlags', 'memoryBarrierCount', 'pMemoryBarriers', 'bufferMemoryBarrierCount', 'pBufferMemoryBarriers', 'imageMemoryBarrierCount', 'pImageMemoryBarriers']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DEPENDENCY_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'dependencyFlags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkDependencyFlags',
        'enum': 'VkDependencyFlags',
        'is_string': False,
    },
    'memoryBarrierCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pMemoryBarriers': {
        'type': CPointerType(CComplexType('VkMemoryBarrier2')),
        'type_name': 'VkMemoryBarrier2',
        'structure': 'VkMemoryBarrier2',
        'length': [['memoryBarrierCount']],
        'is_string': False,
    },
    'bufferMemoryBarrierCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pBufferMemoryBarriers': {
        'type': CPointerType(CComplexType('VkBufferMemoryBarrier2')),
        'type_name': 'VkBufferMemoryBarrier2',
        'structure': 'VkBufferMemoryBarrier2',
        'length': [['bufferMemoryBarrierCount']],
        'is_string': False,
    },
    'imageMemoryBarrierCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pImageMemoryBarriers': {
        'type': CPointerType(CComplexType('VkImageMemoryBarrier2')),
        'type_name': 'VkImageMemoryBarrier2',
        'structure': 'VkImageMemoryBarrier2',
        'length': [['imageMemoryBarrierCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkBufferMemoryBarrier2',
    'VkImageMemoryBarrier2',
    'VkMemoryBarrier2',
}
_included_in_ = set()
_input_of_ = {
    'vkCmdPipelineBarrier2',
    'vkCmdSetEvent2',
    'vkCmdWaitEvents2',
}
_output_of_ = set()
