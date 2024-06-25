import ctypes

class VkDrawMeshTasksIndirectCommandEXT(ctypes.Structure):
    _fields_ = [
        ('groupCountX', ctypes.c_uint32),
        ('groupCountY', ctypes.c_uint32),
        ('groupCountZ', ctypes.c_uint32),
    ]

VkDrawMeshTasksIndirectCommandEXT._type_ = {
    'groupCountX': ctypes.c_uint32,
    'groupCountY': ctypes.c_uint32,
    'groupCountZ': ctypes.c_uint32,
}
