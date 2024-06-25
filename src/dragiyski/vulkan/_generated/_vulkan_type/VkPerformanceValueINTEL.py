import ctypes

class VkPerformanceValueINTEL(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'type': ctypes.c_int,
            'data': VkPerformanceValueDataINTEL,
        }


from .VkPerformanceValueDataINTEL import VkPerformanceValueDataINTEL

VkPerformanceValueINTEL._fields_ = [
    ('type', ctypes.c_int),
    ('data', VkPerformanceValueDataINTEL),
]
