from .. import binding

def init(
    self, *args,
    api_version: int,
    application_name: str | bytes | None = None,
    application_version: int = 0,
    engine_name: str | bytes | None = None,
    engine_version: int = 0,
    **kwargs
):
    if isinstance(application_name, str):
        application_name = application_name.encode()
    self.pApplicationName = application_name
    if isinstance(engine_name, str):
        engine_name = engine_name.encode()
    self.pEngineName = engine_name
    self.apiVersion = int(api_version)
    self.applicationVersion = int(application_version)
    self.engineVersion = int(engine_version)

binding.VkApplicationInfo._init_.append(init)
