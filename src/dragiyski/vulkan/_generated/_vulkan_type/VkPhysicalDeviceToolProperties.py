import ctypes

class VkPhysicalDeviceToolProperties(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('name', ctypes.ARRAY(ctypes.c_char, 256)),
        ('version', ctypes.ARRAY(ctypes.c_char, 256)),
        ('purposes', ctypes.c_uint32),
        ('description', ctypes.ARRAY(ctypes.c_char, 256)),
        ('layer', ctypes.ARRAY(ctypes.c_char, 256)),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetPhysicalDeviceToolProperties',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'name': 'name',
        'version': 'version',
        'purposes': 'purposes',
        'description': 'description',
        'layer': 'layer',
    }
    _vk_versions_ = {
        (1, 3),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'purposes': 'VkToolPurposeFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TOOL_PROPERTIES'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TOOL_PROPERTIES
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceToolProperties._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'name': ctypes.ARRAY(ctypes.c_char, 256),
    'version': ctypes.ARRAY(ctypes.c_char, 256),
    'purposes': ctypes.c_uint32,
    'description': ctypes.ARRAY(ctypes.c_char, 256),
    'layer': ctypes.ARRAY(ctypes.c_char, 256),
}
