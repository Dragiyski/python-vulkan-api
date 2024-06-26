import ctypes

class VkPhysicalDeviceOpticalFlowPropertiesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('supportedOutputGridSizes', ctypes.c_uint32),
        ('supportedHintGridSizes', ctypes.c_uint32),
        ('hintSupported', ctypes.c_uint32),
        ('costSupported', ctypes.c_uint32),
        ('bidirectionalFlowSupported', ctypes.c_uint32),
        ('globalFlowSupported', ctypes.c_uint32),
        ('minWidth', ctypes.c_uint32),
        ('minHeight', ctypes.c_uint32),
        ('maxWidth', ctypes.c_uint32),
        ('maxHeight', ctypes.c_uint32),
        ('maxNumRegionsOfInterest', ctypes.c_uint32),
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
        'supportedOutputGridSizes': 'supported_output_grid_sizes',
        'supportedHintGridSizes': 'supported_hint_grid_sizes',
        'hintSupported': 'hint_supported',
        'costSupported': 'cost_supported',
        'bidirectionalFlowSupported': 'bidirectional_flow_supported',
        'globalFlowSupported': 'global_flow_supported',
        'minWidth': 'min_width',
        'minHeight': 'min_height',
        'maxWidth': 'max_width',
        'maxHeight': 'max_height',
        'maxNumRegionsOfInterest': 'max_num_regions_of_interest',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_optical_flow',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'supportedOutputGridSizes': 'VkOpticalFlowGridSizeFlagsNV',
        'supportedHintGridSizes': 'VkOpticalFlowGridSizeFlagsNV',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_OPTICAL_FLOW_PROPERTIES_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_OPTICAL_FLOW_PROPERTIES_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceOpticalFlowPropertiesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'supportedOutputGridSizes': ctypes.c_uint32,
    'supportedHintGridSizes': ctypes.c_uint32,
    'hintSupported': ctypes.c_uint32,
    'costSupported': ctypes.c_uint32,
    'bidirectionalFlowSupported': ctypes.c_uint32,
    'globalFlowSupported': ctypes.c_uint32,
    'minWidth': ctypes.c_uint32,
    'minHeight': ctypes.c_uint32,
    'maxWidth': ctypes.c_uint32,
    'maxHeight': ctypes.c_uint32,
    'maxNumRegionsOfInterest': ctypes.c_uint32,
}
