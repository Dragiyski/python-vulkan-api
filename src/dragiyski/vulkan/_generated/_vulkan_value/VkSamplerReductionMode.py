from enum import IntEnum

class Value(IntEnum):
    VK_SAMPLER_REDUCTION_MODE_MAX = 2
    VK_SAMPLER_REDUCTION_MODE_MIN = 1
    VK_SAMPLER_REDUCTION_MODE_WEIGHTED_AVERAGE = 0
    VK_SAMPLER_REDUCTION_MODE_WEIGHTED_AVERAGE_RANGECLAMP_QCOM = 1000521000
    VK_SAMPLER_REDUCTION_MODE_MAX_EXT = VK_SAMPLER_REDUCTION_MODE_MAX
    VK_SAMPLER_REDUCTION_MODE_MIN_EXT = VK_SAMPLER_REDUCTION_MODE_MIN
    VK_SAMPLER_REDUCTION_MODE_WEIGHTED_AVERAGE_EXT = VK_SAMPLER_REDUCTION_MODE_WEIGHTED_AVERAGE
