import ctypes

class VkPipelineViewportCoarseSampleOrderStateCreateInfoNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'sampleOrderType': ctypes.c_int,
            'customSampleOrderCount': ctypes.c_uint32,
            'pCustomSampleOrders': ctypes.POINTER(VkCoarseSampleOrderCustomNV),
        }


from .VkCoarseSampleOrderCustomNV import VkCoarseSampleOrderCustomNV

VkPipelineViewportCoarseSampleOrderStateCreateInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('sampleOrderType', ctypes.c_int),
    ('customSampleOrderCount', ctypes.c_uint32),
    ('pCustomSampleOrders', ctypes.POINTER(VkCoarseSampleOrderCustomNV)),
]
