import ctypes

class CType(ctypes.Structure):
    pass

from .VkRect2D import CType as VkRect2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('perViewRenderAreaCount', ctypes.c_uint32),
    ('pPerViewRenderAreas', ctypes.POINTER(VkRect2D)),
]

descriptor = {
    'extends': {
        'VkRenderPassBeginInfo',
        'VkRenderingInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkRect2D',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_MULTIVIEW_PER_VIEW_RENDER_AREAS_RENDER_PASS_BEGIN_INFO_QCOM', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'perViewRenderAreaCount': {'python_name': ['per', 'view', 'render', 'area', 'count']},
        'pPerViewRenderAreas': {'python_name': ['p', 'per', 'view', 'render', 'areas'], 'len': [['perViewRenderAreaCount']], 'type': 'VkRect2D'},
    }
}
