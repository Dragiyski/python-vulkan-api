import ctypes

class CType(ctypes.Structure):
    pass

from .VkRect2D import CType as VkRect2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('transform', ctypes.c_uint32),
    ('renderArea', VkRect2D),
]

descriptor = {
    'extends': {
        'VkCommandBufferInheritanceInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkRect2D',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_COMMAND_BUFFER_INHERITANCE_RENDER_PASS_TRANSFORM_INFO_QCOM', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'transform': {'python_name': ['transform'], 'type': 'VkSurfaceTransformFlagBitsKHR'},
        'renderArea': {'python_name': ['render', 'area'], 'type': 'VkRect2D'},
    }
}
