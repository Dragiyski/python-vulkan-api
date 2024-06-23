import ctypes

class CType(ctypes.Structure):
    pass

from .VkViewportWScalingNV import CType as VkViewportWScalingNV

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('viewportWScalingEnable', ctypes.c_uint32),
    ('viewportCount', ctypes.c_uint32),
    ('pViewportWScalings', ctypes.POINTER(VkViewportWScalingNV)),
]

descriptor = {
    'extends': {
        'VkPipelineViewportStateCreateInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkViewportWScalingNV',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_W_SCALING_STATE_CREATE_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'viewportWScalingEnable': {'python_name': ['viewport', 'wscaling', 'enable']},
        'viewportCount': {'python_name': ['viewport', 'count']},
        'pViewportWScalings': {'python_name': ['p', 'viewport', 'wscalings'], 'len': [['viewportCount']], 'type': 'VkViewportWScalingNV'},
    }
}
