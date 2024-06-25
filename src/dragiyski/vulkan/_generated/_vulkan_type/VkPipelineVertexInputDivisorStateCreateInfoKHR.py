import ctypes

class VkPipelineVertexInputDivisorStateCreateInfoKHR(ctypes.Structure):
    pass

from .VkVertexInputBindingDivisorDescriptionKHR import VkVertexInputBindingDivisorDescriptionKHR

VkPipelineVertexInputDivisorStateCreateInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('vertexBindingDivisorCount', ctypes.c_uint32),
    ('pVertexBindingDivisors', ctypes.POINTER(VkVertexInputBindingDivisorDescriptionKHR)),
]

VkPipelineVertexInputDivisorStateCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'vertexBindingDivisorCount': ctypes.c_uint32,
    'pVertexBindingDivisors': ctypes.POINTER(VkVertexInputBindingDivisorDescriptionKHR),
}
