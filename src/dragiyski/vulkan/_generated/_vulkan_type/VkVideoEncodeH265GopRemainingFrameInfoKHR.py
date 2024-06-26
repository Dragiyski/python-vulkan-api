import ctypes

class VkVideoEncodeH265GopRemainingFrameInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('useGopRemainingFrames', ctypes.c_uint32),
        ('gopRemainingI', ctypes.c_uint32),
        ('gopRemainingP', ctypes.c_uint32),
        ('gopRemainingB', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkVideoBeginCodingInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'useGopRemainingFrames': 'use_gop_remaining_frames',
        'gopRemainingI': 'gop_remaining_i',
        'gopRemainingP': 'gop_remaining',
        'gopRemainingB': 'gop_remaining_b',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_encode_h265',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_GOP_REMAINING_FRAME_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_GOP_REMAINING_FRAME_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkVideoEncodeH265GopRemainingFrameInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'useGopRemainingFrames': ctypes.c_uint32,
    'gopRemainingI': ctypes.c_uint32,
    'gopRemainingP': ctypes.c_uint32,
    'gopRemainingB': ctypes.c_uint32,
}
