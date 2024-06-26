import ctypes

class VkExtensionProperties(ctypes.Structure):
    _fields_ = [
        ('extensionName', ctypes.ARRAY(ctypes.c_char, 256)),
        ('specVersion', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkVideoCapabilitiesKHR',
        'VkVideoSessionCreateInfoKHR',
    }
    _input_of_ = set()
    _output_of_ = {
        'vkEnumerateDeviceExtensionProperties',
        'vkEnumerateInstanceExtensionProperties',
    }
    _python_name_ = {
        'extensionName': 'extension_name',
        'specVersion': 'spec_version',
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

VkExtensionProperties._type_ = {
    'extensionName': ctypes.ARRAY(ctypes.c_char, 256),
    'specVersion': ctypes.c_uint32,
}
