from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdWaitEvents'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'eventCount', 'pEvents', 'srcStageMask', 'dstStageMask', 'memoryBarrierCount', 'pMemoryBarriers', 'bufferMemoryBarrierCount', 'pBufferMemoryBarriers', 'imageMemoryBarrierCount', 'pImageMemoryBarriers']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'eventCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pEvents': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'length': [['eventCount']],
        'output': False,
    },
    'srcStageMask': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'dstStageMask': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'memoryBarrierCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pMemoryBarriers': {
        'type': CPointerType(CComplexType('VkMemoryBarrier')),
        'is_string': False,
        'length': [['memoryBarrierCount']],
        'output': False,
    },
    'bufferMemoryBarrierCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pBufferMemoryBarriers': {
        'type': CPointerType(CComplexType('VkBufferMemoryBarrier')),
        'is_string': False,
        'length': [['bufferMemoryBarrierCount']],
        'output': False,
    },
    'imageMemoryBarrierCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pImageMemoryBarriers': {
        'type': CPointerType(CComplexType('VkImageMemoryBarrier')),
        'is_string': False,
        'length': [['imageMemoryBarrierCount']],
        'output': False,
    },
}
_return_type_ = CVoidType()
