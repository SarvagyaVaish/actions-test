import yaml
from packaging.version import Version


METADATA_FILENAME = "release_metadata.yaml"

if __name__ == "__main__":
    data = {}

    with open(METADATA_FILENAME, "r") as f:
        data = yaml.load(f)

    v_curr = Version(data["sw_version"])
    v_next_str = str(v_curr.release[0]) + "." + str(v_curr.release[1] + 1)
    data["sw_version"] = v_next_str

    print("Setting sw version to {}".format(v_next_str))

    with open(METADATA_FILENAME, "w") as f:
        yaml.dump(data, f)
