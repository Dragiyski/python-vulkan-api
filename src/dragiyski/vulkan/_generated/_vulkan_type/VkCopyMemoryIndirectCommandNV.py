import ctypes

class VkCopyMemoryIndirectCommandNV(ctypes.Structure):
    _fields_ = [
        ('srcAddress', ctypes.c_uint64),
        ('dstAddress', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'srcAddress': 'src_address',
        'dstAddress': 'dst_address',
        'size': 'size',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_copy_memory_indirect',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkCopyMemoryIndirectCommandNV._type_ = {
    'srcAddress': ctypes.c_uint64,
    'dstAddress': ctypes.c_uint64,
    'size': ctypes.c_uint64,
}
