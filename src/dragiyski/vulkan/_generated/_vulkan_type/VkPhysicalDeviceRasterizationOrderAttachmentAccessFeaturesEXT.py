import ctypes

class VkPhysicalDeviceRasterizationOrderAttachmentAccessFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('rasterizationOrderColorAttachmentAccess', ctypes.c_uint32),
        ('rasterizationOrderDepthAttachmentAccess', ctypes.c_uint32),
        ('rasterizationOrderStencilAttachmentAccess', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkDeviceCreateInfo',
        'VkPhysicalDeviceFeatures2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'rasterizationOrderColorAttachmentAccess': 'rasterization_order_color_attachment_access',
        'rasterizationOrderDepthAttachmentAccess': 'rasterization_order_depth_attachment_access',
        'rasterizationOrderStencilAttachmentAccess': 'rasterization_order_stencil_attachment_access',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_rasterization_order_attachment_access',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RASTERIZATION_ORDER_ATTACHMENT_ACCESS_FEATURES_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RASTERIZATION_ORDER_ATTACHMENT_ACCESS_FEATURES_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceRasterizationOrderAttachmentAccessFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'rasterizationOrderColorAttachmentAccess': ctypes.c_uint32,
    'rasterizationOrderDepthAttachmentAccess': ctypes.c_uint32,
    'rasterizationOrderStencilAttachmentAccess': ctypes.c_uint32,
}
