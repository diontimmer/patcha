class Patch:
    def __init__(self, original, modified):
        self.original = original
        self.modified = modified
        self.patched = False

    def apply_patch(self):
        if not self.patched:
            self._replace_function(self.original, self.modified)
            self.patched = True

    def revert_patch(self):
        if self.patched:
            self._replace_function(self.modified, self.original)
            self.patched = False

    def _replace_function(self, old, new):
        module_name = old.__module__
        func_name = old.__name__
        module = __import__(module_name)
        parts = module_name.split(".")
        for part in parts[1:]:
            module = getattr(module, part)
        setattr(module, func_name, new)
