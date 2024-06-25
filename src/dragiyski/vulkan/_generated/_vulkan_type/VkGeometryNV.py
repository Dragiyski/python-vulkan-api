import ctypes

class VkGeometryNV(ctypes.Structure):
    pass

from .VkGeometryDataNV import VkGeometryDataNV

VkGeometryNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('geometryType', ctypes.c_int),
    ('geometry', VkGeometryDataNV),
    ('flags', ctypes.c_uint32),
]

VkGeometryNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'geometryType': ctypes.c_int,
    'geometry': VkGeometryDataNV,
    'flags': ctypes.c_uint32,
}
