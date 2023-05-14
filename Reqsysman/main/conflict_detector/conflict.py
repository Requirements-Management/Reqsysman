

class Conflict:
    def __init__(self, source_requirement, target_requirement, relation, source_version, target_version):
        self.source_requirement = source_requirement
        self.target_requirement = target_requirement
        self.relation = relation
        self.source_version = source_version
        self.target_version = target_version

    def __str__(self):
        return f"Conflict: {self.source_requirement} {self.relation} {self.target_requirement} has version mismatch. " \
               f"Source version: {self.source_version}, Target version: {self.target_version}"
