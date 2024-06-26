import ctypes

class VkPhysicalDeviceGroupProperties(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('physicalDeviceCount', ctypes.c_uint32),
        ('physicalDevices', ctypes.ARRAY(ctypes.c_void_p, 32)),
        ('subsetAllocation', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkEnumeratePhysicalDeviceGroups',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'physicalDeviceCount': 'physical_device_count',
        'physicalDevices': 'physical_devices',
        'subsetAllocation': 'subset_allocation',
    }
    _vk_versions_ = {
        (1, 1),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_GROUP_PROPERTIES'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_GROUP_PROPERTIES
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceGroupProperties._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'physicalDeviceCount': ctypes.c_uint32,
    'physicalDevices': ctypes.ARRAY(ctypes.c_void_p, 32),
    'subsetAllocation': ctypes.c_uint32,
}
