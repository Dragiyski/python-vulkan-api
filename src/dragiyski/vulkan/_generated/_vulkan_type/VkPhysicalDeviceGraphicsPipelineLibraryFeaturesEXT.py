import ctypes

class VkPhysicalDeviceGraphicsPipelineLibraryFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('graphicsPipelineLibrary', ctypes.c_uint32),
    ]

VkPhysicalDeviceGraphicsPipelineLibraryFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'graphicsPipelineLibrary': ctypes.c_uint32,
}
