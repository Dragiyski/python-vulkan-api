import ctypes

class VkPipelineCacheSafetyCriticalIndexEntry(ctypes.Structure):
    _fields_ = [
        ('pipelineIdentifier', ctypes.ARRAY(ctypes.c_uint8, 16)),
        ('pipelineMemorySize', ctypes.c_uint64),
        ('jsonSize', ctypes.c_uint64),
        ('jsonOffset', ctypes.c_uint64),
        ('stageIndexCount', ctypes.c_uint32),
        ('stageIndexStride', ctypes.c_uint32),
        ('stageIndexOffset', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'pipelineIdentifier': 'pipeline_identifier',
        'pipelineMemorySize': 'pipeline_memory_size',
        'jsonSize': 'json_size',
        'jsonOffset': 'json_offset',
        'stageIndexCount': 'stage_index_count',
        'stageIndexStride': 'stage_index_stride',
        'stageIndexOffset': 'stage_index_offset',
    }
    _vk_versions_ = set()
    _vk_extensions_ = set()
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkPipelineCacheSafetyCriticalIndexEntry._type_ = {
    'pipelineIdentifier': ctypes.ARRAY(ctypes.c_uint8, 16),
    'pipelineMemorySize': ctypes.c_uint64,
    'jsonSize': ctypes.c_uint64,
    'jsonOffset': ctypes.c_uint64,
    'stageIndexCount': ctypes.c_uint32,
    'stageIndexStride': ctypes.c_uint32,
    'stageIndexOffset': ctypes.c_uint64,
}
