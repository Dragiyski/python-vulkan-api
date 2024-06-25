import ctypes

class VkGeneratedCommandsInfoNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'pipelineBindPoint': ctypes.c_int,
            'pipeline': ctypes.c_void_p,
            'indirectCommandsLayout': ctypes.c_void_p,
            'streamCount': ctypes.c_uint32,
            'pStreams': ctypes.POINTER(VkIndirectCommandsStreamNV),
            'sequencesCount': ctypes.c_uint32,
            'preprocessBuffer': ctypes.c_void_p,
            'preprocessOffset': ctypes.c_uint64,
            'preprocessSize': ctypes.c_uint64,
            'sequencesCountBuffer': ctypes.c_void_p,
            'sequencesCountOffset': ctypes.c_uint64,
            'sequencesIndexBuffer': ctypes.c_void_p,
            'sequencesIndexOffset': ctypes.c_uint64,
        }


from .VkIndirectCommandsStreamNV import VkIndirectCommandsStreamNV

VkGeneratedCommandsInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pipelineBindPoint', ctypes.c_int),
    ('pipeline', ctypes.c_void_p),
    ('indirectCommandsLayout', ctypes.c_void_p),
    ('streamCount', ctypes.c_uint32),
    ('pStreams', ctypes.POINTER(VkIndirectCommandsStreamNV)),
    ('sequencesCount', ctypes.c_uint32),
    ('preprocessBuffer', ctypes.c_void_p),
    ('preprocessOffset', ctypes.c_uint64),
    ('preprocessSize', ctypes.c_uint64),
    ('sequencesCountBuffer', ctypes.c_void_p),
    ('sequencesCountOffset', ctypes.c_uint64),
    ('sequencesIndexBuffer', ctypes.c_void_p),
    ('sequencesIndexOffset', ctypes.c_uint64),
]
