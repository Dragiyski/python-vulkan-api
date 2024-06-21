import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderInputAttachmentArrayDynamicIndexing', ctypes.c_uint32),
        ('shaderUniformTexelBufferArrayDynamicIndexing', ctypes.c_uint32),
        ('shaderStorageTexelBufferArrayDynamicIndexing', ctypes.c_uint32),
        ('shaderUniformBufferArrayNonUniformIndexing', ctypes.c_uint32),
        ('shaderSampledImageArrayNonUniformIndexing', ctypes.c_uint32),
        ('shaderStorageBufferArrayNonUniformIndexing', ctypes.c_uint32),
        ('shaderStorageImageArrayNonUniformIndexing', ctypes.c_uint32),
        ('shaderInputAttachmentArrayNonUniformIndexing', ctypes.c_uint32),
        ('shaderUniformTexelBufferArrayNonUniformIndexing', ctypes.c_uint32),
        ('shaderStorageTexelBufferArrayNonUniformIndexing', ctypes.c_uint32),
        ('descriptorBindingUniformBufferUpdateAfterBind', ctypes.c_uint32),
        ('descriptorBindingSampledImageUpdateAfterBind', ctypes.c_uint32),
        ('descriptorBindingStorageImageUpdateAfterBind', ctypes.c_uint32),
        ('descriptorBindingStorageBufferUpdateAfterBind', ctypes.c_uint32),
        ('descriptorBindingUniformTexelBufferUpdateAfterBind', ctypes.c_uint32),
        ('descriptorBindingStorageTexelBufferUpdateAfterBind', ctypes.c_uint32),
        ('descriptorBindingUpdateUnusedWhilePending', ctypes.c_uint32),
        ('descriptorBindingPartiallyBound', ctypes.c_uint32),
        ('descriptorBindingVariableDescriptorCount', ctypes.c_uint32),
        ('runtimeDescriptorArray', ctypes.c_uint32),
    ]
