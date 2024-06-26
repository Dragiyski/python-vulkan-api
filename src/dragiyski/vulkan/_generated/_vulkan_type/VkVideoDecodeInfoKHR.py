import ctypes

class VkVideoDecodeInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkVideoDecodeAV1PictureInfoKHR',
        'VkVideoDecodeH264PictureInfoKHR',
        'VkVideoDecodeH265PictureInfoKHR',
        'VkVideoInlineQueryInfoKHR',
    }
    _includes_ = {
        'VkVideoPictureResourceInfoKHR',
        'VkVideoReferenceSlotInfoKHR',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCmdDecodeVideoKHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'srcBuffer': 'src_buffer',
        'srcBufferOffset': 'src_buffer_offset',
        'srcBufferRange': 'src_buffer_range',
        'dstPictureResource': 'dst_picture_resource',
        'pSetupReferenceSlot': 'setup_reference_slot',
        'referenceSlotCount': 'reference_slot_count',
        'pReferenceSlots': 'reference_slots',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_decode_queue',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkVideoDecodeFlagsKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_DECODE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkVideoPictureResourceInfoKHR import VkVideoPictureResourceInfoKHR
from .VkVideoReferenceSlotInfoKHR import VkVideoReferenceSlotInfoKHR

VkVideoDecodeInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('srcBuffer', ctypes.c_void_p),
    ('srcBufferOffset', ctypes.c_uint64),
    ('srcBufferRange', ctypes.c_uint64),
    ('dstPictureResource', VkVideoPictureResourceInfoKHR),
    ('pSetupReferenceSlot', ctypes.POINTER(VkVideoReferenceSlotInfoKHR)),
    ('referenceSlotCount', ctypes.c_uint32),
    ('pReferenceSlots', ctypes.POINTER(VkVideoReferenceSlotInfoKHR)),
]

VkVideoDecodeInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'srcBuffer': ctypes.c_void_p,
    'srcBufferOffset': ctypes.c_uint64,
    'srcBufferRange': ctypes.c_uint64,
    'dstPictureResource': VkVideoPictureResourceInfoKHR,
    'pSetupReferenceSlot': ctypes.POINTER(VkVideoReferenceSlotInfoKHR),
    'referenceSlotCount': ctypes.c_uint32,
    'pReferenceSlots': ctypes.POINTER(VkVideoReferenceSlotInfoKHR),
}
