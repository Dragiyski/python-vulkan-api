import ctypes

class CType(ctypes.Structure):
    pass

from .VkCoarseSampleOrderCustomNV import CType as VkCoarseSampleOrderCustomNV

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('sampleOrderType', ctypes.c_int),
    ('customSampleOrderCount', ctypes.c_uint32),
    ('pCustomSampleOrders', ctypes.POINTER(VkCoarseSampleOrderCustomNV)),
]

descriptor = {
    'extends': {
        'VkPipelineViewportStateCreateInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkCoarseSampleOrderCustomNV',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_COARSE_SAMPLE_ORDER_STATE_CREATE_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'sampleOrderType': {'python_name': ['sample', 'order', 'type'], 'type': 'VkCoarseSampleOrderTypeNV'},
        'customSampleOrderCount': {'python_name': ['custom', 'sample', 'order', 'count']},
        'pCustomSampleOrders': {'python_name': ['p', 'custom', 'sample', 'orders'], 'len': [['customSampleOrderCount']], 'type': 'VkCoarseSampleOrderCustomNV'},
    }
}
