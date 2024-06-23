import ctypes

class CType(ctypes.Structure):
    pass

from .VkRect2D import CType as VkRect2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('discardRectangleMode', ctypes.c_int),
    ('discardRectangleCount', ctypes.c_uint32),
    ('pDiscardRectangles', ctypes.POINTER(VkRect2D)),
]

descriptor = {
    'extends': {
        'VkGraphicsPipelineCreateInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkRect2D',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_DISCARD_RECTANGLE_STATE_CREATE_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkPipelineDiscardRectangleStateCreateFlagsEXT'},
        'discardRectangleMode': {'python_name': ['discard', 'rectangle', 'mode'], 'type': 'VkDiscardRectangleModeEXT'},
        'discardRectangleCount': {'python_name': ['discard', 'rectangle', 'count']},
        'pDiscardRectangles': {'python_name': ['p', 'discard', 'rectangles'], 'len': [['discardRectangleCount']], 'type': 'VkRect2D'},
    }
}
