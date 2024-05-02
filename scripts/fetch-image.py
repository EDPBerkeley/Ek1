import os
from utils.db_utils import DBUtils as dbu
from utils.string_utils import StringUtils as su



def main():
    random_product = dbu.get_random_product()
    image_binary = random_product["images"][0]["element"].read()
    file_name = su.to_camel_case(random_product["name"])
    file_path = '/Users/erchispatwardhan/Downloads/' + file_name
    with open(file_path, 'wb') as file:
        file.write(image_binary)

    file_size = os.path.getsize(file_path)

    print(f"File Size: {file_size} bytes")


if __name__ == "__main__":
    dbu.initiate_connection()
    main()
