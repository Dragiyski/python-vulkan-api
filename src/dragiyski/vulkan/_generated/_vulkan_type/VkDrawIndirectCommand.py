import ctypes

class VkDrawIndirectCommand(ctypes.Structure):
    _fields_ = [
        ('vertexCount', ctypes.c_uint32),
        ('instanceCount', ctypes.c_uint32),
        ('firstVertex', ctypes.c_uint32),
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
        'vertexCount': 'vertex_count',
        'instanceCount': 'instance_count',
        'firstVertex': 'first_vertex',
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

VkDrawIndirectCommand._type_ = {
    'vertexCount': ctypes.c_uint32,
    'instanceCount': ctypes.c_uint32,
    'firstVertex': ctypes.c_uint32,
    'firstInstance': ctypes.c_uint32,
}
