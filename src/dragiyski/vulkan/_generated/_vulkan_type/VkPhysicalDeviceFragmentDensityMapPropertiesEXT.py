import ctypes

class VkPhysicalDeviceFragmentDensityMapPropertiesEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'minFragmentDensityTexelSize': VkExtent2D,
            'maxFragmentDensityTexelSize': VkExtent2D,
            'fragmentDensityInvocations': ctypes.c_uint32,
        }


from .VkExtent2D import VkExtent2D

VkPhysicalDeviceFragmentDensityMapPropertiesEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('minFragmentDensityTexelSize', VkExtent2D),
    ('maxFragmentDensityTexelSize', VkExtent2D),
    ('fragmentDensityInvocations', ctypes.c_uint32),
]
