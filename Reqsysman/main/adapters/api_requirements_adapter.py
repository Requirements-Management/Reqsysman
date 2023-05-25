from typing import List, Dict, Union

class ApiRequirementsAdapter:
    def __init__(self):
        pass

    def get_all_requirements(self, id: str = None, branch: str = None, commit_hash: str = None) -> List[Dict[str, Union[str, int]]]:
        # Здесь мы предполагаем, что API предоставляет endpoint для получения всех требований.
        # В реальной реализации здесь будет вызов к API с передачей commit_id и branch как параметров.

        # mock
        return [
            {
                "id": "REQ1",
                "description": "Some description1",
                "type_id": 10,
                "priority": "Medium",
                "status": "Approved",
            },
            {
                "id": "REQ2",
                "description": "Some description2",
                "type_id": 11,
                "priority": "Low",
                "status": "Not Approved",
            },
            {
                "id": "REQ3",
                "description": "Some description3",
                "type_id": 12,
                "priority": "High",
                "status": "Approved",
            },
        ]

    def get_requirement_by_id(self, id: str, branch: str = None, commit_hash: str = None) -> Dict[str, Union[str, int]]:
        # Здесь мы предполагаем, что API предоставляет endpoint для получения требования по ID.
        # В реальной реализации здесь будет вызов к API с передачей commit_id и branch как параметров.
        pass

    def update_requirement(self, id: str, data: Dict[str, Union[str, int]], branch: str = None, commit_hash: str = None) -> Dict[str, Union[str, int]]:
        # Здесь мы предполагаем, что API предоставляет endpoint для обновления требования.
        # В реальной реализации здесь будет вызов к API с передачей commit_id и branch как параметров.
        pass

    def create_requirement(self, id: str, data: Dict[str, Union[str, int]], branch: str = None, commit_hash: str = None) -> Dict[str, Union[str, int]]:
        # Здесь мы предполагаем, что API предоставляет endpoint для добавления требования.
        # В реальной реализации здесь будет вызов к API с передачей commit_id и branch как параметров.
        pass

    def delete_requirement(self, id: str, branch: str = None, commit_hash: str = None) -> Dict[str, str]:
        # Здесь мы предполагаем, что API предоставляет endpoint для удаления требования.
        # В реальной реализации здесь будет вызов к API с передачей commit_id и branch как параметров.
        pass
