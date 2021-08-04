def get_instrument_name_from_id(instrument_id, instrument_list):
    return next(
        (item for item in instrument_list if item.get("id") == instrument_id),
        {"name": ""},
    ).get("name")