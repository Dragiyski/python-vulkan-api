import ctypes

class VkConformanceVersion(ctypes.Structure):
    _fields_ = [
        ('major', ctypes.c_uint8),
        ('minor', ctypes.c_uint8),
        ('subminor', ctypes.c_uint8),
        ('patch', ctypes.c_uint8),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkPhysicalDeviceDriverProperties',
        'VkPhysicalDeviceVulkan12Properties',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'major': 'major',
        'minor': 'minor',
        'subminor': 'subminor',
        'patch': 'patch',
    }
    _vk_versions_ = {
        (1, 2),
    }
    _vk_extensions_ = set()
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkConformanceVersion._type_ = {
    'major': ctypes.c_uint8,
    'minor': ctypes.c_uint8,
    'subminor': ctypes.c_uint8,
    'patch': ctypes.c_uint8,
}
