import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkPerformanceCounterScopeKHR(VulkanIntEnum):
    VK_PERFORMANCE_COUNTER_SCOPE_RENDER_PASS_KHR = 1
    VK_PERFORMANCE_COUNTER_SCOPE_COMMAND_BUFFER_KHR = 0
    VK_PERFORMANCE_COUNTER_SCOPE_COMMAND_KHR = 2

sys.modules[__name__] = VkPerformanceCounterScopeKHR
