import ctypes, sys

class VkPipelineViewportCoarseSampleOrderStateCreateInfoNV(ctypes.Structure):
    pass

sys.modules[__name__] = VkPipelineViewportCoarseSampleOrderStateCreateInfoNV

from . import VkCoarseSampleOrderCustomNV

VkPipelineViewportCoarseSampleOrderStateCreateInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('sampleOrderType', ctypes.c_int),
    ('customSampleOrderCount', ctypes.c_uint32),
    ('pCustomSampleOrders', ctypes.POINTER(VkCoarseSampleOrderCustomNV)),
]
