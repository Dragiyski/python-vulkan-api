import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkDeviceDiagnosticsConfigFlagsNV(VulkanUIntFlag):
    VK_DEVICE_DIAGNOSTICS_CONFIG_ENABLE_AUTOMATIC_CHECKPOINTS_BIT_NV = 4
    VK_DEVICE_DIAGNOSTICS_CONFIG_ENABLE_RESOURCE_TRACKING_BIT_NV = 2
    VK_DEVICE_DIAGNOSTICS_CONFIG_ENABLE_SHADER_DEBUG_INFO_BIT_NV = 1
    VK_DEVICE_DIAGNOSTICS_CONFIG_ENABLE_SHADER_ERROR_REPORTING_BIT_NV = 8

sys.modules[__name__] = VkDeviceDiagnosticsConfigFlagsNV

