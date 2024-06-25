import ctypes

class VkBindSparseInfo(ctypes.Structure):
    pass

from .VkSparseBufferMemoryBindInfo import VkSparseBufferMemoryBindInfo
from .VkSparseImageMemoryBindInfo import VkSparseImageMemoryBindInfo
from .VkSparseImageOpaqueMemoryBindInfo import VkSparseImageOpaqueMemoryBindInfo

VkBindSparseInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('waitSemaphoreCount', ctypes.c_uint32),
    ('pWaitSemaphores', ctypes.POINTER(ctypes.c_void_p)),
    ('bufferBindCount', ctypes.c_uint32),
    ('pBufferBinds', ctypes.POINTER(VkSparseBufferMemoryBindInfo)),
    ('imageOpaqueBindCount', ctypes.c_uint32),
    ('pImageOpaqueBinds', ctypes.POINTER(VkSparseImageOpaqueMemoryBindInfo)),
    ('imageBindCount', ctypes.c_uint32),
    ('pImageBinds', ctypes.POINTER(VkSparseImageMemoryBindInfo)),
    ('signalSemaphoreCount', ctypes.c_uint32),
    ('pSignalSemaphores', ctypes.POINTER(ctypes.c_void_p)),
]

VkBindSparseInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'waitSemaphoreCount': ctypes.c_uint32,
    'pWaitSemaphores': ctypes.POINTER(ctypes.c_void_p),
    'bufferBindCount': ctypes.c_uint32,
    'pBufferBinds': ctypes.POINTER(VkSparseBufferMemoryBindInfo),
    'imageOpaqueBindCount': ctypes.c_uint32,
    'pImageOpaqueBinds': ctypes.POINTER(VkSparseImageOpaqueMemoryBindInfo),
    'imageBindCount': ctypes.c_uint32,
    'pImageBinds': ctypes.POINTER(VkSparseImageMemoryBindInfo),
    'signalSemaphoreCount': ctypes.c_uint32,
    'pSignalSemaphores': ctypes.POINTER(ctypes.c_void_p),
}
