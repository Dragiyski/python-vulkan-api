import ctypes

class VkDisplayPlaneCapabilities2KHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'capabilities': VkDisplayPlaneCapabilitiesKHR,
        }


from .VkDisplayPlaneCapabilitiesKHR import VkDisplayPlaneCapabilitiesKHR

VkDisplayPlaneCapabilities2KHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('capabilities', VkDisplayPlaneCapabilitiesKHR),
]
