def deep_update(base_dict: dict, update_with: dict) -> dict:
    """
    Deep update of dictionary with another dictionary.
    """
    # iterate over keys in update_with
    for key, value in update_with.items():
        # if value is a dict, and base_dict has a value for that key that is also a dict
        if isinstance(value, dict):
            base_dict_value = base_dict.get(key)
            # if base_dict has a value for that key that is also a dict, recurse
            if isinstance(base_dict_value, dict):
                deep_update(base_dict_value, value)
            else:
                base_dict[key] = value
        else:
            base_dict[key] = value

    return base_dict
