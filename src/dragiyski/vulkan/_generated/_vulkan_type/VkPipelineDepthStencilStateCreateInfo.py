import ctypes

class CType(ctypes.Structure):
    pass

from .VkStencilOpState import CType as VkStencilOpState

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('depthTestEnable', ctypes.c_uint32),
    ('depthWriteEnable', ctypes.c_uint32),
    ('depthCompareOp', ctypes.c_int),
    ('depthBoundsTestEnable', ctypes.c_uint32),
    ('stencilTestEnable', ctypes.c_uint32),
    ('front', VkStencilOpState),
    ('back', VkStencilOpState),
    ('minDepthBounds', ctypes.c_float),
    ('maxDepthBounds', ctypes.c_float),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkStencilOpState',
    },
    'included_in': {
        'VkGraphicsPipelineCreateInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_DEPTH_STENCIL_STATE_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkPipelineDepthStencilStateCreateFlags'},
        'depthTestEnable': {'python_name': ['depth', 'test', 'enable']},
        'depthWriteEnable': {'python_name': ['depth', 'write', 'enable']},
        'depthCompareOp': {'python_name': ['depth', 'compare', 'op'], 'type': 'VkCompareOp'},
        'depthBoundsTestEnable': {'python_name': ['depth', 'bounds', 'test', 'enable']},
        'stencilTestEnable': {'python_name': ['stencil', 'test', 'enable']},
        'front': {'python_name': ['front'], 'type': 'VkStencilOpState'},
        'back': {'python_name': ['back'], 'type': 'VkStencilOpState'},
        'minDepthBounds': {'python_name': ['min', 'depth', 'bounds']},
        'maxDepthBounds': {'python_name': ['max', 'depth', 'bounds']},
    }
}
