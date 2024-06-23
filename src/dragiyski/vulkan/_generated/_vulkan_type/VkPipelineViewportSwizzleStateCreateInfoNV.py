import ctypes

class CType(ctypes.Structure):
    pass

from .VkViewportSwizzleNV import CType as VkViewportSwizzleNV

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('viewportCount', ctypes.c_uint32),
    ('pViewportSwizzles', ctypes.POINTER(VkViewportSwizzleNV)),
]

descriptor = {
    'extends': {
        'VkPipelineViewportStateCreateInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkViewportSwizzleNV',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_SWIZZLE_STATE_CREATE_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkPipelineViewportSwizzleStateCreateFlagsNV'},
        'viewportCount': {'python_name': ['viewport', 'count']},
        'pViewportSwizzles': {'python_name': ['p', 'viewport', 'swizzles'], 'len': [['viewportCount']], 'type': 'VkViewportSwizzleNV'},
    }
}
