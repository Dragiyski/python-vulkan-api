import ctypes

class VkPhysicalDevicePerStageDescriptorSetFeaturesNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'perStageDescriptorSet': ctypes.c_uint32,
            'dynamicPipelineLayout': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('perStageDescriptorSet', ctypes.c_uint32),
        ('dynamicPipelineLayout', ctypes.c_uint32),
    ]
