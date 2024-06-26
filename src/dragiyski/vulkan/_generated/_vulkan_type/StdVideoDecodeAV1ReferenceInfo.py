import ctypes

class StdVideoDecodeAV1ReferenceInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'StdVideoDecodeAV1ReferenceInfoFlags',
    }
    _included_in_ = {
        'VkVideoDecodeAV1DpbSlotInfoKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'flags': 'flags',
        'frame_type': 'frame_type',
        'RefFrameSignBias': 'ref_frame_sign_bias',
        'OrderHint': 'order_hint',
        'SavedOrderHints': 'saved_order_hints',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_av1std_decode',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .StdVideoDecodeAV1ReferenceInfoFlags import StdVideoDecodeAV1ReferenceInfoFlags

StdVideoDecodeAV1ReferenceInfo._fields_ = [
    ('flags', StdVideoDecodeAV1ReferenceInfoFlags),
    ('frame_type', ctypes.c_uint8),
    ('RefFrameSignBias', ctypes.c_uint8),
    ('OrderHint', ctypes.c_uint8),
    ('SavedOrderHints', ctypes.ARRAY(ctypes.c_uint8, 8)),
]

StdVideoDecodeAV1ReferenceInfo._type_ = {
    'flags': StdVideoDecodeAV1ReferenceInfoFlags,
    'frame_type': ctypes.c_uint8,
    'RefFrameSignBias': ctypes.c_uint8,
    'OrderHint': ctypes.c_uint8,
    'SavedOrderHints': ctypes.ARRAY(ctypes.c_uint8, 8),
}
