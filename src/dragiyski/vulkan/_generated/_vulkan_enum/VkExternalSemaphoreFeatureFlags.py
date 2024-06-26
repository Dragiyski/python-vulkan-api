from enum import IntFlag

class VkExternalSemaphoreFeatureFlags(IntFlag):
    VK_EXTERNAL_SEMAPHORE_FEATURE_EXPORTABLE_BIT = 1
    VK_EXTERNAL_SEMAPHORE_FEATURE_IMPORTABLE_BIT = 2
    VK_EXTERNAL_SEMAPHORE_FEATURE_EXPORTABLE_BIT_KHR = VK_EXTERNAL_SEMAPHORE_FEATURE_EXPORTABLE_BIT
    VK_EXTERNAL_SEMAPHORE_FEATURE_IMPORTABLE_BIT_KHR = VK_EXTERNAL_SEMAPHORE_FEATURE_IMPORTABLE_BIT
