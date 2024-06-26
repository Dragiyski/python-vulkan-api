import ctypes

class VkDrawMeshTasksIndirectCommandEXT(ctypes.Structure):
    _fields_ = [
        ('groupCountX', ctypes.c_uint32),
        ('groupCountY', ctypes.c_uint32),
        ('groupCountZ', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'groupCountX': 'group_count_x',
        'groupCountY': 'group_count_y',
        'groupCountZ': 'group_count_z',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_mesh_shader',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkDrawMeshTasksIndirectCommandEXT._type_ = {
    'groupCountX': ctypes.c_uint32,
    'groupCountY': ctypes.c_uint32,
    'groupCountZ': ctypes.c_uint32,
}
