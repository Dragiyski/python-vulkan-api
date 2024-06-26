from enum import IntEnum

class VkShaderFloatControlsIndependence(IntEnum):
    VK_SHADER_FLOAT_CONTROLS_INDEPENDENCE_32_BIT_ONLY = 0
    VK_SHADER_FLOAT_CONTROLS_INDEPENDENCE_ALL = 1
    VK_SHADER_FLOAT_CONTROLS_INDEPENDENCE_NONE = 2
    VK_SHADER_FLOAT_CONTROLS_INDEPENDENCE_32_BIT_ONLY_KHR = VK_SHADER_FLOAT_CONTROLS_INDEPENDENCE_32_BIT_ONLY
    VK_SHADER_FLOAT_CONTROLS_INDEPENDENCE_ALL_KHR = VK_SHADER_FLOAT_CONTROLS_INDEPENDENCE_ALL
    VK_SHADER_FLOAT_CONTROLS_INDEPENDENCE_NONE_KHR = VK_SHADER_FLOAT_CONTROLS_INDEPENDENCE_NONE
