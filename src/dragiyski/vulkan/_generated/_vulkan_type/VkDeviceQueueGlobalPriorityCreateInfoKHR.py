import ctypes

class VkDeviceQueueGlobalPriorityCreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('globalPriority', ctypes.c_int),
    ]

VkDeviceQueueGlobalPriorityCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'globalPriority': ctypes.c_int,
}
