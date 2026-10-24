import json
from pathlib import Path
from types import SimpleNamespace

# Helper class that mimics the config module (supports .CONTENDERS and .RIVALS)
class BattleConfig(SimpleNamespace):
    CONTENDERS: list
    RIVALS: list

def save_battles(contenders, rivals, filepath="../data/battles.json"):
    """Save race contenders and rival pairs to a local JSON file."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    # Ensure rivals are lists of pairs for valid JSON serialization
    serialized_rivals = [list(pair) for pair in rivals]
    data = {
        "CONTENDERS": list(contenders),
        "RIVALS": serialized_rivals
    }
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Battles saved to {filepath}!")

def load_battles(filepath="../data/battles.json") -> BattleConfig:
    """
    Load race contenders and rival pairs from local JSON file.
    Returns an object with .CONTENDERS and .RIVALS attributes (matching DATA.CONTENDERS / DATA.RIVALS).
    """
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"Battle configuration not found at {filepath}. Run battle_finder first.")
    
    with open(path, "r") as f:
        data = json.load(f)
    
    # Convert rivals back to tuples
    rivals = [tuple(pair) for pair in data.get("RIVALS", [])]
    contenders = data.get("CONTENDERS", [])
    
    return BattleConfig(CONTENDERS=contenders, RIVALS=rivals)

# Function to write Contenders (backwards-compatible with legacy config.py)
def write_contenders(Contenders, rivals, local_path="../data/battles.json", write_legacy_config=True):
    """
    Save contenders & rivals locally to JSON (recommended) and optionally
    sync with configuration/config.py for backwards compatibility.
    """
    # 1. Save locally to race data/
    if local_path:
        try:
            save_battles(Contenders, rivals, filepath=local_path)
        except Exception as e:
            print(f"Warning: could not save local battles JSON: {e}")

    # 2. Sync to legacy configuration/config.py for backwards compatibility
    if write_legacy_config:
        config_path = Path(__file__).resolve().parent / "config.py"
        try:
            with open(config_path, "w") as conf:
                conf.write(f"CONTENDERS = {repr(Contenders)}\n")
                conf.write(f"RIVALS = {repr(rivals)}\n")
            print("Global legacy configuration synced!")
        except Exception as e:
            # Fallback to relative path if write failed
            try:
                with open("../../configuration/config.py", "w") as conf:
                    conf.write(f"CONTENDERS = {repr(Contenders)}\n")
                    conf.write(f"RIVALS = {repr(rivals)}\n")
                print("Global legacy configuration synced!")
            except Exception as e2:
                print(f"Could not update legacy config: {e2}") 