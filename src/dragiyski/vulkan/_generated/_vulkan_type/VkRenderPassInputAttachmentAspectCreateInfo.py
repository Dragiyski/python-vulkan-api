import ctypes

class VkRenderPassInputAttachmentAspectCreateInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'aspectReferenceCount': ctypes.c_uint32,
            'pAspectReferences': ctypes.POINTER(VkInputAttachmentAspectReference),
        }


from .VkInputAttachmentAspectReference import VkInputAttachmentAspectReference

VkRenderPassInputAttachmentAspectCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('aspectReferenceCount', ctypes.c_uint32),
    ('pAspectReferences', ctypes.POINTER(VkInputAttachmentAspectReference)),
]
