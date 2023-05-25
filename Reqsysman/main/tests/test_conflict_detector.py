import unittest
from unittest.mock import MagicMock

from Reqsysman.main.adapters.api_relationship_adapter import ApiRelationShipsAdapter
from Reqsysman.main.adapters.api_requirements_adapter import ApiRequirementsAdapter
from Reqsysman.main.conflict_detector.conflict_detector import ConflictDetector


class TestConflictDetector(unittest.TestCase):
    def setUp(self):
        self.api_requirements_adapter = ApiRequirementsAdapter()
        self.api_relationships_adapter = ApiRelationShipsAdapter()
        self.conflict_detector = ConflictDetector(self.api_relationships_adapter, self.api_requirements_adapter)

    def test_detect_conflicts(self):
        
        self.api_requirements_adapter.get_requirement_by_id = MagicMock(return_value={"id": "req1", "version": "1.0"})
        self.api_relationships_adapter.get_relationships = MagicMock(return_value=[{
            "source": {"id": "req1", "version": "1.0"},
            "target": {"id": "req2", "version": "1.0"},
        }])

        conflicts = self.conflict_detector.detect_conflicts(branch_name="main", commit_hash="123abc")

        self.assertEqual(len(conflicts), 0)

        self.api_requirements_adapter.get_requirement_by_id = MagicMock(return_value={"id": "req1", "version": "1.1"})
        
        conflicts = self.conflict_detector.detect_conflicts(branch_name="main", commit_hash="123abc")

        self.assertEqual(len(conflicts), 1)


if __name__ == "__main__":
    unittest.main()
