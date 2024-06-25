import ctypes

class VkPhysicalDeviceImageCompressionControlSwapchainFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('imageCompressionControlSwapchain', ctypes.c_uint32),
    ]

VkPhysicalDeviceImageCompressionControlSwapchainFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'imageCompressionControlSwapchain': ctypes.c_uint32,
}
