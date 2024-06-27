from enum import IntEnum

class VkDebugReportObjectTypeEXT(IntEnum):
    VK_DEBUG_REPORT_OBJECT_TYPE_ACCELERATION_STRUCTURE_KHR_EXT = 1000150000
    VK_DEBUG_REPORT_OBJECT_TYPE_ACCELERATION_STRUCTURE_NV_EXT = 1000165000
    VK_DEBUG_REPORT_OBJECT_TYPE_BUFFER_COLLECTION_FUCHSIA_EXT = 1000366000
    VK_DEBUG_REPORT_OBJECT_TYPE_BUFFER_EXT = 9
    VK_DEBUG_REPORT_OBJECT_TYPE_BUFFER_VIEW_EXT = 13
    VK_DEBUG_REPORT_OBJECT_TYPE_COMMAND_BUFFER_EXT = 6
    VK_DEBUG_REPORT_OBJECT_TYPE_COMMAND_POOL_EXT = 25
    VK_DEBUG_REPORT_OBJECT_TYPE_CUDA_FUNCTION_NV_EXT = 1000307001
    VK_DEBUG_REPORT_OBJECT_TYPE_CUDA_MODULE_NV_EXT = 1000307000
    VK_DEBUG_REPORT_OBJECT_TYPE_CU_FUNCTION_NVX_EXT = 1000029001
    VK_DEBUG_REPORT_OBJECT_TYPE_CU_MODULE_NVX_EXT = 1000029000
    VK_DEBUG_REPORT_OBJECT_TYPE_DEBUG_REPORT_CALLBACK_EXT_EXT = 28
    VK_DEBUG_REPORT_OBJECT_TYPE_DESCRIPTOR_POOL_EXT = 22
    VK_DEBUG_REPORT_OBJECT_TYPE_DESCRIPTOR_SET_EXT = 23
    VK_DEBUG_REPORT_OBJECT_TYPE_DESCRIPTOR_SET_LAYOUT_EXT = 20
    VK_DEBUG_REPORT_OBJECT_TYPE_DESCRIPTOR_UPDATE_TEMPLATE_EXT = 1000085000
    VK_DEBUG_REPORT_OBJECT_TYPE_DEVICE_EXT = 3
    VK_DEBUG_REPORT_OBJECT_TYPE_DEVICE_MEMORY_EXT = 8
    VK_DEBUG_REPORT_OBJECT_TYPE_DISPLAY_KHR_EXT = 29
    VK_DEBUG_REPORT_OBJECT_TYPE_DISPLAY_MODE_KHR_EXT = 30
    VK_DEBUG_REPORT_OBJECT_TYPE_EVENT_EXT = 11
    VK_DEBUG_REPORT_OBJECT_TYPE_FENCE_EXT = 7
    VK_DEBUG_REPORT_OBJECT_TYPE_FRAMEBUFFER_EXT = 24
    VK_DEBUG_REPORT_OBJECT_TYPE_IMAGE_EXT = 10
    VK_DEBUG_REPORT_OBJECT_TYPE_IMAGE_VIEW_EXT = 14
    VK_DEBUG_REPORT_OBJECT_TYPE_INSTANCE_EXT = 1
    VK_DEBUG_REPORT_OBJECT_TYPE_PHYSICAL_DEVICE_EXT = 2
    VK_DEBUG_REPORT_OBJECT_TYPE_PIPELINE_CACHE_EXT = 16
    VK_DEBUG_REPORT_OBJECT_TYPE_PIPELINE_EXT = 19
    VK_DEBUG_REPORT_OBJECT_TYPE_PIPELINE_LAYOUT_EXT = 17
    VK_DEBUG_REPORT_OBJECT_TYPE_QUERY_POOL_EXT = 12
    VK_DEBUG_REPORT_OBJECT_TYPE_QUEUE_EXT = 4
    VK_DEBUG_REPORT_OBJECT_TYPE_RENDER_PASS_EXT = 18
    VK_DEBUG_REPORT_OBJECT_TYPE_SAMPLER_EXT = 21
    VK_DEBUG_REPORT_OBJECT_TYPE_SAMPLER_YCBCR_CONVERSION_EXT = 1000156000
    VK_DEBUG_REPORT_OBJECT_TYPE_SEMAPHORE_EXT = 5
    VK_DEBUG_REPORT_OBJECT_TYPE_SHADER_MODULE_EXT = 15
    VK_DEBUG_REPORT_OBJECT_TYPE_SURFACE_KHR_EXT = 26
    VK_DEBUG_REPORT_OBJECT_TYPE_SWAPCHAIN_KHR_EXT = 27
    VK_DEBUG_REPORT_OBJECT_TYPE_UNKNOWN_EXT = 0
    VK_DEBUG_REPORT_OBJECT_TYPE_VALIDATION_CACHE_EXT_EXT = 33
    VK_DEBUG_REPORT_OBJECT_TYPE_DEBUG_REPORT_EXT = VK_DEBUG_REPORT_OBJECT_TYPE_DEBUG_REPORT_CALLBACK_EXT_EXT
    VK_DEBUG_REPORT_OBJECT_TYPE_DESCRIPTOR_UPDATE_TEMPLATE_KHR_EXT = VK_DEBUG_REPORT_OBJECT_TYPE_DESCRIPTOR_UPDATE_TEMPLATE_EXT
    VK_DEBUG_REPORT_OBJECT_TYPE_SAMPLER_YCBCR_CONVERSION_KHR_EXT = VK_DEBUG_REPORT_OBJECT_TYPE_SAMPLER_YCBCR_CONVERSION_EXT
    VK_DEBUG_REPORT_OBJECT_TYPE_VALIDATION_CACHE_EXT = VK_DEBUG_REPORT_OBJECT_TYPE_VALIDATION_CACHE_EXT_EXT