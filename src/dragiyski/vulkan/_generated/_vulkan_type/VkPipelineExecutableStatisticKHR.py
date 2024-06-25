import ctypes

class VkPipelineExecutableStatisticKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'name': ctypes.ARRAY(ctypes.c_char, 256),
            'description': ctypes.ARRAY(ctypes.c_char, 256),
            'format': ctypes.c_int,
            'value': VkPipelineExecutableStatisticValueKHR,
        }


from .VkPipelineExecutableStatisticValueKHR import VkPipelineExecutableStatisticValueKHR

VkPipelineExecutableStatisticKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('name', ctypes.ARRAY(ctypes.c_char, 256)),
    ('description', ctypes.ARRAY(ctypes.c_char, 256)),
    ('format', ctypes.c_int),
    ('value', VkPipelineExecutableStatisticValueKHR),
]
