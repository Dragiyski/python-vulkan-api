from enum import IntFlag

class VkQueueFlags(IntFlag):
    VK_QUEUE_COMPUTE_BIT = 2
    VK_QUEUE_GRAPHICS_BIT = 1
    VK_QUEUE_OPTICAL_FLOW_BIT_NV = 256
    VK_QUEUE_PROTECTED_BIT = 16
    VK_QUEUE_SPARSE_BINDING_BIT = 8
    VK_QUEUE_TRANSFER_BIT = 4
    VK_QUEUE_VIDEO_DECODE_BIT_KHR = 32
    VK_QUEUE_VIDEO_ENCODE_BIT_KHR = 64
