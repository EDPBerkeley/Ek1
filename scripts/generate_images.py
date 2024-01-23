import os
import requests
from openai import OpenAI

client = OpenAI()

products = [
    "Golf Balls",
    "Protein Bars",
    "Trekking Poles",
    "Electrolyte Tablets",
    "Sweat-wicking T-shirts",
    "Resistance Bands",
    "Kayak Paddle",
    "Camping Chair",
    "Cycling Jerseys",
    "Inflatable Kayak",
    "Boogie Board",
    "Bike Pump",
    "Snow Sled",
    "Cycling Shorts",
    "Water Skiing Equipment",
    "Camping Tent",
    "Soccer Ball",
    "Snorkeling Gear",
    "Fishing Rod and Reel Combo",
    "Diamond Necklaces",
    "Clutch Purses",
    "Blanket Scarves",
    "Heart Necklaces",
    "Statement Rings",
    "Art Deco Jewelry",
    "Bamboo Sunglasses",
    "Pearl Jewelry",
    "Tassel Earrings",
    "Tribal Jewelry",
    "Smartwatches",
    "Hoop Earrings",
    "Wedding Rings",
    "Wedding Jewelry Sets",
    "Vintage Jewelry",
    "Resistance Bands",
    "Jump Rope",
    "CPR Face Shield",
    "Intimate Massagers",
    "Bathroom Scale",
    "TENS Unit",
    "EKG Monitor",
    "Tweezers",
    "Magnetic Therapy Products",
    "Pull-Up Bar",
    "Self-Help Books",
    "Smart Scale",
    "Weight Bench",
    "Sex Toys",
    "Pulse Oximeter",
    "Calcium Supplements",
    "Homeopathic Remedies",
    "Deodorant",
    "Personal Lubricants",
    "Safety Corner Protectors",
    "Soft Toys",
    "Maternity Dresses",
    "Maternity Pillow",
    "Baby Bottles",
    "Baby Monitors",
    "Breast Pumps",
    "Baby Mobiles",
    "Baby Hats",
    "Convertible Car Seats",
    "Bassinets",
    "Maternity Jeans",
    "Changing Pads",
    "Window Guards",
    "Maternity Leggings",
    "Maternity Tops",
    "Baby Proofing Kits",
    "Changing Tables",
    "Notebooks",
    "Academic Planner",
    "The Gruffalo by Julia Donaldson",
    "Bad Blood: Secrets and Lies in a Silicon Valley Startup by John Carreyrou",
    "Alice's Adventures in Wonderland by Lewis Carroll",
    "Where the Wild Things Are by Maurice Sendak",
    "Markers",
    "The Da Vinci Code by Dan Brown",
    "Happiness Planner",
    "Coloring Pencils",
    "Desk Organizer",
    "Desk Pad Calendar",
    "Desk Calendar",
    "Food Diary",
    "The Immortal Life of Henrietta Lacks by Rebecca Skloot",
    "Collectible Coins",
    "Poster Art",
    "Collectible Card Games",
    "Handmade Pottery",
    "Figurative Sculptures",
    "Rare Children's Books",
    "Vintage Accessories",
    "Music Posters",
    "Vintage Vinyl Records",
    "Antique Jewelry",
    "Rare Science Fiction Books",
    "Non-Sports Cards",
    "Metal Sculptures",
    "Vintage Postcards",
    "Antique Coins",
    "Antique Rugs",
    "Pokémon Cards",
    "Rare Stamps",
    "Daypacks",
    "Hardside Suitcases",
    "Noise-Canceling Headphones",
    "GPS Navigation Devices",
    "Hydration Packs",
    "Backpacks",
    "City Maps",
    "Travel Maps",
    "Rolling Backpacks",
    "Travel Backpacks",
    "Travel Locks",
    "Travel Wallets",
    "Travel Totes",
    "Drawstring Backpacks",
    "Portable Safes",
    "Travel Adapters",
    "Road Trip Guides",
    "Quick-Dry Underwear",
    "Hiking Boots",
    "Dapper Dan Hair Styling Cream",
    "Makeup Organizer",
    "L'Oréal Paris Foundation",
    "Baxter of California Pomade",
    "Crest 3D White Toothpaste",
    "Essential Oil Diffuser",
    "Olaplex Hair Perfector No. 3",
    "TRESemmé Shampoo and Conditioner",
    "Organic Lavender Oil",
    "Cremo Beard Oil",
    "Lavender Essential Oil",
    "Yves Saint Laurent Black Opium",
    "Makeup Brushes Set",
    "The Ordinary Niacinamide Serum",
    "Oral-B Electric Toothbrush",
    "Argan Oil Hair Serum",
    "Too Faced Blush",
    "Beard Trimmer",
    "Stud Earrings",
    "Blanket Scarves",
    "Sport Sunglasses",
    "Gold Necklaces",
    "Gothic Jewelry",
    "Tribal Jewelry",
    "Custom Jewelry",
    "Mirrored Sunglasses",
    "Wrap Bracelets",
    "Chronograph Watches",
    "Analog Watches",
    "Nameplate Necklaces",
    "Promise Rings",
    "Ear Jackets",
    "Statement Earrings",
    "Tennis Bracelets",
    "Birthstone Rings",
    "Pearl Necklaces",
    "Pet Bathing Tools",
    "Cat Beds",
    "Aquarium Air Pumps",
    "Joint Supplements for Pets",
    "Bird Cage Accessories",
    "Horse Stall Supplies",
    "Pet Towels and Dryers",
    "Dog Toys",
    "Bird Feeders",
    "Fish Tank Cleaning Supplies",
    "Pet Ear and Eye Cleaners",
    "Dog Beds",
    "Dog Bowls and Feeders",
    "Cat Bowls and Feeders",
    "Cat Health and Wellness Products",
    "Cat Toys",
    "Pet Pain Relief Medications",
    "Camping Cookware Set",
    "Volleyball",
    "Snowboard",
    "Bike Lights",
    "Cycling Jerseys",
    "Basketball",
    "Golf Clubs Set",
    "Hockey Stick",
    "Baseball Glove",
    "Performance Hoodies",
    "Snow Sled",
    "Fishing Rod and Reel Combo",
    "Golf Bag",
    "Dumbbell Set",
    "Cycling Gloves",
    "BCAA Supplements",
    "Baby Lotion",
    "Baby Body Wash",
    "Baby Proofing Kits",
    "Baby Wipes",
    "Baby Rompers",
    "Baby Oral Care",
    "Baby Powder",
    "Cradles",
    "Umbrella Strollers",
    "Crib Mobiles",
    "Cabinet Locks",
    "Baby Cribs",
    "Door Locks",
    "Baby Gates",
    "Convertible Car Seats",
    "Baby Washcloths",
    "Diaper Rash Creams",
    "Baby Spoons",
    "Nursing Covers",
    "Stone Sculptures",
    "Gold Coins",
    "Vintage Stamps",
    "Vintage Postcards",
    "Vintage Toys",
    "Antique Jewelry",
    "Collectible Books",
    "Antique Watches",
    "Modern Art Paintings",
    "First Edition Books",
    "Watercolor Paintings",
    "Antique Coins",
    "Canvas Prints",
    "Rare Children's Books",
    "Magic: The Gathering Cards",
    "Antique Lamps",
    "Handmade Jewelry",
    "Handmade Pottery",
    "Metal Sculptures",
    "Non-Sports Cards",
    "Silk Scarves",
    "Crossbody Bags",
    "Dress Watches",
    "Pearl Necklaces",
    "Link Bracelets",
    "Blanket Scarves",
    "Retro Jewelry",
    "Costume Jewelry",
    "Heart Necklaces",
    "Dangle Earrings",
    "Silver Jewelry",
    "Midi Rings",
    "Diamond Jewelry",
    "ID Bracelets",
    "Pearl Earrings",
    "Automatic Watches",
    "Stud Earrings",
    "Wayfarer Sunglasses",
    "Statement Jewelry",
    "Wireless Security Camera",
    "Duvet Cover Set",
    "Mop and Bucket",
    "Keurig Coffee Maker",
    "Bedspread",
    "Bed Skirt",
    "Dinnerware Set",
    "Artificial Plants",
    "Cordless Drill",
    "Storage Bins",
    "TV Stand",
    "Serving Platter",
    "KitchenAid Stand Mixer",
    "Wall Clock",
    "Trash Bags",
    "Mesh WiFi System",
    "Down Comforter",
    "Vitamix Blender",
    "Flatware Set",
    "Eggs",
    "Japanese Ramen Ingredients",
    "Pork Chops",
    "Organic Fruits",
    "Vegan Snacks",
    "Potato Chips",
    "Chinese Cuisine Ingredients",
    "Middle Eastern Cuisine Ingredients",
    "Salmon Fillet",
    "Sugar-Free Snacks",
    "Organic Vegetables",
    "Olive Oil",
    "Chocolate Bars",
    "Energy Drinks",
    "Granola Bars",
    "Organic Cereals",
    "Cookies",
    "Green Tea",
    "Bell Peppers",
    "External Hard Drives",
    "STEM Education Kits",
    "Desk Lamps",
    "Art Supplies for Schools",
    "Yearly Planners",
    "Desk Plants",
    "Journals",
    "Office Desks",
    "Mailroom Carts",
    "Binders",
    "Document Scanners",
    "Desk Organizers",
    "Mechanical Pencils",
    "Weekly Planners",
    "Mailing Labels",
    "Appointment Books",
    "Wide-Format Printers",
    "Envelopes",
    "Sony DualSense Controller",
    "iPhone 13",
    "Whoop Strap 4.0",
    "Arlo Pro 4 Security Camera",
    "Rode VideoMic Pro",
    "Nintendo Joy-Con",
    "Xbox Game Pass Subscription",
    "Philips Hue Smart Bulbs",
    "Oculus Quest 2",
    "Lenovo Tab M10",
    "SimpliSafe Home Security System",
    "Wyze Cam Outdoor",
    "Withings Body+ Smart Scale",
    "Microsoft Surface Pro",
    "Orbi Mesh WiFi System",
    "Nest Learning Thermostat",
    "Bose QuietComfort 35 II",
    "FiiO Hi-Res Player",
    "Xbox Game Pass Subscription",
    "Spigen Phone Case",
    "Nintendo Switch",
    "Gaming Headset",
    "Suunto 7 Smartwatch",
    "Screen Protector",
    "HP Envy x360",
    "OnePlus 9",
    "Withings Body+ Smart Scale",
    "TP-Link Archer C4000 Router",
    "Oculus Quest 2",
    "Wyze Cam Outdoor",
    "Canon EOS 5D Mark IV",
    "Apple AirPods Pro",
    "Universal Remote Control",
    "Asus ROG Gaming Laptop",
    "Bluetooth Selfie Stick",
    "Nintendo Joy-Con",
    "Horse Stall Supplies",
    "Small Animal Food",
    "Pet First Aid Kits",
    "Dog Health and Wellness Products",
    "Bird Feeders",
    "Cat Toys",
    "Pet Bathing Tools",
    "Pet Vitamins and Supplements",
    "Bird Food",
    "Fish Tank Cleaning Supplies",
    "Wet Dog Food",
    "Raw Pet Food",
    "Dog Beds",
    "Pet Ear and Eye Cleaners",
    "Pet Dental Care Products",
    "Pet Antibiotics",
    "Live Aquarium Plants",
    "Pet Grooming Gloves"
]


for i in range(5, len(products)):
    directory = f"/Users/erchispatwardhan/PycharmProjects/fastApiProject/assets/{products[i]}"
    os.makedirs(directory, exist_ok=True)

    for j in range(3):
        prompt = f"I need a prompt to ask Dalle for a simple and realistic non-artistic photo that anyone could have taken of {products[i]} that is meant to be listed on Amazon to sell on a catalogue, please just respond with the prompt only"

        text_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt},
            ]
        )

        text_prompt = text_response.choices[0].message.content

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



