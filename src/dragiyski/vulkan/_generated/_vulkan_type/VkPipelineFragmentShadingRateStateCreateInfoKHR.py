import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('fragmentSize', VkExtent2D),
    ('combinerOps', ctypes.ARRAY(ctypes.c_int, 2)),
]

descriptor = {
    'extends': {
        'VkGraphicsPipelineCreateInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkExtent2D',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_FRAGMENT_SHADING_RATE_STATE_CREATE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'fragmentSize': {'python_name': ['fragment', 'size'], 'type': 'VkExtent2D'},
        'combinerOps': {'python_name': ['combiner', 'ops'], 'type': 'VkFragmentShadingRateCombinerOpKHR'},
    }
}
