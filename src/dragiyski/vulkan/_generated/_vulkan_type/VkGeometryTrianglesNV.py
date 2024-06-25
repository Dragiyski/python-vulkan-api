import ctypes

class VkGeometryTrianglesNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'vertexData': ctypes.c_void_p,
            'vertexOffset': ctypes.c_uint64,
            'vertexCount': ctypes.c_uint32,
            'vertexStride': ctypes.c_uint64,
            'vertexFormat': ctypes.c_int,
            'indexData': ctypes.c_void_p,
            'indexOffset': ctypes.c_uint64,
            'indexCount': ctypes.c_uint32,
            'indexType': ctypes.c_int,
            'transformData': ctypes.c_void_p,
            'transformOffset': ctypes.c_uint64,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('vertexData', ctypes.c_void_p),
        ('vertexOffset', ctypes.c_uint64),
        ('vertexCount', ctypes.c_uint32),
        ('vertexStride', ctypes.c_uint64),
        ('vertexFormat', ctypes.c_int),
        ('indexData', ctypes.c_void_p),
        ('indexOffset', ctypes.c_uint64),
        ('indexCount', ctypes.c_uint32),
        ('indexType', ctypes.c_int),
        ('transformData', ctypes.c_void_p),
        ('transformOffset', ctypes.c_uint64),
    ]
