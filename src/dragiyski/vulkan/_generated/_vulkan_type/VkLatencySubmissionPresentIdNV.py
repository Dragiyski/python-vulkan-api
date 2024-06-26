import ctypes

class VkLatencySubmissionPresentIdNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('presentID', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = {
        'VkSubmitInfo',
        'VkSubmitInfo2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'presentID': 'present_id',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_low_latency2',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_LATENCY_SUBMISSION_PRESENT_ID_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_LATENCY_SUBMISSION_PRESENT_ID_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkLatencySubmissionPresentIdNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'presentID': ctypes.c_uint64,
}
