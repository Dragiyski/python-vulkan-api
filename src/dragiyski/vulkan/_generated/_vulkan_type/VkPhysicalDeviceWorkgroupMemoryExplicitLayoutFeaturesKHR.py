import ctypes

class VkPhysicalDeviceWorkgroupMemoryExplicitLayoutFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('workgroupMemoryExplicitLayout', ctypes.c_uint32),
        ('workgroupMemoryExplicitLayoutScalarBlockLayout', ctypes.c_uint32),
        ('workgroupMemoryExplicitLayout8BitAccess', ctypes.c_uint32),
        ('workgroupMemoryExplicitLayout16BitAccess', ctypes.c_uint32),
    ]

VkPhysicalDeviceWorkgroupMemoryExplicitLayoutFeaturesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'workgroupMemoryExplicitLayout': ctypes.c_uint32,
    'workgroupMemoryExplicitLayoutScalarBlockLayout': ctypes.c_uint32,
    'workgroupMemoryExplicitLayout8BitAccess': ctypes.c_uint32,
    'workgroupMemoryExplicitLayout16BitAccess': ctypes.c_uint32,
}
