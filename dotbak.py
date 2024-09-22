import os
import time
import shutil
import json
import sys

# Define color constants
class Colors:
    RESET = "\033[0m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"

def load_config(config_file):
    """Load configuration file"""
    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"{Colors.RED}Error loading the configuration file: {e}{Colors.RESET}")
        sys.exit(1)

def validate_paths(config):
    """Check if paths exist and output invalid paths after checking all"""
    invalid_paths = []  # List to store invalid paths
    for root_dir, sources in config.items():
        # Build the source paths list
        source_paths = [
            os.path.expanduser(os.path.join("~", source) if root_dir == "home" else os.path.join(f"/{root_dir}", source))
            for source in sources
        ]
        for path in source_paths:
            if not os.path.exists(path):
                invalid_paths.append(path)  # Collect invalid paths

    if invalid_paths:
        for path in invalid_paths:
            print(f"{Colors.RED}Error: Source path '{path}' does not exist.{Colors.RESET}")
        sys.exit(1)  # Exit program if there are any invalid paths
    else:
        print(f"{Colors.GREEN}All paths are valid.{Colors.RESET}")

def backup_dotfiles(config):
    """Backup the dotfiles in the configuration"""
    for root_dir, sources in config.items():
        peer_dir = os.path.join(os.getcwd(), root_dir)

        # If the target directory already exists, delete it
        if os.path.exists(peer_dir):
            shutil.rmtree(peer_dir)

        for source in sources:
            source_path = os.path.expanduser(
                os.path.join("~", source)
                if root_dir == "home"
                else os.path.join(f"/{root_dir}", source)
            )
            is_file = os.path.isfile(source_path)
            dest_path = os.path.join(peer_dir, source)

            try:
                if is_file:
                    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                    shutil.copy2(source_path, dest_path)
                else:
                    shutil.copytree(source_path, dest_path)

                print(f"{Colors.GREEN}Copied {'file' if is_file else 'directory'}: {Colors.YELLOW}{source_path}{Colors.GREEN} to {Colors.YELLOW}{dest_path}{Colors.RESET}")
            except (FileNotFoundError, PermissionError) as e:
                print(f"{Colors.RED}Error: {type(e).__name__} - {e}{Colors.RESET}")
            except Exception as e:
                print(f"{Colors.RED}Error: Encountered a problem - {e}{Colors.RESET}")

if __name__ == "__main__":
    config_file = "dotbak.json"

    try:
        config = load_config(config_file)   # Load configuration file
        validate_paths(config)              # Validate source paths

        start_time = time.time()            # Record start time
        backup_dotfiles(config)             # Backup operation
        end_time = time.time()              # Record end time

        print(f"\nBackup completed! Time taken: {end_time - start_time:.2f} seconds.")

    except FileNotFoundError:
        print(f"{Colors.RED}Error: Configuration file '{config_file}' not found.{Colors.RESET}")
    except json.JSONDecodeError:
        print(f"{Colors.RED}Error: Configuration file '{config_file}' is not valid JSON.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}Error: An unexpected error occurred - {e}{Colors.RESET}")
