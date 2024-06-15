import ctypes, sys

class VkPipelineFragmentShadingRateStateCreateInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkPipelineFragmentShadingRateStateCreateInfoKHR

from . import VkExtent2D

VkPipelineFragmentShadingRateStateCreateInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('fragmentSize', VkExtent2D),
    ('combinerOps', ctypes.ARRAY(ctypes.c_int, 2)),
]
