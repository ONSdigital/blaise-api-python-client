from typing import Any, Dict, List, Union


def get_instrument_name_from_id(instrument_id: str, instrument_list: List[Dict[str, Any]]) -> Union[Any, None, str]:
    return next(
        (item for item in instrument_list if item.get("id") == instrument_id),
        {"name": ""},
    ).get("name")
