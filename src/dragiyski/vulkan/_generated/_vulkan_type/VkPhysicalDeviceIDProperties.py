import ctypes

class VkPhysicalDeviceIDProperties(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('deviceUUID', ctypes.ARRAY(ctypes.c_uint8, 16)),
        ('driverUUID', ctypes.ARRAY(ctypes.c_uint8, 16)),
        ('deviceLUID', ctypes.ARRAY(ctypes.c_uint8, 8)),
        ('deviceNodeMask', ctypes.c_uint32),
        ('deviceLUIDValid', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkPhysicalDeviceProperties2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'deviceUUID': 'device_uuid',
        'driverUUID': 'driver_uuid',
        'deviceLUID': 'device_luid',
        'deviceNodeMask': 'device_node_mask',
        'deviceLUIDValid': 'device_luidvalid',
    }
    _vk_versions_ = {
        (1, 1),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ID_PROPERTIES'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ID_PROPERTIES
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceIDProperties._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'deviceUUID': ctypes.ARRAY(ctypes.c_uint8, 16),
    'driverUUID': ctypes.ARRAY(ctypes.c_uint8, 16),
    'deviceLUID': ctypes.ARRAY(ctypes.c_uint8, 8),
    'deviceNodeMask': ctypes.c_uint32,
    'deviceLUIDValid': ctypes.c_uint32,
}
