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
