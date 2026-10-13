from typing import Any


def get_questionnaire_name_from_id(
    questionnaire_id: str, questionnaire_list: list[dict[str, Any]]
) -> Any | str | None:
    return next(
        (item for item in questionnaire_list if item.get("id") == questionnaire_id),
        {"name": ""},
    ).get("name")
