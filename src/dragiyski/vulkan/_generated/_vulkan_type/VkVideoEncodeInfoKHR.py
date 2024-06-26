import ctypes

class VkVideoEncodeInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkVideoEncodeH264PictureInfoKHR',
        'VkVideoEncodeH265PictureInfoKHR',
        'VkVideoInlineQueryInfoKHR',
    }
    _includes_ = {
        'VkVideoPictureResourceInfoKHR',
        'VkVideoReferenceSlotInfoKHR',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCmdEncodeVideoKHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'dstBuffer': 'dst_buffer',
        'dstBufferOffset': 'dst_buffer_offset',
        'dstBufferRange': 'dst_buffer_range',
        'srcPictureResource': 'src_picture_resource',
        'pSetupReferenceSlot': 'setup_reference_slot',
        'referenceSlotCount': 'reference_slot_count',
        'pReferenceSlots': 'reference_slots',
        'precedingExternallyEncodedBytes': 'preceding_externally_encoded_bytes',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_encode_queue',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkVideoEncodeFlagsKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkVideoPictureResourceInfoKHR import VkVideoPictureResourceInfoKHR
from .VkVideoReferenceSlotInfoKHR import VkVideoReferenceSlotInfoKHR

VkVideoEncodeInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('dstBuffer', ctypes.c_void_p),
    ('dstBufferOffset', ctypes.c_uint64),
    ('dstBufferRange', ctypes.c_uint64),
    ('srcPictureResource', VkVideoPictureResourceInfoKHR),
    ('pSetupReferenceSlot', ctypes.POINTER(VkVideoReferenceSlotInfoKHR)),
    ('referenceSlotCount', ctypes.c_uint32),
    ('pReferenceSlots', ctypes.POINTER(VkVideoReferenceSlotInfoKHR)),
    ('precedingExternallyEncodedBytes', ctypes.c_uint32),
]

VkVideoEncodeInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'dstBuffer': ctypes.c_void_p,
    'dstBufferOffset': ctypes.c_uint64,
    'dstBufferRange': ctypes.c_uint64,
    'srcPictureResource': VkVideoPictureResourceInfoKHR,
    'pSetupReferenceSlot': ctypes.POINTER(VkVideoReferenceSlotInfoKHR),
    'referenceSlotCount': ctypes.c_uint32,
    'pReferenceSlots': ctypes.POINTER(VkVideoReferenceSlotInfoKHR),
    'precedingExternallyEncodedBytes': ctypes.c_uint32,
}
