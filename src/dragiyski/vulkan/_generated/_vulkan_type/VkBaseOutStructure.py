import ctypes

class VkBaseOutStructure(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.POINTER(VkBaseOutStructure),
        }



VkBaseOutStructure._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.POINTER(VkBaseOutStructure)),
]
