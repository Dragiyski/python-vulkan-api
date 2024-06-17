import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkMemoryOverallocationBehaviorAMD(VulkanIntEnum):
    VK_MEMORY_OVERALLOCATION_BEHAVIOR_ALLOWED_AMD = 1
    VK_MEMORY_OVERALLOCATION_BEHAVIOR_DEFAULT_AMD = 0
    VK_MEMORY_OVERALLOCATION_BEHAVIOR_DISALLOWED_AMD = 2

sys.modules[__name__] = VkMemoryOverallocationBehaviorAMD

