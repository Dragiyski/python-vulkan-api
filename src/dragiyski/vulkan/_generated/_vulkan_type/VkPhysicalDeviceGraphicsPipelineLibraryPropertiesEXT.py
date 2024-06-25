import ctypes

class VkPhysicalDeviceGraphicsPipelineLibraryPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('graphicsPipelineLibraryFastLinking', ctypes.c_uint32),
        ('graphicsPipelineLibraryIndependentInterpolationDecoration', ctypes.c_uint32),
    ]

VkPhysicalDeviceGraphicsPipelineLibraryPropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'graphicsPipelineLibraryFastLinking': ctypes.c_uint32,
    'graphicsPipelineLibraryIndependentInterpolationDecoration': ctypes.c_uint32,
}
