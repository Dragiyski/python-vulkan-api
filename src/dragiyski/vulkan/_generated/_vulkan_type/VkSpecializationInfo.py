import ctypes

class VkSpecializationInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'mapEntryCount': ctypes.c_uint32,
            'pMapEntries': ctypes.POINTER(VkSpecializationMapEntry),
            'dataSize': ctypes.c_size_t,
            'pData': ctypes.c_void_p,
        }


from .VkSpecializationMapEntry import VkSpecializationMapEntry

VkSpecializationInfo._fields_ = [
    ('mapEntryCount', ctypes.c_uint32),
    ('pMapEntries', ctypes.POINTER(VkSpecializationMapEntry)),
    ('dataSize', ctypes.c_size_t),
    ('pData', ctypes.c_void_p),
]
