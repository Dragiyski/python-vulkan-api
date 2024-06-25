import ctypes

class VkAccelerationStructureInfoNV(ctypes.Structure):
    pass

from .VkGeometryNV import VkGeometryNV

VkAccelerationStructureInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('type', ctypes.c_int),
    ('flags', ctypes.c_uint32),
    ('instanceCount', ctypes.c_uint32),
    ('geometryCount', ctypes.c_uint32),
    ('pGeometries', ctypes.POINTER(VkGeometryNV)),
]

VkAccelerationStructureInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'type': ctypes.c_int,
    'flags': ctypes.c_uint32,
    'instanceCount': ctypes.c_uint32,
    'geometryCount': ctypes.c_uint32,
    'pGeometries': ctypes.POINTER(VkGeometryNV),
}
