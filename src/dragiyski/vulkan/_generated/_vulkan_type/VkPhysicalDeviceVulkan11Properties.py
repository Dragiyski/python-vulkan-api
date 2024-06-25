import ctypes

class VkPhysicalDeviceVulkan11Properties(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('deviceUUID', ctypes.ARRAY(ctypes.c_uint8, 16)),
        ('driverUUID', ctypes.ARRAY(ctypes.c_uint8, 16)),
        ('deviceLUID', ctypes.ARRAY(ctypes.c_uint8, 8)),
        ('deviceNodeMask', ctypes.c_uint32),
        ('deviceLUIDValid', ctypes.c_uint32),
        ('subgroupSize', ctypes.c_uint32),
        ('subgroupSupportedStages', ctypes.c_uint32),
        ('subgroupSupportedOperations', ctypes.c_uint32),
        ('subgroupQuadOperationsInAllStages', ctypes.c_uint32),
        ('pointClippingBehavior', ctypes.c_int),
        ('maxMultiviewViewCount', ctypes.c_uint32),
        ('maxMultiviewInstanceIndex', ctypes.c_uint32),
        ('protectedNoFault', ctypes.c_uint32),
        ('maxPerSetDescriptors', ctypes.c_uint32),
        ('maxMemoryAllocationSize', ctypes.c_uint64),
    ]

VkPhysicalDeviceVulkan11Properties._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'deviceUUID': ctypes.ARRAY(ctypes.c_uint8, 16),
    'driverUUID': ctypes.ARRAY(ctypes.c_uint8, 16),
    'deviceLUID': ctypes.ARRAY(ctypes.c_uint8, 8),
    'deviceNodeMask': ctypes.c_uint32,
    'deviceLUIDValid': ctypes.c_uint32,
    'subgroupSize': ctypes.c_uint32,
    'subgroupSupportedStages': ctypes.c_uint32,
    'subgroupSupportedOperations': ctypes.c_uint32,
    'subgroupQuadOperationsInAllStages': ctypes.c_uint32,
    'pointClippingBehavior': ctypes.c_int,
    'maxMultiviewViewCount': ctypes.c_uint32,
    'maxMultiviewInstanceIndex': ctypes.c_uint32,
    'protectedNoFault': ctypes.c_uint32,
    'maxPerSetDescriptors': ctypes.c_uint32,
    'maxMemoryAllocationSize': ctypes.c_uint64,
}
