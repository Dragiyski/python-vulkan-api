import ctypes

class VkPhysicalDeviceDriverProperties(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkPhysicalDeviceProperties2',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkConformanceVersion',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'driverID': 'driver_id',
        'driverName': 'driver_name',
        'driverInfo': 'driver_info',
        'conformanceVersion': 'conformance_version',
    }
    _vk_versions_ = {
        (1, 2),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'driverID': 'VkDriverId',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DRIVER_PROPERTIES'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DRIVER_PROPERTIES
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkConformanceVersion import VkConformanceVersion

VkPhysicalDeviceDriverProperties._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('driverID', ctypes.c_int),
    ('driverName', ctypes.ARRAY(ctypes.c_char, 256)),
    ('driverInfo', ctypes.ARRAY(ctypes.c_char, 256)),
    ('conformanceVersion', VkConformanceVersion),
]

VkPhysicalDeviceDriverProperties._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'driverID': ctypes.c_int,
    'driverName': ctypes.ARRAY(ctypes.c_char, 256),
    'driverInfo': ctypes.ARRAY(ctypes.c_char, 256),
    'conformanceVersion': VkConformanceVersion,
}
