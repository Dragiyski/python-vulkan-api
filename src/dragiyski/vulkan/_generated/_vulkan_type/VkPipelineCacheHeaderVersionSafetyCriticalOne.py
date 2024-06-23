import ctypes

class CType(ctypes.Structure):
    pass

from .VkPipelineCacheHeaderVersionOne import CType as VkPipelineCacheHeaderVersionOne

CType._fields_ = [
    ('headerVersionOne', VkPipelineCacheHeaderVersionOne),
    ('validationVersion', ctypes.c_int),
    ('implementationData', ctypes.c_uint32),
    ('pipelineIndexCount', ctypes.c_uint32),
    ('pipelineIndexStride', ctypes.c_uint32),
    ('pipelineIndexOffset', ctypes.c_uint64),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkPipelineCacheHeaderVersionOne',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'headerVersionOne': {'python_name': ['header', 'version', 'one'], 'type': 'VkPipelineCacheHeaderVersionOne'},
        'validationVersion': {'python_name': ['validation', 'version'], 'type': 'VkPipelineCacheValidationVersion'},
        'implementationData': {'python_name': ['implementation', 'data']},
        'pipelineIndexCount': {'python_name': ['pipeline', 'index', 'count']},
        'pipelineIndexStride': {'python_name': ['pipeline', 'index', 'stride']},
        'pipelineIndexOffset': {'python_name': ['pipeline', 'index', 'offset']},
    }
}
