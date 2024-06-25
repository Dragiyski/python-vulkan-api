import ctypes

class VkDirectDriverLoadingListLUNARG(ctypes.Structure):
    pass

from .VkDirectDriverLoadingInfoLUNARG import VkDirectDriverLoadingInfoLUNARG

VkDirectDriverLoadingListLUNARG._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('mode', ctypes.c_int),
    ('driverCount', ctypes.c_uint32),
    ('pDrivers', ctypes.POINTER(VkDirectDriverLoadingInfoLUNARG)),
]

VkDirectDriverLoadingListLUNARG._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'mode': ctypes.c_int,
    'driverCount': ctypes.c_uint32,
    'pDrivers': ctypes.POINTER(VkDirectDriverLoadingInfoLUNARG),
}
