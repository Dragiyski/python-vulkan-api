import ctypes

class VkExportMetalDeviceInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('mtlDevice', ctypes.c_void_p),
    ]

VkExportMetalDeviceInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'mtlDevice': ctypes.c_void_p,
}
