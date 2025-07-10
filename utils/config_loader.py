import yaml

class ConfigLoader(dict):
    def __init__(self, path="config/config.yaml"):
        try:
            with open(path, "r") as f:
                data = yaml.safe_load(f)
                if not isinstance(data, dict):
                    raise ValueError("YAML config must be a dictionary at the root level.")
        except FileNotFoundError:
            raise FileNotFoundError(f"Config file not found at: {path}")
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML format: {e}")
        
        super().__init__(data)
