from enum import IntFlag

class VkBufferCreateFlags(IntFlag):
    VK_BUFFER_CREATE_DESCRIPTOR_BUFFER_CAPTURE_REPLAY_BIT_EXT = 32
    VK_BUFFER_CREATE_DEVICE_ADDRESS_CAPTURE_REPLAY_BIT = 16
    VK_BUFFER_CREATE_PROTECTED_BIT = 8
    VK_BUFFER_CREATE_SPARSE_ALIASED_BIT = 4
    VK_BUFFER_CREATE_SPARSE_BINDING_BIT = 1
    VK_BUFFER_CREATE_SPARSE_RESIDENCY_BIT = 2
    VK_BUFFER_CREATE_VIDEO_PROFILE_INDEPENDENT_BIT_KHR = 64
    VK_BUFFER_CREATE_DEVICE_ADDRESS_CAPTURE_REPLAY_BIT_EXT = VK_BUFFER_CREATE_DEVICE_ADDRESS_CAPTURE_REPLAY_BIT
    VK_BUFFER_CREATE_DEVICE_ADDRESS_CAPTURE_REPLAY_BIT_KHR = VK_BUFFER_CREATE_DEVICE_ADDRESS_CAPTURE_REPLAY_BIT
