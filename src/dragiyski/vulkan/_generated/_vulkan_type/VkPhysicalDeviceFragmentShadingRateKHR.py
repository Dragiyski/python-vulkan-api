import ctypes

class VkPhysicalDeviceFragmentShadingRateKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'sampleCounts': ctypes.c_uint32,
            'fragmentSize': VkExtent2D,
        }


from .VkExtent2D import VkExtent2D

VkPhysicalDeviceFragmentShadingRateKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('sampleCounts', ctypes.c_uint32),
    ('fragmentSize', VkExtent2D),
]
