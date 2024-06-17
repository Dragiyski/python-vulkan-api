import ctypes
from .vulkan_base import VKAPI_PTR, VKAPI_CALL
from ._vulkan_type import VkDebugUtilsMessengerCallbackDataEXT
from ._vulkan_type import VkDeviceMemoryReportCallbackDataEXT
from ._vulkan_type import VkFaultData

vkAllocationFunction = VKAPI_PTR(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_int)
vkDebugReportCallbackEXT = VKAPI_PTR(ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int, ctypes.c_uint64, ctypes.c_size_t, ctypes.c_int32, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_void_p)
vkDebugUtilsMessengerCallbackEXT = VKAPI_PTR(ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkDebugUtilsMessengerCallbackDataEXT), ctypes.c_void_p)
vkDeviceMemoryReportCallbackEXT = VKAPI_PTR(None, ctypes.POINTER(VkDeviceMemoryReportCallbackDataEXT), ctypes.c_void_p)
vkFaultCallbackFunction = VKAPI_PTR(None, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkFaultData))
vkFreeFunction = VKAPI_PTR(None, ctypes.c_void_p, ctypes.c_void_p)
vkVoidFunction = VKAPI_PTR(None)
vkGetInstanceProcAddrLUNARG = VKAPI_PTR(ctypes.POINTER(vkVoidFunction), ctypes.c_void_p, ctypes.c_char_p)
vkInternalAllocationNotification = VKAPI_PTR(None, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_int, ctypes.c_int)
vkInternalFreeNotification = VKAPI_PTR(None, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_int, ctypes.c_int)
vkReallocationFunction = VKAPI_PTR(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_int)


__all__ = [
    'vkAllocationFunction',
    'vkDebugReportCallbackEXT',
    'vkDebugUtilsMessengerCallbackEXT',
    'vkDeviceMemoryReportCallbackEXT',
    'vkFaultCallbackFunction',
    'vkFreeFunction',
    'vkGetInstanceProcAddrLUNARG',
    'vkInternalAllocationNotification',
    'vkInternalFreeNotification',
    'vkReallocationFunction',
    'vkVoidFunction',
]
