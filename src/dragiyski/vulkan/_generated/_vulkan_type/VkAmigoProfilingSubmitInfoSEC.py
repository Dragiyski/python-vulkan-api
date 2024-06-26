import ctypes

class VkAmigoProfilingSubmitInfoSEC(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('firstDrawTimestamp', ctypes.c_uint64),
        ('swapBufferTimestamp', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = {
        'VkSubmitInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'firstDrawTimestamp': 'first_draw_timestamp',
        'swapBufferTimestamp': 'swap_buffer_timestamp',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_SEC_amigo_profiling',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_AMIGO_PROFILING_SUBMIT_INFO_SEC'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_AMIGO_PROFILING_SUBMIT_INFO_SEC
        for function in self._init_:
            function(self, *args, **kwargs)

VkAmigoProfilingSubmitInfoSEC._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'firstDrawTimestamp': ctypes.c_uint64,
    'swapBufferTimestamp': ctypes.c_uint64,
}
