import os

from utils.db_utils import DBUtils



def find_empty_folders(directory="/Users/erchispatwardhan/PycharmProjects/fastApiProject/assets"):
    empty_folders = []

    for folder in os.listdir(directory):

        if os.path.isdir(folder) and os.listdir(directory) is None:
            empty_folders.append(directory)

    return empty_folders


def add_image(product_name, image):
    product = DBUtils.get_product_by_name(name=product_name)
    product.images.append(image)

    try:
        product.save()
    except Exception as e:
        print(product.id + " could not be updated")

def create_image(product_name):
    image_response = client.images.generate(
        model="dall-e-3",
        prompt=text_prompt,
        size="1024x1024",
        quality="standard",
        n=3,
    )

    image_url = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-MJZd9Yzelc7yFfJKqPJCgNH6/user-ponPP1ZAQMSuQSW3NyNyk1z2/img-SuAbdZwqP3iflxxvQTsp8zk0.png?st=2024-01-19T05%3A31%3A31Z&se=2024-01-19T07%3A31%3A31Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-01-18T12%3A21%3A30Z&ske=2024-01-19T12%3A21%3A30Z&sks=b&skv=2021-08-06&sig=NZPbIId6nWDoXyAFC3w75NCFi98oNQbpa4O0NuEgiRY%3D"

    # image_url = image_response.data[0].url
    print(image_url)

    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            # Save Image
            image_path = f"{directory}/{products[i]}{j}.jpg"
            with open(image_path, 'wb') as f:
                f.write(response.content)

    except requests.RequestException as e:
        print(f"Error downloading {image_url}: {e}")








DBUtils.initiate_connection()


