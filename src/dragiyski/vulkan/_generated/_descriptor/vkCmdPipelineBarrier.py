from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdPipelineBarrier'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'srcStageMask', 'dstStageMask', 'dependencyFlags', 'memoryBarrierCount', 'pMemoryBarriers', 'bufferMemoryBarrierCount', 'pBufferMemoryBarriers', 'imageMemoryBarrierCount', 'pImageMemoryBarriers']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'srcStageMask': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'dstStageMask': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'dependencyFlags': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'memoryBarrierCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pMemoryBarriers': {
        'type': CPointerType(CComplexType('VkMemoryBarrier')),
        'is_string': False,
        'length': [['memoryBarrierCount']],
    },
    'bufferMemoryBarrierCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pBufferMemoryBarriers': {
        'type': CPointerType(CComplexType('VkBufferMemoryBarrier')),
        'is_string': False,
        'length': [['bufferMemoryBarrierCount']],
    },
    'imageMemoryBarrierCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pImageMemoryBarriers': {
        'type': CPointerType(CComplexType('VkImageMemoryBarrier')),
        'is_string': False,
        'length': [['imageMemoryBarrierCount']],
    },
}
_return_type_ = CVoidType()
