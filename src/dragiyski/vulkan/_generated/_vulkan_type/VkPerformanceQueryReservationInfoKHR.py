import ctypes

class VkPerformanceQueryReservationInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxPerformanceQueriesPerPool', ctypes.c_uint32),
    ]

VkPerformanceQueryReservationInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxPerformanceQueriesPerPool': ctypes.c_uint32,
}
