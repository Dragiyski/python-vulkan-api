import ctypes

class VkPhysicalDeviceMultiviewPerViewRenderAreasFeaturesQCOM(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('multiviewPerViewRenderAreas', ctypes.c_uint32),
    ]

VkPhysicalDeviceMultiviewPerViewRenderAreasFeaturesQCOM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'multiviewPerViewRenderAreas': ctypes.c_uint32,
}
