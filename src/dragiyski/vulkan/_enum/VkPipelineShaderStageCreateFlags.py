import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkPipelineShaderStageCreateFlags(VulkanUIntFlag):
    VK_PIPELINE_SHADER_STAGE_CREATE_ALLOW_VARYING_SUBGROUP_SIZE_BIT = 1
    VK_PIPELINE_SHADER_STAGE_CREATE_REQUIRE_FULL_SUBGROUPS_BIT = 2

sys.modules[__name__] = VkPipelineShaderStageCreateFlags
