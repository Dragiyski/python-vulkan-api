import ctypes

class VkVideoDecodeH265SessionParametersCreateInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkVideoSessionParametersCreateInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkVideoDecodeH265SessionParametersAddInfoKHR',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'maxStdVPSCount': 'max_std_vpscount',
        'maxStdSPSCount': 'max_std_spscount',
        'maxStdPPSCount': 'max_std_ppscount',
        'pParametersAddInfo': 'parameters_add_info',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_decode_h265',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_DECODE_H265_SESSION_PARAMETERS_CREATE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_H265_SESSION_PARAMETERS_CREATE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkVideoDecodeH265SessionParametersAddInfoKHR import VkVideoDecodeH265SessionParametersAddInfoKHR

VkVideoDecodeH265SessionParametersCreateInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('maxStdVPSCount', ctypes.c_uint32),
    ('maxStdSPSCount', ctypes.c_uint32),
    ('maxStdPPSCount', ctypes.c_uint32),
    ('pParametersAddInfo', ctypes.POINTER(VkVideoDecodeH265SessionParametersAddInfoKHR)),
]

VkVideoDecodeH265SessionParametersCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxStdVPSCount': ctypes.c_uint32,
    'maxStdSPSCount': ctypes.c_uint32,
    'maxStdPPSCount': ctypes.c_uint32,
    'pParametersAddInfo': ctypes.POINTER(VkVideoDecodeH265SessionParametersAddInfoKHR),
}
