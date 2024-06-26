import ctypes

class VkBufferCopy(ctypes.Structure):
    _fields_ = [
        ('srcOffset', ctypes.c_uint64),
        ('dstOffset', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCmdCopyBuffer',
    }
    _output_of_ = set()
    _python_name_ = {
        'srcOffset': 'src_offset',
        'dstOffset': 'dst_offset',
        'size': 'size',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkBufferCopy._type_ = {
    'srcOffset': ctypes.c_uint64,
    'dstOffset': ctypes.c_uint64,
    'size': ctypes.c_uint64,
}
