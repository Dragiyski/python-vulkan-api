import ctypes

class VkVideoBeginCodingInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkVideoEncodeH264GopRemainingFrameInfoKHR',
        'VkVideoEncodeH264RateControlInfoKHR',
        'VkVideoEncodeH265GopRemainingFrameInfoKHR',
        'VkVideoEncodeH265RateControlInfoKHR',
        'VkVideoEncodeRateControlInfoKHR',
    }
    _includes_ = {
        'VkVideoReferenceSlotInfoKHR',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCmdBeginVideoCodingKHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'videoSession': 'video_session',
        'videoSessionParameters': 'video_session_parameters',
        'referenceSlotCount': 'reference_slot_count',
        'pReferenceSlots': 'reference_slots',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_queue',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkVideoBeginCodingFlagsKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_BEGIN_CODING_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_BEGIN_CODING_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkVideoReferenceSlotInfoKHR import VkVideoReferenceSlotInfoKHR

VkVideoBeginCodingInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('videoSession', ctypes.c_void_p),
    ('videoSessionParameters', ctypes.c_void_p),
    ('referenceSlotCount', ctypes.c_uint32),
    ('pReferenceSlots', ctypes.POINTER(VkVideoReferenceSlotInfoKHR)),
]

VkVideoBeginCodingInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'videoSession': ctypes.c_void_p,
    'videoSessionParameters': ctypes.c_void_p,
    'referenceSlotCount': ctypes.c_uint32,
    'pReferenceSlots': ctypes.POINTER(VkVideoReferenceSlotInfoKHR),
}
