import ctypes

class VkSparseImageMemoryBindInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkSparseImageMemoryBind',
    }
    _included_in_ = {
        'VkBindSparseInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'image': 'image',
        'bindCount': 'bind_count',
        'pBinds': 'binds',
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


from .VkSparseImageMemoryBind import VkSparseImageMemoryBind

VkSparseImageMemoryBindInfo._fields_ = [
    ('image', ctypes.c_void_p),
    ('bindCount', ctypes.c_uint32),
    ('pBinds', ctypes.POINTER(VkSparseImageMemoryBind)),
]

VkSparseImageMemoryBindInfo._type_ = {
    'image': ctypes.c_void_p,
    'bindCount': ctypes.c_uint32,
    'pBinds': ctypes.POINTER(VkSparseImageMemoryBind),
}
