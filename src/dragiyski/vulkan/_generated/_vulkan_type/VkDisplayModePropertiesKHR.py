import ctypes

class VkDisplayModePropertiesKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'displayMode': ctypes.c_void_p,
            'parameters': VkDisplayModeParametersKHR,
        }


from .VkDisplayModeParametersKHR import VkDisplayModeParametersKHR

VkDisplayModePropertiesKHR._fields_ = [
    ('displayMode', ctypes.c_void_p),
    ('parameters', VkDisplayModeParametersKHR),
]
