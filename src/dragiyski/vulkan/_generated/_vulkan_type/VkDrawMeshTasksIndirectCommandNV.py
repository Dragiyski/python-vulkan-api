import ctypes

class VkDrawMeshTasksIndirectCommandNV(ctypes.Structure):
    _fields_ = [
        ('taskCount', ctypes.c_uint32),
        ('firstTask', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'taskCount': 'task_count',
        'firstTask': 'first_task',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_mesh_shader',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkDrawMeshTasksIndirectCommandNV._type_ = {
    'taskCount': ctypes.c_uint32,
    'firstTask': ctypes.c_uint32,
}
