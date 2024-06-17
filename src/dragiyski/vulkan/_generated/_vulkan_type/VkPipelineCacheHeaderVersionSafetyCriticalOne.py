import ctypes, sys

class VkPipelineCacheHeaderVersionSafetyCriticalOne(ctypes.Structure):
    pass

sys.modules[__name__] = VkPipelineCacheHeaderVersionSafetyCriticalOne

from . import VkPipelineCacheHeaderVersionOne

VkPipelineCacheHeaderVersionSafetyCriticalOne._fields_ = [
    ('headerVersionOne', VkPipelineCacheHeaderVersionOne),
    ('validationVersion', ctypes.c_int),
    ('implementationData', ctypes.c_uint32),
    ('pipelineIndexCount', ctypes.c_uint32),
    ('pipelineIndexStride', ctypes.c_uint32),
    ('pipelineIndexOffset', ctypes.c_uint64),
]
