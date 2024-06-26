import ctypes

class VkDirectDriverLoadingListLUNARG(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkInstanceCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkDirectDriverLoadingInfoLUNARG',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'mode': 'mode',
        'driverCount': 'driver_count',
        'pDrivers': 'drivers',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_LUNARG_direct_driver_loading',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'mode': 'VkDirectDriverLoadingModeLUNARG',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DIRECT_DRIVER_LOADING_LIST_LUNARG'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DIRECT_DRIVER_LOADING_LIST_LUNARG
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkDirectDriverLoadingInfoLUNARG import VkDirectDriverLoadingInfoLUNARG

VkDirectDriverLoadingListLUNARG._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('mode', ctypes.c_int),
    ('driverCount', ctypes.c_uint32),
    ('pDrivers', ctypes.POINTER(VkDirectDriverLoadingInfoLUNARG)),
]

VkDirectDriverLoadingListLUNARG._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'mode': ctypes.c_int,
    'driverCount': ctypes.c_uint32,
    'pDrivers': ctypes.POINTER(VkDirectDriverLoadingInfoLUNARG),
}
