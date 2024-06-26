from enum import IntFlag

class VkPipelineStageFlags(IntFlag):
    VK_PIPELINE_STAGE_ACCELERATION_STRUCTURE_BUILD_BIT_KHR = 33554432
    VK_PIPELINE_STAGE_ALL_COMMANDS_BIT = 65536
    VK_PIPELINE_STAGE_ALL_GRAPHICS_BIT = 32768
    VK_PIPELINE_STAGE_BOTTOM_OF_PIPE_BIT = 8192
    VK_PIPELINE_STAGE_COLOR_ATTACHMENT_OUTPUT_BIT = 1024
    VK_PIPELINE_STAGE_COMMAND_PREPROCESS_BIT_NV = 131072
    VK_PIPELINE_STAGE_COMPUTE_SHADER_BIT = 2048
    VK_PIPELINE_STAGE_CONDITIONAL_RENDERING_BIT_EXT = 262144
    VK_PIPELINE_STAGE_DRAW_INDIRECT_BIT = 2
    VK_PIPELINE_STAGE_EARLY_FRAGMENT_TESTS_BIT = 256
    VK_PIPELINE_STAGE_FRAGMENT_DENSITY_PROCESS_BIT_EXT = 8388608
    VK_PIPELINE_STAGE_FRAGMENT_SHADER_BIT = 128
    VK_PIPELINE_STAGE_FRAGMENT_SHADING_RATE_ATTACHMENT_BIT_KHR = 4194304
    VK_PIPELINE_STAGE_GEOMETRY_SHADER_BIT = 64
    VK_PIPELINE_STAGE_HOST_BIT = 16384
    VK_PIPELINE_STAGE_LATE_FRAGMENT_TESTS_BIT = 512
    VK_PIPELINE_STAGE_MESH_SHADER_BIT_EXT = 1048576
    VK_PIPELINE_STAGE_NONE = 0
    VK_PIPELINE_STAGE_RAY_TRACING_SHADER_BIT_KHR = 2097152
    VK_PIPELINE_STAGE_TASK_SHADER_BIT_EXT = 524288
    VK_PIPELINE_STAGE_TESSELLATION_CONTROL_SHADER_BIT = 16
    VK_PIPELINE_STAGE_TESSELLATION_EVALUATION_SHADER_BIT = 32
    VK_PIPELINE_STAGE_TOP_OF_PIPE_BIT = 1
    VK_PIPELINE_STAGE_TRANSFER_BIT = 4096
    VK_PIPELINE_STAGE_TRANSFORM_FEEDBACK_BIT_EXT = 16777216
    VK_PIPELINE_STAGE_VERTEX_INPUT_BIT = 4
    VK_PIPELINE_STAGE_VERTEX_SHADER_BIT = 8
    VK_PIPELINE_STAGE_ACCELERATION_STRUCTURE_BUILD_BIT_NV = VK_PIPELINE_STAGE_ACCELERATION_STRUCTURE_BUILD_BIT_KHR
    VK_PIPELINE_STAGE_MESH_SHADER_BIT_NV = VK_PIPELINE_STAGE_MESH_SHADER_BIT_EXT
    VK_PIPELINE_STAGE_NONE_KHR = VK_PIPELINE_STAGE_NONE
    VK_PIPELINE_STAGE_RAY_TRACING_SHADER_BIT_NV = VK_PIPELINE_STAGE_RAY_TRACING_SHADER_BIT_KHR
    VK_PIPELINE_STAGE_SHADING_RATE_IMAGE_BIT_NV = VK_PIPELINE_STAGE_FRAGMENT_SHADING_RATE_ATTACHMENT_BIT_KHR
    VK_PIPELINE_STAGE_TASK_SHADER_BIT_NV = VK_PIPELINE_STAGE_TASK_SHADER_BIT_EXT
