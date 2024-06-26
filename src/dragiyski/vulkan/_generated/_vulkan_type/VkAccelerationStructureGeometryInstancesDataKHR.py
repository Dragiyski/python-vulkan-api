import ctypes

class VkAccelerationStructureGeometryInstancesDataKHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkDeviceOrHostAddressConstKHR',
    }
    _included_in_ = {
        'VkAccelerationStructureGeometryDataKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'arrayOfPointers': 'array_of_pointers',
        'data': 'data',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_acceleration_structure',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_GEOMETRY_INSTANCES_DATA_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_GEOMETRY_INSTANCES_DATA_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkDeviceOrHostAddressConstKHR import VkDeviceOrHostAddressConstKHR

VkAccelerationStructureGeometryInstancesDataKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('arrayOfPointers', ctypes.c_uint32),
    ('data', VkDeviceOrHostAddressConstKHR),
]

VkAccelerationStructureGeometryInstancesDataKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'arrayOfPointers': ctypes.c_uint32,
    'data': VkDeviceOrHostAddressConstKHR,
}
