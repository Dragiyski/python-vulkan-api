import ctypes

class VkLayerProperties(ctypes.Structure):
    _fields_ = [
        ('layerName', ctypes.ARRAY(ctypes.c_char, 256)),
        ('specVersion', ctypes.c_uint32),
        ('implementationVersion', ctypes.c_uint32),
        ('description', ctypes.ARRAY(ctypes.c_char, 256)),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkEnumerateDeviceLayerProperties',
        'vkEnumerateInstanceLayerProperties',
    }
    _python_name_ = {
        'layerName': 'layer_name',
        'specVersion': 'spec_version',
        'implementationVersion': 'implementation_version',
        'description': 'description',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkLayerProperties._type_ = {
    'layerName': ctypes.ARRAY(ctypes.c_char, 256),
    'specVersion': ctypes.c_uint32,
    'implementationVersion': ctypes.c_uint32,
    'description': ctypes.ARRAY(ctypes.c_char, 256),
}
