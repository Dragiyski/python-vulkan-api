import ctypes

class VkPipelineCacheStageValidationIndexEntry(ctypes.Structure):
    _fields_ = [
        ('codeSize', ctypes.c_uint64),
        ('codeOffset', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'codeSize': 'code_size',
        'codeOffset': 'code_offset',
    }
    _vk_versions_ = set()
    _vk_extensions_ = set()
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkPipelineCacheStageValidationIndexEntry._type_ = {
    'codeSize': ctypes.c_uint64,
    'codeOffset': ctypes.c_uint64,
}
