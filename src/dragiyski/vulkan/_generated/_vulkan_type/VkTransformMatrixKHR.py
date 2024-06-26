import ctypes

class VkTransformMatrixKHR(ctypes.Structure):
    _fields_ = [
        ('matrix', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_float, 4), 3)),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkAccelerationStructureInstanceKHR',
        'VkAccelerationStructureMatrixMotionInstanceNV',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'matrix': 'matrix',
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

VkTransformMatrixKHR._type_ = {
    'matrix': ctypes.ARRAY(ctypes.ARRAY(ctypes.c_float, 4), 3),
}
