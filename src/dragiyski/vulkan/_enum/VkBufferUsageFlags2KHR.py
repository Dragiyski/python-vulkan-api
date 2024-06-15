import ctypes, sys
from .._vulkan_base import VulkanULongFlag

class VkBufferUsageFlags2KHR(VulkanULongFlag):
    VK_BUFFER_USAGE_2_ACCELERATION_STRUCTURE_BUILD_INPUT_READ_ONLY_BIT_KHR = 524288
    VK_BUFFER_USAGE_2_ACCELERATION_STRUCTURE_STORAGE_BIT_KHR = 1048576
    VK_BUFFER_USAGE_2_CONDITIONAL_RENDERING_BIT_EXT = 512
    VK_BUFFER_USAGE_2_EXECUTION_GRAPH_SCRATCH_BIT_AMDX = 33554432
    VK_BUFFER_USAGE_2_INDEX_BUFFER_BIT_KHR = 64
    VK_BUFFER_USAGE_2_INDIRECT_BUFFER_BIT_KHR = 256
    VK_BUFFER_USAGE_2_MICROMAP_BUILD_INPUT_READ_ONLY_BIT_EXT = 8388608
    VK_BUFFER_USAGE_2_MICROMAP_STORAGE_BIT_EXT = 16777216
    VK_BUFFER_USAGE_2_PUSH_DESCRIPTORS_DESCRIPTOR_BUFFER_BIT_EXT = 67108864
    VK_BUFFER_USAGE_2_RESOURCE_DESCRIPTOR_BUFFER_BIT_EXT = 4194304
    VK_BUFFER_USAGE_2_SAMPLER_DESCRIPTOR_BUFFER_BIT_EXT = 2097152
    VK_BUFFER_USAGE_2_SHADER_BINDING_TABLE_BIT_KHR = 1024
    VK_BUFFER_USAGE_2_SHADER_DEVICE_ADDRESS_BIT_KHR = 131072
    VK_BUFFER_USAGE_2_STORAGE_BUFFER_BIT_KHR = 32
    VK_BUFFER_USAGE_2_STORAGE_TEXEL_BUFFER_BIT_KHR = 8
    VK_BUFFER_USAGE_2_TRANSFER_DST_BIT_KHR = 2
    VK_BUFFER_USAGE_2_TRANSFER_SRC_BIT_KHR = 1
    VK_BUFFER_USAGE_2_TRANSFORM_FEEDBACK_BUFFER_BIT_EXT = 2048
    VK_BUFFER_USAGE_2_TRANSFORM_FEEDBACK_COUNTER_BUFFER_BIT_EXT = 4096
    VK_BUFFER_USAGE_2_UNIFORM_BUFFER_BIT_KHR = 16
    VK_BUFFER_USAGE_2_UNIFORM_TEXEL_BUFFER_BIT_KHR = 4
    VK_BUFFER_USAGE_2_VERTEX_BUFFER_BIT_KHR = 128
    VK_BUFFER_USAGE_2_VIDEO_DECODE_DST_BIT_KHR = 16384
    VK_BUFFER_USAGE_2_VIDEO_DECODE_SRC_BIT_KHR = 8192
    VK_BUFFER_USAGE_2_VIDEO_ENCODE_DST_BIT_KHR = 32768
    VK_BUFFER_USAGE_2_VIDEO_ENCODE_SRC_BIT_KHR = 65536

sys.modules[__name__] = VkBufferUsageFlags2KHR

VkBufferUsageFlags2KHR.VK_BUFFER_USAGE_2_RAY_TRACING_BIT_NV = VkBufferUsageFlags2KHR.VK_BUFFER_USAGE_2_SHADER_BINDING_TABLE_BIT_KHR
