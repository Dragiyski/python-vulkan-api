import ctypes

class VkDescriptorAddressInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('address', ctypes.c_uint64),
        ('range', ctypes.c_uint64),
        ('format', ctypes.c_int),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkDescriptorDataEXT',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'address': 'address',
        'range': 'range',
        'format': 'format',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_descriptor_buffer',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'format': 'VkFormat',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DESCRIPTOR_ADDRESS_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DESCRIPTOR_ADDRESS_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkDescriptorAddressInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'address': ctypes.c_uint64,
    'range': ctypes.c_uint64,
    'format': ctypes.c_int,
}
