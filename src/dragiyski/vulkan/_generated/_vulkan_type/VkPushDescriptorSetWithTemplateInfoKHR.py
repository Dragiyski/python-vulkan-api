import ctypes

class VkPushDescriptorSetWithTemplateInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'descriptorUpdateTemplate': ctypes.c_void_p,
            'layout': ctypes.c_void_p,
            'set': ctypes.c_uint32,
            'pData': ctypes.c_void_p,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('descriptorUpdateTemplate', ctypes.c_void_p),
        ('layout', ctypes.c_void_p),
        ('set', ctypes.c_uint32),
        ('pData', ctypes.c_void_p),
    ]
