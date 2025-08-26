from typing import Any, Dict, List, Union


def get_questionnaire_name_from_id(
    questionnaire_id: str, questionnaire_list: List[Dict[str, Any]]
) -> Union[Any, None, str]:
    return next(
        (item for item in questionnaire_list if item.get("id") == questionnaire_id),
        {"name": ""},
    ).get("name")
