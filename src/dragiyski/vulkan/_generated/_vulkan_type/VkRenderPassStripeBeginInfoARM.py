import ctypes

class VkRenderPassStripeBeginInfoARM(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkRenderPassBeginInfo',
        'VkRenderingInfo',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkRenderPassStripeInfoARM',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'stripeInfoCount': 'stripe_info_count',
        'pStripeInfos': 'stripe_infos',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_ARM_render_pass_striped',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_RENDER_PASS_STRIPE_BEGIN_INFO_ARM'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDER_PASS_STRIPE_BEGIN_INFO_ARM
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkRenderPassStripeInfoARM import VkRenderPassStripeInfoARM

VkRenderPassStripeBeginInfoARM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stripeInfoCount', ctypes.c_uint32),
    ('pStripeInfos', ctypes.POINTER(VkRenderPassStripeInfoARM)),
]

VkRenderPassStripeBeginInfoARM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'stripeInfoCount': ctypes.c_uint32,
    'pStripeInfos': ctypes.POINTER(VkRenderPassStripeInfoARM),
}
