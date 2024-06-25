import ctypes

class VkRenderPassFragmentDensityMapCreateInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'fragmentDensityMapAttachment': VkAttachmentReference,
        }


from .VkAttachmentReference import VkAttachmentReference

VkRenderPassFragmentDensityMapCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('fragmentDensityMapAttachment', VkAttachmentReference),
]
