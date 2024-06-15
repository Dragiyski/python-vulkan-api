import ctypes
from ._vulkan_base import VKAPI_PTR, VKAPI_CALL
from ._struct import VkDebugUtilsMessengerCallbackDataEXT
from ._struct import VkFaultData
from ._struct import VkDeviceMemoryReportCallbackDataEXT

vkInternalAllocationNotification = VKAPI_PTR(None, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_int, ctypes.c_int)
vkInternalFreeNotification = VKAPI_PTR(None, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_int, ctypes.c_int)
vkReallocationFunction = VKAPI_PTR(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_int)
vkAllocationFunction = VKAPI_PTR(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_int)
vkFreeFunction = VKAPI_PTR(None, ctypes.c_void_p, ctypes.c_void_p)
vkVoidFunction = VKAPI_PTR(None)
vkDebugReportCallbackEXT = VKAPI_PTR(ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int, ctypes.c_uint64, ctypes.c_size_t, ctypes.c_int32, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_void_p)
vkDebugUtilsMessengerCallbackEXT = VKAPI_PTR(ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkDebugUtilsMessengerCallbackDataEXT), ctypes.c_void_p)
vkFaultCallbackFunction = VKAPI_PTR(None, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkFaultData))
vkDeviceMemoryReportCallbackEXT = VKAPI_PTR(None, ctypes.POINTER(VkDeviceMemoryReportCallbackDataEXT), ctypes.c_void_p)
vkGetInstanceProcAddrLUNARG = VKAPI_PTR(ctypes.POINTER(vkVoidFunction), ctypes.c_void_p, ctypes.c_char_p)

__all__ = [
    'vkInternalAllocationNotification',
    'vkInternalFreeNotification',
    'vkReallocationFunction',
    'vkAllocationFunction',
    'vkFreeFunction',
    'vkVoidFunction',
    'vkDebugReportCallbackEXT',
    'vkDebugUtilsMessengerCallbackEXT',
    'vkFaultCallbackFunction',
    'vkDeviceMemoryReportCallbackEXT',
    'vkGetInstanceProcAddrLUNARG',
]
