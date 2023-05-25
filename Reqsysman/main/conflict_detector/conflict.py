
class Conflict:
    def __init__(self, source_requirement, target_requirement, relation):
        self.source_requirement = source_requirement
        self.target_requirement = target_requirement
        self.relation = relation


    def __str__(self):
        return f"Conflict: {self.source_requirement} {self.relation} {self.target_requirement} has version mismatch. "
