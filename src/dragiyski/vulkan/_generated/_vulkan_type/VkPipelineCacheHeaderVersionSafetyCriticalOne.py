import ctypes

class VkPipelineCacheHeaderVersionSafetyCriticalOne(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkPipelineCacheHeaderVersionOne',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'headerVersionOne': 'header_version_one',
        'validationVersion': 'validation_version',
        'implementationData': 'implementation_data',
        'pipelineIndexCount': 'pipeline_index_count',
        'pipelineIndexStride': 'pipeline_index_stride',
        'pipelineIndexOffset': 'pipeline_index_offset',
    }
    _vk_versions_ = set()
    _vk_extensions_ = set()
    _vk_enum_ = {
        'validationVersion': 'VkPipelineCacheValidationVersion',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkPipelineCacheHeaderVersionOne import VkPipelineCacheHeaderVersionOne

VkPipelineCacheHeaderVersionSafetyCriticalOne._fields_ = [
    ('headerVersionOne', VkPipelineCacheHeaderVersionOne),
    ('validationVersion', ctypes.c_int),
    ('implementationData', ctypes.c_uint32),
    ('pipelineIndexCount', ctypes.c_uint32),
    ('pipelineIndexStride', ctypes.c_uint32),
    ('pipelineIndexOffset', ctypes.c_uint64),
]

VkPipelineCacheHeaderVersionSafetyCriticalOne._type_ = {
    'headerVersionOne': VkPipelineCacheHeaderVersionOne,
    'validationVersion': ctypes.c_int,
    'implementationData': ctypes.c_uint32,
    'pipelineIndexCount': ctypes.c_uint32,
    'pipelineIndexStride': ctypes.c_uint32,
    'pipelineIndexOffset': ctypes.c_uint64,
}
