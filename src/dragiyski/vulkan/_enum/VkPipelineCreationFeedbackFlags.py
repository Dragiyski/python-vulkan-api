import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkPipelineCreationFeedbackFlags(VulkanUIntFlag):
    VK_PIPELINE_CREATION_FEEDBACK_BASE_PIPELINE_ACCELERATION_BIT = 4
    VK_PIPELINE_CREATION_FEEDBACK_APPLICATION_PIPELINE_CACHE_HIT_BIT = 2
    VK_PIPELINE_CREATION_FEEDBACK_VALID_BIT = 1

sys.modules[__name__] = VkPipelineCreationFeedbackFlags
