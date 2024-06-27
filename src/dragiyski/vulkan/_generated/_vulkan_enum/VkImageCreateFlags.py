from enum import IntFlag

class VkImageCreateFlags(IntFlag):
    VK_IMAGE_CREATE_2D_ARRAY_COMPATIBLE_BIT = 32
    VK_IMAGE_CREATE_2D_VIEW_COMPATIBLE_BIT_EXT = 131072
    VK_IMAGE_CREATE_ALIAS_BIT = 1024
    VK_IMAGE_CREATE_BLOCK_TEXEL_VIEW_COMPATIBLE_BIT = 128
    VK_IMAGE_CREATE_CORNER_SAMPLED_BIT_NV = 8192
    VK_IMAGE_CREATE_CUBE_COMPATIBLE_BIT = 16
    VK_IMAGE_CREATE_DESCRIPTOR_BUFFER_CAPTURE_REPLAY_BIT_EXT = 65536
    VK_IMAGE_CREATE_DISJOINT_BIT = 512
    VK_IMAGE_CREATE_EXTENDED_USAGE_BIT = 256
    VK_IMAGE_CREATE_FRAGMENT_DENSITY_MAP_OFFSET_BIT_QCOM = 32768
    VK_IMAGE_CREATE_MULTISAMPLED_RENDER_TO_SINGLE_SAMPLED_BIT_EXT = 262144
    VK_IMAGE_CREATE_MUTABLE_FORMAT_BIT = 8
    VK_IMAGE_CREATE_PROTECTED_BIT = 2048
    VK_IMAGE_CREATE_SAMPLE_LOCATIONS_COMPATIBLE_DEPTH_BIT_EXT = 4096
    VK_IMAGE_CREATE_SPARSE_ALIASED_BIT = 4
    VK_IMAGE_CREATE_SPARSE_BINDING_BIT = 1
    VK_IMAGE_CREATE_SPARSE_RESIDENCY_BIT = 2
    VK_IMAGE_CREATE_SPLIT_INSTANCE_BIND_REGIONS_BIT = 64
    VK_IMAGE_CREATE_SUBSAMPLED_BIT_EXT = 16384
    VK_IMAGE_CREATE_VIDEO_PROFILE_INDEPENDENT_BIT_KHR = 1048576
    VK_IMAGE_CREATE_2D_ARRAY_COMPATIBLE_BIT_KHR = VK_IMAGE_CREATE_2D_ARRAY_COMPATIBLE_BIT
    VK_IMAGE_CREATE_ALIAS_BIT_KHR = VK_IMAGE_CREATE_ALIAS_BIT
    VK_IMAGE_CREATE_BLOCK_TEXEL_VIEW_COMPATIBLE_BIT_KHR = VK_IMAGE_CREATE_BLOCK_TEXEL_VIEW_COMPATIBLE_BIT
    VK_IMAGE_CREATE_DISJOINT_BIT_KHR = VK_IMAGE_CREATE_DISJOINT_BIT
    VK_IMAGE_CREATE_EXTENDED_USAGE_BIT_KHR = VK_IMAGE_CREATE_EXTENDED_USAGE_BIT
    VK_IMAGE_CREATE_SPLIT_INSTANCE_BIND_REGIONS_BIT_KHR = VK_IMAGE_CREATE_SPLIT_INSTANCE_BIND_REGIONS_BIT