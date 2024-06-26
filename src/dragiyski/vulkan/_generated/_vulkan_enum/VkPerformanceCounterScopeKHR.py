from enum import IntEnum

class VkPerformanceCounterScopeKHR(IntEnum):
    VK_PERFORMANCE_COUNTER_SCOPE_COMMAND_BUFFER_KHR = 0
    VK_PERFORMANCE_COUNTER_SCOPE_COMMAND_KHR = 2
    VK_PERFORMANCE_COUNTER_SCOPE_RENDER_PASS_KHR = 1
    VK_QUERY_SCOPE_COMMAND_BUFFER_KHR = VK_PERFORMANCE_COUNTER_SCOPE_COMMAND_BUFFER_KHR
    VK_QUERY_SCOPE_COMMAND_KHR = VK_PERFORMANCE_COUNTER_SCOPE_COMMAND_KHR
    VK_QUERY_SCOPE_RENDER_PASS_KHR = VK_PERFORMANCE_COUNTER_SCOPE_RENDER_PASS_KHR
