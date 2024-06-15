import ctypes, sys

class VkPhysicalDeviceFragmentShadingRatePropertiesKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkPhysicalDeviceFragmentShadingRatePropertiesKHR

from . import VkExtent2D

VkPhysicalDeviceFragmentShadingRatePropertiesKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('minFragmentShadingRateAttachmentTexelSize', VkExtent2D),
    ('maxFragmentShadingRateAttachmentTexelSize', VkExtent2D),
    ('maxFragmentShadingRateAttachmentTexelSizeAspectRatio', ctypes.c_uint32),
    ('primitiveFragmentShadingRateWithMultipleViewports', ctypes.c_uint32),
    ('layeredShadingRateAttachments', ctypes.c_uint32),
    ('fragmentShadingRateNonTrivialCombinerOps', ctypes.c_uint32),
    ('maxFragmentSize', VkExtent2D),
    ('maxFragmentSizeAspectRatio', ctypes.c_uint32),
    ('maxFragmentShadingRateCoverageSamples', ctypes.c_uint32),
    ('maxFragmentShadingRateRasterizationSamples', ctypes.c_uint32),
    ('fragmentShadingRateWithShaderDepthStencilWrites', ctypes.c_uint32),
    ('fragmentShadingRateWithSampleMask', ctypes.c_uint32),
    ('fragmentShadingRateWithShaderSampleMask', ctypes.c_uint32),
    ('fragmentShadingRateWithConservativeRasterization', ctypes.c_uint32),
    ('fragmentShadingRateWithFragmentShaderInterlock', ctypes.c_uint32),
    ('fragmentShadingRateWithCustomSampleLocations', ctypes.c_uint32),
    ('fragmentShadingRateStrictMultiplyCombiner', ctypes.c_uint32),
]
