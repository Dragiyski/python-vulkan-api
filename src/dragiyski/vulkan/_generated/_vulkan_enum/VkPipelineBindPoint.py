from enum import IntEnum

class VkPipelineBindPoint(IntEnum):
    VK_PIPELINE_BIND_POINT_COMPUTE = 1
    VK_PIPELINE_BIND_POINT_EXECUTION_GRAPH_AMDX = 1000134000
    VK_PIPELINE_BIND_POINT_GRAPHICS = 0
    VK_PIPELINE_BIND_POINT_RAY_TRACING_KHR = 1000165000
    VK_PIPELINE_BIND_POINT_SUBPASS_SHADING_HUAWEI = 1000369003
    VK_PIPELINE_BIND_POINT_RAY_TRACING_NV = VK_PIPELINE_BIND_POINT_RAY_TRACING_KHR
