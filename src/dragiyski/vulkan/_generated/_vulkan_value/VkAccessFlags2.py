from enum import IntFlag

class Value(IntFlag):
    VK_ACCESS_2_ACCELERATION_STRUCTURE_READ_BIT_KHR = 2097152
    VK_ACCESS_2_ACCELERATION_STRUCTURE_WRITE_BIT_KHR = 4194304
    VK_ACCESS_2_COLOR_ATTACHMENT_READ_BIT = 128
    VK_ACCESS_2_COLOR_ATTACHMENT_READ_NONCOHERENT_BIT_EXT = 524288
    VK_ACCESS_2_COLOR_ATTACHMENT_WRITE_BIT = 256
    VK_ACCESS_2_COMMAND_PREPROCESS_READ_BIT_NV = 131072
    VK_ACCESS_2_COMMAND_PREPROCESS_WRITE_BIT_NV = 262144
    VK_ACCESS_2_CONDITIONAL_RENDERING_READ_BIT_EXT = 1048576
    VK_ACCESS_2_DEPTH_STENCIL_ATTACHMENT_READ_BIT = 512
    VK_ACCESS_2_DEPTH_STENCIL_ATTACHMENT_WRITE_BIT = 1024
    VK_ACCESS_2_DESCRIPTOR_BUFFER_READ_BIT_EXT = 2199023255552
    VK_ACCESS_2_FRAGMENT_DENSITY_MAP_READ_BIT_EXT = 16777216
    VK_ACCESS_2_FRAGMENT_SHADING_RATE_ATTACHMENT_READ_BIT_KHR = 8388608
    VK_ACCESS_2_HOST_READ_BIT = 8192
    VK_ACCESS_2_HOST_WRITE_BIT = 16384
    VK_ACCESS_2_INDEX_READ_BIT = 2
    VK_ACCESS_2_INDIRECT_COMMAND_READ_BIT = 1
    VK_ACCESS_2_INPUT_ATTACHMENT_READ_BIT = 16
    VK_ACCESS_2_INVOCATION_MASK_READ_BIT_HUAWEI = 549755813888
    VK_ACCESS_2_MEMORY_READ_BIT = 32768
    VK_ACCESS_2_MEMORY_WRITE_BIT = 65536
    VK_ACCESS_2_MICROMAP_READ_BIT_EXT = 17592186044416
    VK_ACCESS_2_MICROMAP_WRITE_BIT_EXT = 35184372088832
    VK_ACCESS_2_NONE = 0
    VK_ACCESS_2_OPTICAL_FLOW_READ_BIT_NV = 4398046511104
    VK_ACCESS_2_OPTICAL_FLOW_WRITE_BIT_NV = 8796093022208
    VK_ACCESS_2_SHADER_BINDING_TABLE_READ_BIT_KHR = 1099511627776
    VK_ACCESS_2_SHADER_READ_BIT = 32
    VK_ACCESS_2_SHADER_SAMPLED_READ_BIT = 4294967296
    VK_ACCESS_2_SHADER_STORAGE_READ_BIT = 8589934592
    VK_ACCESS_2_SHADER_STORAGE_WRITE_BIT = 17179869184
    VK_ACCESS_2_SHADER_WRITE_BIT = 64
    VK_ACCESS_2_TRANSFER_READ_BIT = 2048
    VK_ACCESS_2_TRANSFER_WRITE_BIT = 4096
    VK_ACCESS_2_TRANSFORM_FEEDBACK_COUNTER_READ_BIT_EXT = 67108864
    VK_ACCESS_2_TRANSFORM_FEEDBACK_COUNTER_WRITE_BIT_EXT = 134217728
    VK_ACCESS_2_TRANSFORM_FEEDBACK_WRITE_BIT_EXT = 33554432
    VK_ACCESS_2_UNIFORM_READ_BIT = 8
    VK_ACCESS_2_VERTEX_ATTRIBUTE_READ_BIT = 4
    VK_ACCESS_2_VIDEO_DECODE_READ_BIT_KHR = 34359738368
    VK_ACCESS_2_VIDEO_DECODE_WRITE_BIT_KHR = 68719476736
    VK_ACCESS_2_VIDEO_ENCODE_READ_BIT_KHR = 137438953472
    VK_ACCESS_2_VIDEO_ENCODE_WRITE_BIT_KHR = 274877906944
    VK_ACCESS_2_ACCELERATION_STRUCTURE_READ_BIT_NV = VK_ACCESS_2_ACCELERATION_STRUCTURE_READ_BIT_KHR
    VK_ACCESS_2_ACCELERATION_STRUCTURE_WRITE_BIT_NV = VK_ACCESS_2_ACCELERATION_STRUCTURE_WRITE_BIT_KHR
    VK_ACCESS_2_COLOR_ATTACHMENT_READ_BIT_KHR = VK_ACCESS_2_COLOR_ATTACHMENT_READ_BIT
    VK_ACCESS_2_COLOR_ATTACHMENT_WRITE_BIT_KHR = VK_ACCESS_2_COLOR_ATTACHMENT_WRITE_BIT
    VK_ACCESS_2_DEPTH_STENCIL_ATTACHMENT_READ_BIT_KHR = VK_ACCESS_2_DEPTH_STENCIL_ATTACHMENT_READ_BIT
    VK_ACCESS_2_DEPTH_STENCIL_ATTACHMENT_WRITE_BIT_KHR = VK_ACCESS_2_DEPTH_STENCIL_ATTACHMENT_WRITE_BIT
    VK_ACCESS_2_HOST_READ_BIT_KHR = VK_ACCESS_2_HOST_READ_BIT
    VK_ACCESS_2_HOST_WRITE_BIT_KHR = VK_ACCESS_2_HOST_WRITE_BIT
    VK_ACCESS_2_INDEX_READ_BIT_KHR = VK_ACCESS_2_INDEX_READ_BIT
    VK_ACCESS_2_INDIRECT_COMMAND_READ_BIT_KHR = VK_ACCESS_2_INDIRECT_COMMAND_READ_BIT
    VK_ACCESS_2_INPUT_ATTACHMENT_READ_BIT_KHR = VK_ACCESS_2_INPUT_ATTACHMENT_READ_BIT
    VK_ACCESS_2_MEMORY_READ_BIT_KHR = VK_ACCESS_2_MEMORY_READ_BIT
    VK_ACCESS_2_MEMORY_WRITE_BIT_KHR = VK_ACCESS_2_MEMORY_WRITE_BIT
    VK_ACCESS_2_NONE_KHR = VK_ACCESS_2_NONE
    VK_ACCESS_2_SHADER_READ_BIT_KHR = VK_ACCESS_2_SHADER_READ_BIT
    VK_ACCESS_2_SHADER_SAMPLED_READ_BIT_KHR = VK_ACCESS_2_SHADER_SAMPLED_READ_BIT
    VK_ACCESS_2_SHADER_STORAGE_READ_BIT_KHR = VK_ACCESS_2_SHADER_STORAGE_READ_BIT
    VK_ACCESS_2_SHADER_STORAGE_WRITE_BIT_KHR = VK_ACCESS_2_SHADER_STORAGE_WRITE_BIT
    VK_ACCESS_2_SHADER_WRITE_BIT_KHR = VK_ACCESS_2_SHADER_WRITE_BIT
    VK_ACCESS_2_SHADING_RATE_IMAGE_READ_BIT_NV = VK_ACCESS_2_FRAGMENT_SHADING_RATE_ATTACHMENT_READ_BIT_KHR
    VK_ACCESS_2_TRANSFER_READ_BIT_KHR = VK_ACCESS_2_TRANSFER_READ_BIT
    VK_ACCESS_2_TRANSFER_WRITE_BIT_KHR = VK_ACCESS_2_TRANSFER_WRITE_BIT
    VK_ACCESS_2_UNIFORM_READ_BIT_KHR = VK_ACCESS_2_UNIFORM_READ_BIT
    VK_ACCESS_2_VERTEX_ATTRIBUTE_READ_BIT_KHR = VK_ACCESS_2_VERTEX_ATTRIBUTE_READ_BIT
