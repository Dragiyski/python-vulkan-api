import ctypes

class VkDrawIndexedIndirectCommand(ctypes.Structure):
    _fields_ = [
        ('indexCount', ctypes.c_uint32),
        ('instanceCount', ctypes.c_uint32),
        ('firstIndex', ctypes.c_uint32),
        ('vertexOffset', ctypes.c_int32),
        ('firstInstance', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'indexCount': 'index_count',
        'instanceCount': 'instance_count',
        'firstIndex': 'first_index',
        'vertexOffset': 'vertex_offset',
        'firstInstance': 'first_instance',
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

VkDrawIndexedIndirectCommand._type_ = {
    'indexCount': ctypes.c_uint32,
    'instanceCount': ctypes.c_uint32,
    'firstIndex': ctypes.c_uint32,
    'vertexOffset': ctypes.c_int32,
    'firstInstance': ctypes.c_uint32,
}
