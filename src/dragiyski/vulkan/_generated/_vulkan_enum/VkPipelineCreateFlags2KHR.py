from enum import IntFlag

class VkPipelineCreateFlags2KHR(IntFlag):
    VK_PIPELINE_CREATE_2_ALLOW_DERIVATIVES_BIT_KHR = 2
    VK_PIPELINE_CREATE_2_CAPTURE_INTERNAL_REPRESENTATIONS_BIT_KHR = 128
    VK_PIPELINE_CREATE_2_CAPTURE_STATISTICS_BIT_KHR = 64
    VK_PIPELINE_CREATE_2_COLOR_ATTACHMENT_FEEDBACK_LOOP_BIT_EXT = 33554432
    VK_PIPELINE_CREATE_2_DEFER_COMPILE_BIT_NV = 32
    VK_PIPELINE_CREATE_2_DEPTH_STENCIL_ATTACHMENT_FEEDBACK_LOOP_BIT_EXT = 67108864
    VK_PIPELINE_CREATE_2_DERIVATIVE_BIT_KHR = 4
    VK_PIPELINE_CREATE_2_DESCRIPTOR_BUFFER_BIT_EXT = 536870912
    VK_PIPELINE_CREATE_2_DISABLE_OPTIMIZATION_BIT_KHR = 1
    VK_PIPELINE_CREATE_2_DISPATCH_BASE_BIT_KHR = 16
    VK_PIPELINE_CREATE_2_EARLY_RETURN_ON_FAILURE_BIT_KHR = 512
    VK_PIPELINE_CREATE_2_ENABLE_LEGACY_DITHERING_BIT_EXT = 17179869184
    VK_PIPELINE_CREATE_2_FAIL_ON_PIPELINE_COMPILE_REQUIRED_BIT_KHR = 256
    VK_PIPELINE_CREATE_2_INDIRECT_BINDABLE_BIT_NV = 262144
    VK_PIPELINE_CREATE_2_LIBRARY_BIT_KHR = 2048
    VK_PIPELINE_CREATE_2_LINK_TIME_OPTIMIZATION_BIT_EXT = 1024
    VK_PIPELINE_CREATE_2_NO_PROTECTED_ACCESS_BIT_EXT = 134217728
    VK_PIPELINE_CREATE_2_PROTECTED_ACCESS_ONLY_BIT_EXT = 1073741824
    VK_PIPELINE_CREATE_2_RAY_TRACING_ALLOW_MOTION_BIT_NV = 1048576
    VK_PIPELINE_CREATE_2_RAY_TRACING_DISPLACEMENT_MICROMAP_BIT_NV = 268435456
    VK_PIPELINE_CREATE_2_RAY_TRACING_NO_NULL_ANY_HIT_SHADERS_BIT_KHR = 16384
    VK_PIPELINE_CREATE_2_RAY_TRACING_NO_NULL_CLOSEST_HIT_SHADERS_BIT_KHR = 32768
    VK_PIPELINE_CREATE_2_RAY_TRACING_NO_NULL_INTERSECTION_SHADERS_BIT_KHR = 131072
    VK_PIPELINE_CREATE_2_RAY_TRACING_NO_NULL_MISS_SHADERS_BIT_KHR = 65536
    VK_PIPELINE_CREATE_2_RAY_TRACING_OPACITY_MICROMAP_BIT_EXT = 16777216
    VK_PIPELINE_CREATE_2_RAY_TRACING_SHADER_GROUP_HANDLE_CAPTURE_REPLAY_BIT_KHR = 524288
    VK_PIPELINE_CREATE_2_RAY_TRACING_SKIP_AABBS_BIT_KHR = 8192
    VK_PIPELINE_CREATE_2_RAY_TRACING_SKIP_TRIANGLES_BIT_KHR = 4096
    VK_PIPELINE_CREATE_2_RENDERING_FRAGMENT_DENSITY_MAP_ATTACHMENT_BIT_EXT = 4194304
    VK_PIPELINE_CREATE_2_RENDERING_FRAGMENT_SHADING_RATE_ATTACHMENT_BIT_KHR = 2097152
    VK_PIPELINE_CREATE_2_RETAIN_LINK_TIME_OPTIMIZATION_INFO_BIT_EXT = 8388608
    VK_PIPELINE_CREATE_2_VIEW_INDEX_FROM_DEVICE_INDEX_BIT_KHR = 8