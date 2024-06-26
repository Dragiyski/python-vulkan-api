import ctypes

class VkAabbPositionsKHR(ctypes.Structure):
    _fields_ = [
        ('minX', ctypes.c_float),
        ('minY', ctypes.c_float),
        ('minZ', ctypes.c_float),
        ('maxX', ctypes.c_float),
        ('maxY', ctypes.c_float),
        ('maxZ', ctypes.c_float),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'minX': 'min_x',
        'minY': 'min_y',
        'minZ': 'min_z',
        'maxX': 'max_x',
        'maxY': 'max_y',
        'maxZ': 'max_z',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_acceleration_structure',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkAabbPositionsKHR._type_ = {
    'minX': ctypes.c_float,
    'minY': ctypes.c_float,
    'minZ': ctypes.c_float,
    'maxX': ctypes.c_float,
    'maxY': ctypes.c_float,
    'maxZ': ctypes.c_float,
}
