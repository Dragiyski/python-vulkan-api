import ctypes

class CType(ctypes.Structure):
    pass

from .VkViewport import CType as VkViewport

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('viewportScissor2D', ctypes.c_uint32),
    ('viewportDepthCount', ctypes.c_uint32),
    ('pViewportDepths', ctypes.POINTER(VkViewport)),
]

descriptor = {
    'extends': {
        'VkCommandBufferInheritanceInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkViewport',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_COMMAND_BUFFER_INHERITANCE_VIEWPORT_SCISSOR_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'viewportScissor2D': {'python_name': ['viewport', 'scissor2', 'd']},
        'viewportDepthCount': {'python_name': ['viewport', 'depth', 'count']},
        'pViewportDepths': {'python_name': ['p', 'viewport', 'depths'], 'type': 'VkViewport'},
    }
}
