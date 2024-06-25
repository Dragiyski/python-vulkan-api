import ctypes

class VkDeviceGroupSubmitInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('waitSemaphoreCount', ctypes.c_uint32),
        ('pWaitSemaphoreDeviceIndices', ctypes.POINTER(ctypes.c_uint32)),
        ('commandBufferCount', ctypes.c_uint32),
        ('pCommandBufferDeviceMasks', ctypes.POINTER(ctypes.c_uint32)),
        ('signalSemaphoreCount', ctypes.c_uint32),
        ('pSignalSemaphoreDeviceIndices', ctypes.POINTER(ctypes.c_uint32)),
    ]

VkDeviceGroupSubmitInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'waitSemaphoreCount': ctypes.c_uint32,
    'pWaitSemaphoreDeviceIndices': ctypes.POINTER(ctypes.c_uint32),
    'commandBufferCount': ctypes.c_uint32,
    'pCommandBufferDeviceMasks': ctypes.POINTER(ctypes.c_uint32),
    'signalSemaphoreCount': ctypes.c_uint32,
    'pSignalSemaphoreDeviceIndices': ctypes.POINTER(ctypes.c_uint32),
}
