import ctypes

class CType(ctypes.Structure):
    pass

from .VkVertexInputBindingDivisorDescriptionKHR import CType as VkVertexInputBindingDivisorDescriptionKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('vertexBindingDivisorCount', ctypes.c_uint32),
    ('pVertexBindingDivisors', ctypes.POINTER(VkVertexInputBindingDivisorDescriptionKHR)),
]

descriptor = {
    'extends': {
        'VkPipelineVertexInputStateCreateInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkVertexInputBindingDivisorDescriptionKHR',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_VERTEX_INPUT_DIVISOR_STATE_CREATE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'vertexBindingDivisorCount': {'python_name': ['vertex', 'binding', 'divisor', 'count']},
        'pVertexBindingDivisors': {'python_name': ['p', 'vertex', 'binding', 'divisors'], 'len': [['vertexBindingDivisorCount']], 'type': 'VkVertexInputBindingDivisorDescriptionKHR'},
    }
}
