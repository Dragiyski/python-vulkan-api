import ctypes

class VkPhysicalDeviceRenderPassStripedPropertiesARM(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'renderPassStripeGranularity': VkExtent2D,
            'maxRenderPassStripes': ctypes.c_uint32,
        }


from .VkExtent2D import VkExtent2D

VkPhysicalDeviceRenderPassStripedPropertiesARM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('renderPassStripeGranularity', VkExtent2D),
    ('maxRenderPassStripes', ctypes.c_uint32),
]
