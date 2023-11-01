from pathlib import Path
import pandas as pd
import tarfile
import urllib.request
import matplotlib.pyplot as plt
import numpy as np
from zlib import crc32

def load_housing_data(url = "https://github.com/ageron/data/raw/main/housing.tgz"):
    tarball_path = Path("datasets/housing.tg")
    if not tarball_path.is_file():
        Path("datasets").mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(url, tarball_path)
        with tarfile.open(tarball_path) as housing_tarball:
            housing_tarball.extractall(path="datasets")
    return pd.read_csv(Path("datasets/housing/housing.csv"))

def is_id_in_test_set(indentifier, test_ratio):
    return crc32(np.int64(indentifier)) < test_ratio * 2**32

def split_data_with_id_hash(data, test_ratio, id_column):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: is_id_in_test_set(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]


def main():
    housing = load_housing_data()

    housing_with_id = housing.reset_index()
    train_set, test_set = split_data_with_id_hash(housing_with_id, 0.2, "index")


if __name__ == "__main__":
    main()