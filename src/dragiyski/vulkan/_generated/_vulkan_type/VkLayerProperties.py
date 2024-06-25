import ctypes

class VkLayerProperties(ctypes.Structure):
    _fields_ = [
        ('layerName', ctypes.ARRAY(ctypes.c_char, 256)),
        ('specVersion', ctypes.c_uint32),
        ('implementationVersion', ctypes.c_uint32),
        ('description', ctypes.ARRAY(ctypes.c_char, 256)),
    ]

VkLayerProperties._type_ = {
    'layerName': ctypes.ARRAY(ctypes.c_char, 256),
    'specVersion': ctypes.c_uint32,
    'implementationVersion': ctypes.c_uint32,
    'description': ctypes.ARRAY(ctypes.c_char, 256),
}
