import ctypes

class VkApplicationInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pApplicationName', ctypes.c_char_p),
        ('applicationVersion', ctypes.c_uint32),
        ('pEngineName', ctypes.c_char_p),
        ('engineVersion', ctypes.c_uint32),
        ('apiVersion', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkInstanceCreateInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'pApplicationName': 'application_name',
        'applicationVersion': 'application_version',
        'pEngineName': 'engine_name',
        'engineVersion': 'engine_version',
        'apiVersion': 'api_version',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_APPLICATION_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_APPLICATION_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkApplicationInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pApplicationName': ctypes.c_char_p,
    'applicationVersion': ctypes.c_uint32,
    'pEngineName': ctypes.c_char_p,
    'engineVersion': ctypes.c_uint32,
    'apiVersion': ctypes.c_uint32,
}
