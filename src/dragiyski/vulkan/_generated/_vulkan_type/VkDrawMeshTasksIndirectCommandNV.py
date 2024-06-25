import ctypes

class VkDrawMeshTasksIndirectCommandNV(ctypes.Structure):
    _fields_ = [
        ('taskCount', ctypes.c_uint32),
        ('firstTask', ctypes.c_uint32),
    ]

VkDrawMeshTasksIndirectCommandNV._type_ = {
    'taskCount': ctypes.c_uint32,
    'firstTask': ctypes.c_uint32,
}
