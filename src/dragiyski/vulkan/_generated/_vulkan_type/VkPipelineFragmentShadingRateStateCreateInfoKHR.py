import ctypes

class VkPipelineFragmentShadingRateStateCreateInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'fragmentSize': VkExtent2D,
            'combinerOps': ctypes.ARRAY(ctypes.c_int, 2),
        }


from .VkExtent2D import VkExtent2D

VkPipelineFragmentShadingRateStateCreateInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('fragmentSize', VkExtent2D),
    ('combinerOps', ctypes.ARRAY(ctypes.c_int, 2)),
]
