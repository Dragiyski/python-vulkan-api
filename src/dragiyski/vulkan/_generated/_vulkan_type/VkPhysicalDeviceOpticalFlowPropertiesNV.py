import ctypes

class VkPhysicalDeviceOpticalFlowPropertiesNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'supportedOutputGridSizes': ctypes.c_uint32,
            'supportedHintGridSizes': ctypes.c_uint32,
            'hintSupported': ctypes.c_uint32,
            'costSupported': ctypes.c_uint32,
            'bidirectionalFlowSupported': ctypes.c_uint32,
            'globalFlowSupported': ctypes.c_uint32,
            'minWidth': ctypes.c_uint32,
            'minHeight': ctypes.c_uint32,
            'maxWidth': ctypes.c_uint32,
            'maxHeight': ctypes.c_uint32,
            'maxNumRegionsOfInterest': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('supportedOutputGridSizes', ctypes.c_uint32),
        ('supportedHintGridSizes', ctypes.c_uint32),
        ('hintSupported', ctypes.c_uint32),
        ('costSupported', ctypes.c_uint32),
        ('bidirectionalFlowSupported', ctypes.c_uint32),
        ('globalFlowSupported', ctypes.c_uint32),
        ('minWidth', ctypes.c_uint32),
        ('minHeight', ctypes.c_uint32),
        ('maxWidth', ctypes.c_uint32),
        ('maxHeight', ctypes.c_uint32),
        ('maxNumRegionsOfInterest', ctypes.c_uint32),
    ]
