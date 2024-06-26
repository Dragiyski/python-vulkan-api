import ctypes

class VkDeviceAddressBindingCallbackDataEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('baseAddress', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
        ('bindingType', ctypes.c_int),
    ]

    _init_ = []
    _extends_ = {
        'VkDebugUtilsMessengerCallbackDataEXT',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'baseAddress': 'base_address',
        'size': 'size',
        'bindingType': 'binding_type',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_device_address_binding_report',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkDeviceAddressBindingFlagsEXT',
        'bindingType': 'VkDeviceAddressBindingTypeEXT',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DEVICE_ADDRESS_BINDING_CALLBACK_DATA_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_ADDRESS_BINDING_CALLBACK_DATA_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkDeviceAddressBindingCallbackDataEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'baseAddress': ctypes.c_uint64,
    'size': ctypes.c_uint64,
    'bindingType': ctypes.c_int,
}
