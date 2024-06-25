import ctypes

class VkPipelineVertexInputDivisorStateCreateInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'vertexBindingDivisorCount': ctypes.c_uint32,
            'pVertexBindingDivisors': ctypes.POINTER(VkVertexInputBindingDivisorDescriptionKHR),
        }


from .VkVertexInputBindingDivisorDescriptionKHR import VkVertexInputBindingDivisorDescriptionKHR

VkPipelineVertexInputDivisorStateCreateInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('vertexBindingDivisorCount', ctypes.c_uint32),
    ('pVertexBindingDivisors', ctypes.POINTER(VkVertexInputBindingDivisorDescriptionKHR)),
]
