import yaml


def yaml_coerce(value: str):
    """Convertvalue to python type

    Args:
        value (str): value to convert
    """
    if isinstance(value, str):
        return yaml.load(f"dummy: {value}", Loader=yaml.SafeLoader)["dummy"]

    return value
