from enum import IntEnum

class VkLatencyMarkerNV(IntEnum):
    VK_LATENCY_MARKER_INPUT_SAMPLE_NV = 6
    VK_LATENCY_MARKER_OUT_OF_BAND_PRESENT_END_NV = 11
    VK_LATENCY_MARKER_OUT_OF_BAND_PRESENT_START_NV = 10
    VK_LATENCY_MARKER_OUT_OF_BAND_RENDERSUBMIT_END_NV = 9
    VK_LATENCY_MARKER_OUT_OF_BAND_RENDERSUBMIT_START_NV = 8
    VK_LATENCY_MARKER_PRESENT_END_NV = 5
    VK_LATENCY_MARKER_PRESENT_START_NV = 4
    VK_LATENCY_MARKER_RENDERSUBMIT_END_NV = 3
    VK_LATENCY_MARKER_RENDERSUBMIT_START_NV = 2
    VK_LATENCY_MARKER_SIMULATION_END_NV = 1
    VK_LATENCY_MARKER_SIMULATION_START_NV = 0
    VK_LATENCY_MARKER_TRIGGER_FLASH_NV = 7
