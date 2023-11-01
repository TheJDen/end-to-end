from pathlib import Path
import pandas as pd
import tarfile
import urllib.request

def load_housing_data(url = "https://github.com/ageron/data/raw/main/housing.tgz"):
    tarball_path = Path("datasets/housing.tg")
    if not tarball_path.is_file():
        Path("datasets").mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(url, tarball_path)
        with tarfile.open(tarball_path) as housing_tarball:
            housing_tarball.extractall(path="datasets")
    return pd.read_csv(Path("datasets/housing/housing.csv"))

def main():
    housing = load_housing_data()
    housing.head()


if __name__ == "__main__":
    main()