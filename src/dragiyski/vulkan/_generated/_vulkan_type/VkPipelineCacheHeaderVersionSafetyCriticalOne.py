import ctypes

class VkPipelineCacheHeaderVersionSafetyCriticalOne(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'headerVersionOne': VkPipelineCacheHeaderVersionOne,
            'validationVersion': ctypes.c_int,
            'implementationData': ctypes.c_uint32,
            'pipelineIndexCount': ctypes.c_uint32,
            'pipelineIndexStride': ctypes.c_uint32,
            'pipelineIndexOffset': ctypes.c_uint64,
        }


from .VkPipelineCacheHeaderVersionOne import VkPipelineCacheHeaderVersionOne

VkPipelineCacheHeaderVersionSafetyCriticalOne._fields_ = [
    ('headerVersionOne', VkPipelineCacheHeaderVersionOne),
    ('validationVersion', ctypes.c_int),
    ('implementationData', ctypes.c_uint32),
    ('pipelineIndexCount', ctypes.c_uint32),
    ('pipelineIndexStride', ctypes.c_uint32),
    ('pipelineIndexOffset', ctypes.c_uint64),
]
