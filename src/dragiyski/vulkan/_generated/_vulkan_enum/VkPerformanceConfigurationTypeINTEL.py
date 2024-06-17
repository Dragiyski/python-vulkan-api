import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkPerformanceConfigurationTypeINTEL(VulkanIntEnum):
    VK_PERFORMANCE_CONFIGURATION_TYPE_COMMAND_QUEUE_METRICS_DISCOVERY_ACTIVATED_INTEL = 0

sys.modules[__name__] = VkPerformanceConfigurationTypeINTEL

