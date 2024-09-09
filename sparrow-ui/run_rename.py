import os


def main():
    folder_path = "./docs/images"
    prefix = "receipt"

    files = os.listdir(folder_path)
    files.sort()

    for index, file_name in enumerate(files):

        if prefix in file_name:
            print(f"skipping ${file_name}")
            continue

        file_ext = os.path.splitext(file_name)[1]
        new_name = f"{prefix}_{index}{file_ext}"

        old_file = os.path.join(folder_path, file_name)
        new_file = os.path.join(folder_path, new_name)

        os.rename(old_file, new_file)

        print(f"renamed {old_file} to {new_file}")


if __name__ == "__main__":
    main()
