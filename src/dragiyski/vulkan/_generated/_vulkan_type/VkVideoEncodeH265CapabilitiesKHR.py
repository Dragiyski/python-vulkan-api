import ctypes

class VkVideoEncodeH265CapabilitiesKHR(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkVideoCapabilitiesKHR',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkExtent2D',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'maxLevelIdc': 'max_level_idc',
        'maxSliceSegmentCount': 'max_slice_segment_count',
        'maxTiles': 'max_tiles',
        'ctbSizes': 'ctb_sizes',
        'transformBlockSizes': 'transform_block_sizes',
        'maxPPictureL0ReferenceCount': 'max_ppicture_l0reference_count',
        'maxBPictureL0ReferenceCount': 'max_bpicture_l0reference_count',
        'maxL1ReferenceCount': 'max_l1reference_count',
        'maxSubLayerCount': 'max_sub_layer_count',
        'expectDyadicTemporalSubLayerPattern': 'expect_dyadic_temporal_sub_layer_pattern',
        'minQp': 'min_qp',
        'maxQp': 'max_qp',
        'prefersGopRemainingFrames': 'prefers_gop_remaining_frames',
        'requiresGopRemainingFrames': 'requires_gop_remaining_frames',
        'stdSyntaxFlags': 'std_syntax_flags',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_encode_h265',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkVideoEncodeH265CapabilityFlagsKHR',
        'maxLevelIdc': 'StdVideoH265LevelIdc',
        'ctbSizes': 'VkVideoEncodeH265CtbSizeFlagsKHR',
        'transformBlockSizes': 'VkVideoEncodeH265TransformBlockSizeFlagsKHR',
        'stdSyntaxFlags': 'VkVideoEncodeH265StdFlagsKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_CAPABILITIES_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_CAPABILITIES_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent2D import VkExtent2D

VkVideoEncodeH265CapabilitiesKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('maxLevelIdc', ctypes.c_int),
    ('maxSliceSegmentCount', ctypes.c_uint32),
    ('maxTiles', VkExtent2D),
    ('ctbSizes', ctypes.c_uint32),
    ('transformBlockSizes', ctypes.c_uint32),
    ('maxPPictureL0ReferenceCount', ctypes.c_uint32),
    ('maxBPictureL0ReferenceCount', ctypes.c_uint32),
    ('maxL1ReferenceCount', ctypes.c_uint32),
    ('maxSubLayerCount', ctypes.c_uint32),
    ('expectDyadicTemporalSubLayerPattern', ctypes.c_uint32),
    ('minQp', ctypes.c_int32),
    ('maxQp', ctypes.c_int32),
    ('prefersGopRemainingFrames', ctypes.c_uint32),
    ('requiresGopRemainingFrames', ctypes.c_uint32),
    ('stdSyntaxFlags', ctypes.c_uint32),
]

VkVideoEncodeH265CapabilitiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'maxLevelIdc': ctypes.c_int,
    'maxSliceSegmentCount': ctypes.c_uint32,
    'maxTiles': VkExtent2D,
    'ctbSizes': ctypes.c_uint32,
    'transformBlockSizes': ctypes.c_uint32,
    'maxPPictureL0ReferenceCount': ctypes.c_uint32,
    'maxBPictureL0ReferenceCount': ctypes.c_uint32,
    'maxL1ReferenceCount': ctypes.c_uint32,
    'maxSubLayerCount': ctypes.c_uint32,
    'expectDyadicTemporalSubLayerPattern': ctypes.c_uint32,
    'minQp': ctypes.c_int32,
    'maxQp': ctypes.c_int32,
    'prefersGopRemainingFrames': ctypes.c_uint32,
    'requiresGopRemainingFrames': ctypes.c_uint32,
    'stdSyntaxFlags': ctypes.c_uint32,
}
