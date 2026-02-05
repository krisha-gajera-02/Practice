# Pathlib Library

from pathlib import Path


def pathlib_demo():
    BASE_DIR = Path(__file__).resolve().parent
    print("Script Location:", BASE_DIR)

    main_dir = BASE_DIR / "pathlib_demo"
    main_dir.mkdir(exist_ok=True)
    print("Main folder created:", main_dir)

    sub_dir = main_dir / "data"
    sub_dir.mkdir(exist_ok=True)
    print("Sub folder created:", sub_dir)

    file_path = sub_dir / "example.txt"
    file_path.write_text(
        "Hello!\n"
        "This file is created using pathlib.\n"
        "Inside pathlib_demo/data folder."
    )
    print("File created:", file_path)

    print("\nFile Content:")
    print(file_path.read_text())

    print("\nFile Name:", file_path.name)
    print("File Extension:", file_path.suffix)
    print("Parent Folder:", file_path.parent)
    print("Absolute Path:", file_path.resolve())

    print("\nExists:", file_path.exists())
    print("Is File:", file_path.is_file())
    print("Is Directory:", sub_dir.is_dir())

    print("\nFiles in data folder:")
    for item in sub_dir.iterdir():
        print(item.name)


if __name__ == "__main__":
    pathlib_demo()
