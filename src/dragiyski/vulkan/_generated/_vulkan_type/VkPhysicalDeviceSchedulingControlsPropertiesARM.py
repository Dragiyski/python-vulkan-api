import ctypes

class VkPhysicalDeviceSchedulingControlsPropertiesARM(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('schedulingControlsFlags', ctypes.c_uint64),
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
        'schedulingControlsFlags': 'scheduling_controls_flags',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_ARM_scheduling_controls',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'schedulingControlsFlags': 'VkPhysicalDeviceSchedulingControlsFlagsARM',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SCHEDULING_CONTROLS_PROPERTIES_ARM'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SCHEDULING_CONTROLS_PROPERTIES_ARM
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceSchedulingControlsPropertiesARM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'schedulingControlsFlags': ctypes.c_uint64,
}
