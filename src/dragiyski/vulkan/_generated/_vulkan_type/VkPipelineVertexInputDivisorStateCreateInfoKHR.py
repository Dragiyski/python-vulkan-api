import ctypes, sys

class VkPipelineVertexInputDivisorStateCreateInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkPipelineVertexInputDivisorStateCreateInfoKHR

from . import VkVertexInputBindingDivisorDescriptionKHR

VkPipelineVertexInputDivisorStateCreateInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('vertexBindingDivisorCount', ctypes.c_uint32),
    ('pVertexBindingDivisors', ctypes.POINTER(VkVertexInputBindingDivisorDescriptionKHR)),
]
