import ctypes

class VkAccelerationStructureCaptureDescriptorDataInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('accelerationStructure', ctypes.c_void_p),
        ('accelerationStructureNV', ctypes.c_void_p),
    ]

VkAccelerationStructureCaptureDescriptorDataInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'accelerationStructure': ctypes.c_void_p,
    'accelerationStructureNV': ctypes.c_void_p,
}
