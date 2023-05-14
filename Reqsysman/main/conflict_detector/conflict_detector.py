
from typing import List
from Reqsysman.main.adapters.api_requirements_adapter import ApiRequirementsAdapter
from Reqsysman.main.conflict_detector.conflict import Conflict

from Reqsysman.main.adapters.api_relationship_adapter import ApiRelationShipsAdapter


class ConflictDetector:
    def __init__(self, api_relations_ships_adapter: ApiRelationShipsAdapter, api_rerquirements_adapter: ApiRequirementsAdapter):
        self.api_relations_ships_adapter = api_relations_ships_adapter
        self.api_rerquirements_adapter = api_rerquirements_adapter

    def detect_conflicts(self, branch_name: str, commit_hash: str) -> List[Conflict]:
        conflicts = []
        requirement_links = self.api_relations_ships_adapter.get_requirement_links(branch_name)
        
        for link in requirement_links:
            source_req = self.api_rerquirements_adapter.get_requirement_by_id(link['source']['id'],commit_hash, branch_name)
            target_req = self.api_rerquirements_adapter.get_requirement(link['target']['id'], commit_hash, branch_name)

            if source_req['version'] != link['source']['version'] or target_req['version'] != link['target']['version']:
                conflicts.append(Conflict(source_req, target_req, link))
                
        return conflicts
