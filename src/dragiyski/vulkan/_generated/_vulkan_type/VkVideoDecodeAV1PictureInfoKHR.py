import ctypes

class VkVideoDecodeAV1PictureInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkVideoDecodeInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = {
        'StdVideoDecodeAV1PictureInfo',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'pStdPictureInfo': 'std_picture_info',
        'referenceNameSlotIndices': 'reference_name_slot_indices',
        'frameHeaderOffset': 'frame_header_offset',
        'tileCount': 'tile_count',
        'pTileOffsets': 'tile_offsets',
        'pTileSizes': 'tile_sizes',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_decode_av1',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_DECODE_AV1_PICTURE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_AV1_PICTURE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .StdVideoDecodeAV1PictureInfo import StdVideoDecodeAV1PictureInfo

VkVideoDecodeAV1PictureInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdPictureInfo', ctypes.POINTER(StdVideoDecodeAV1PictureInfo)),
    ('referenceNameSlotIndices', ctypes.ARRAY(ctypes.c_int32, 7)),
    ('frameHeaderOffset', ctypes.c_uint32),
    ('tileCount', ctypes.c_uint32),
    ('pTileOffsets', ctypes.POINTER(ctypes.c_uint32)),
    ('pTileSizes', ctypes.POINTER(ctypes.c_uint32)),
]

VkVideoDecodeAV1PictureInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pStdPictureInfo': ctypes.POINTER(StdVideoDecodeAV1PictureInfo),
    'referenceNameSlotIndices': ctypes.ARRAY(ctypes.c_int32, 7),
    'frameHeaderOffset': ctypes.c_uint32,
    'tileCount': ctypes.c_uint32,
    'pTileOffsets': ctypes.POINTER(ctypes.c_uint32),
    'pTileSizes': ctypes.POINTER(ctypes.c_uint32),
}
