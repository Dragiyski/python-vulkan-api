from ..xml.taxonomy import Taxonomy

class LazyApiBinding:
    def __init__(self, binding, taxonomy: Taxonomy):
        self._binding = binding
        self._taxonomy = taxonomy

