import ctypes

class VkRenderPassMultiviewCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('subpassCount', ctypes.c_uint32),
        ('pViewMasks', ctypes.POINTER(ctypes.c_uint32)),
        ('dependencyCount', ctypes.c_uint32),
        ('pViewOffsets', ctypes.POINTER(ctypes.c_int32)),
        ('correlationMaskCount', ctypes.c_uint32),
        ('pCorrelationMasks', ctypes.POINTER(ctypes.c_uint32)),
    ]

VkRenderPassMultiviewCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'subpassCount': ctypes.c_uint32,
    'pViewMasks': ctypes.POINTER(ctypes.c_uint32),
    'dependencyCount': ctypes.c_uint32,
    'pViewOffsets': ctypes.POINTER(ctypes.c_int32),
    'correlationMaskCount': ctypes.c_uint32,
    'pCorrelationMasks': ctypes.POINTER(ctypes.c_uint32),
}
