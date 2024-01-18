import json
data = [
    {
        "category": "Sports & Outdoors",
        "name": "Sporty Outdoor Essentials",
        "date_created": "2021-07-09",
        "description": "Sporty Outdoor Essentials offers a wide range of products related to its category.",
        "opening_time": "8:00 AM",
        "closing_time": "5:00 PM",
        "website": "www.sportyoutdooressentials.com",
        "phone_number": "210-483-8423",
        "rating": 2.1,
        "distance": 0.2,
        "cost": 1,
        "payment_methods": 6,
        "products": [
            {
                "category": "Golf",
                "product": "Golf Balls",
                "description": "Designed for distance and durability, these golf balls offer a consistent flight path and exceptional playability. Ideal for golfers of all skill levels seeking to improve their game.",
                "price": 21.05,
                "sku": "S0U5PYD0",
                "quantity": 95,
                "date_created": "2023-09-16"
            },
            {
                "category": "Sports Nutrition",
                "product": "Protein Bars",
                "description": "Packed with essential nutrients and protein, these bars are perfect for a quick energy boost or post-workout recovery. Made with natural ingredients, they're both delicious and nutritious.",
                "price": 411.17,
                "sku": "OZIWCRHM",
                "quantity": 29,
                "date_created": "2023-06-10"
            },
            {
                "category": "Camping & Hiking",
                "product": "Trekking Poles",
                "description": "These lightweight yet sturdy trekking poles provide reliable support on all terrains. Equipped with comfortable grips and adjustable lengths, they're ideal for hikers and trekkers.",
                "price": 388.43,
                "sku": "WUEVOT0T",
                "quantity": 52,
                "date_created": "2023-08-27"
            },
            {
                "category": "Sports Nutrition",
                "product": "Electrolyte Tablets",
                "description": "Stay hydrated and replenished during intense activities with these fast-dissolving electrolyte tablets. They help maintain fluid balance and prevent cramping, keeping you energized.",
                "price": 191.05,
                "sku": "KOKSF36A",
                "quantity": 26,
                "date_created": "2023-07-08"
            },
            {
                "category": "Sports Apparel",
                "product": "Sweat-wicking T-shirts",
                "description": "Experience ultimate comfort with these high-performance T-shirts. The sweat-wicking fabric keeps you dry, while the ergonomic design ensures a perfect fit during any activity.",
                "price": 139.86,
                "sku": "2I4HGSTB",
                "quantity": 91,
                "date_created": "2023-08-26"
            },
            {
                "category": "Fitness & Exercise Equipment",
                "product": "Resistance Bands",
                "description": "Enhance your workouts with these versatile resistance bands. Ideal for strength training, flexibility, and rehabilitation exercises, they come in various resistance levels to suit your needs.",
                "price": 38.67,
                "sku": "RGID1L0G",
                "quantity": 76,
                "date_created": "2023-02-13"
            },
            {
                "category": "Water Sports",
                "product": "Kayak Paddle",
                "description": "Engineered for efficiency and control, this kayak paddle is designed for paddlers seeking a lightweight yet robust solution for their kayaking adventures. Its ergonomic design ensures a comfortable grip and smooth paddling experience.",
                "price": 89.45,
                "sku": "L5QTCI0R",
                "quantity": 13,
                "date_created": "2023-10-02"
            },
            {
                "category": "Camping & Hiking",
                "product": "Camping Chair",
                "description": "This compact and lightweight camping chair is your perfect companion for outdoor",
                "price": 277.52,
                "sku": "2TDQQSL6",
                "quantity": 31,
                "date_created": "2023-02-11"
            },
            {
                "category": "Sports Apparel",
                "product": "Cycling Jerseys",
                "description": "Crafted for cyclists, these jerseys offer a blend of comfort, breathability, and aerodynamic design. Ideal for both competitive racing and leisure biking.",
                "price": 308.26,
                "sku": "94JZR6L8",
                "quantity": 1,
                "date_created": "2023-12-10"
            },
            {
                "category": "Outdoor Recreation",
                "product": "Inflatable Kayak",
                "description": "This inflatable kayak is designed for both beginners and experienced paddlers. It's lightweight, durable, and easy to transport, making it perfect for exploring lakes and rivers.",
                "price": 271.8,
                "sku": "55VO5Z6Z",
                "quantity": 35,
                "date_created": "2023-07-04"
            },
            {
                "category": "Water Sports",
                "product": "Boogie Board",
                "description": "This boogie board is perfect for ocean enthusiasts. It offers a great balance of buoyancy and stability, making it ideal for all skill levels.",
                "price": 25.95,
                "sku": "FORJ4CY9",
                "quantity": 54,
                "date_created": "2023-08-09"
            },
            {
                "category": "Cycling",
                "product": "Bike Pump",
                "description": "A compact and efficient bike pump, essential for keeping your tires inflated on the go. Its portable design makes it a must-have for cyclists.",
                "price": 272.64,
                "sku": "VW07OQ55",
                "quantity": 34,
                "date_created": "2023-08-01"
            },
            {
                "category": "Winter Sports",
                "product": "Snow Sled",
                "description": "This snow sled is designed for fun and durability. It's perfect for a snowy day, offering a smooth and exciting sledding experience.",
                "price": 249.61,
                "sku": "6P5O958P",
                "quantity": 17,
                "date_created": "2023-03-31"
            },
            {
                "category": "Cycling",
                "product": "Cycling Shorts",
                "description": "These cycling shorts provide comfort and support for long rides. With a padded seat and moisture-wicking fabric, they're designed for both casual and serious cyclists.",
                "price": 38.55,
                "sku": "7TK99QBK",
                "quantity": 64,
                "date_created": "2024-01-10"
            },
            {
                "category": "Water Sports",
                "product": "Water Skiing Equipment",
                "description": "High-quality water skiing equipment that offers both safety and performance. It's designed for water sports enthusiasts of all skill levels.",
                "price": 266.25,
                "sku": "RPHHIWNB",
                "quantity": 22,
                "date_created": "2023-07-28"
            },
            {
                "category": "Outdoor Recreation",
                "product": "Camping Tent",
                "description": "This spacious and easy-to-set-up camping tent is perfect for family outings or solo adventures. It's durable and weather-resistant, providing a comfortable shelter in the outdoors.",
                "price": 256.65,
                "sku": "N0VDVQI6",
                "quantity": 57,
                "date_created": "2023-04-25"
            },
            {
                "category": "Team Sports",
                "product": "Soccer Ball",
                "description": "A durable soccer ball that offers great touch and feel. Suitable for all playing surfaces, it's designed for players who value precision and control.",
                "price": 66.34,
                "sku": "LMH2PD6L",
                "quantity": 79,
                "date_created": "2023-03-05"
            },
            {
                "category": "Water Sports",
                "product": "Snorkeling Gear",
                "description": "This snorkeling gear set includes a comfortable mask, snorkel, and fins. It's perfect for exploring underwater worlds, offering clear vision and easy breathing.",
                "price": 425.78,
                "sku": "7RB7J9N6",
                "quantity": 28,
                "date_created": "2023-10-06"
            },
            {
                "category": "Outdoor Recreation",
                "product": "Fishing Rod and Reel Combo",
                "description": "A versatile fishing rod and reel combo suitable for both beginners and experienced anglers. It's lightweight, durable, and perfect for catching a variety of fish.",
                "price": 90.63,
                "sku": "AHL2BYXB",
                "quantity": 5,
                "date_created": "2023-07-28"
            }
        ]
    },
    {
        "category": "Jewelry & Accessories",
        "name": "Glamour Jewelry Haven",
        "date_created": "2020-02-25",
        "description": "Glamour Jewelry Haven offers a wide range of products related to its category.",
        "opening_time": "8:00 AM",
        "closing_time": "6:00 PM",
        "website": "www.glamourjewelryhaven.com",
        "phone_number": "195-533-8931",
        "rating": 3.1,
        "distance": 3.4,
        "cost": 3,
        "payment_methods": 5,
        "products": [
            {
                "category": "Necklaces & Pendants",
                "product": "Diamond Necklaces",
                "description": "These stunning diamond necklaces exude luxury and elegance. Perfect for special occasions, they add a touch of sophistication to any outfit.",
                "price": 368.14,
                "sku": "H3K8FNRF",
                "quantity": 55,
                "date_created": "2023-02-28"
            },
            {
                "category": "Handbags & Wallets",
                "product": "Clutch Purses",
                "description": "Chic and functional, these clutch purses are ideal for evenings out. They combine style with practicality, available in various designs to suit any taste.",
                "price": 485.45,
                "sku": "CEF3NHOF",
                "quantity": 39,
                "date_created": "2023-02-09"
            },
            {
                "category": "Scarves & Wraps",
                "product": "Blanket Scarves",
                "description": "Cozy and fashionable, these blanket scarves are perfect for chilly days. Their versatile design allows them to be styled in multiple ways.",
                "price": 356.45,
                "sku": "1FQXZYDT",
                "quantity": 55,
                "date_created": "2023-04-29"
            },
            {
                "category": "Necklaces & Pendants",
                "product": "Heart Necklaces",
                "description": "Romantic and delicate, these heart necklaces make a perfect gift for a loved one or a special treat for yourself.",
                "price": 498.32,
                "sku": "S8EPICWD",
                "quantity": 66,
                "date_created": "2023-11-01"
            },
            {
                "category": "Rings",
                "product": "Statement Rings",
                "description": "Make a bold statement with these eye-catching rings. They are designed to stand out and add a unique flair to your jewelry collection.",
                "price": 430.38,
                "sku": "0HQOHJFX",
                "quantity": 29,
                "date_created": "2023-07-11"
            },
            {
                "category": "Fashion Jewelry",
                "product": "Art Deco Jewelry",
                "description": "Inspired by the Art Deco era, these pieces feature bold geometric designs and vibrant colors.",
                "price": 290.86,
                "sku": "T8D5W74D",
                "quantity": 1,
                "date_created": "2023-08-01"
            },
            {
                "category": "Sunglasses",
                "product": "Bamboo Sunglasses",
                "description": "Eco-friendly and stylish, these bamboo sunglasses are perfect for the environmentally conscious fashionista. Lightweight and durable, they offer both comfort and style.",
                "price": 148.03,
                "sku": "KDSZ7O1R",
                "quantity": 18,
                "date_created": "2023-04-26"
            },
            {
                "category": "Fine Jewelry",
                "product": "Pearl Jewelry",
                "description": "Timeless jewelry pieces adorned with pearls, symbolizing sophistication and grace.",
                "price": 490.62,
                "sku": "YC0CYZ9S",
                "quantity": 24,
                "date_created": "2023-11-10"
            },
            {
                "category": "Earrings",
                "product": "Tassel Earrings",
                "description": "These tassel earrings are a trendy addition to any outfit. Lightweight and playful, they're perfect for both casual and formal occasions.",
                "price": 397.12,
                "sku": "YFFQCQJY",
                "quantity": 10,
                "date_created": "2023-03-11"
            },
            {
                "category": "Fashion Jewelry",
                "product": "Tribal Jewelry",
                "description": "Intricately designed tribal jewelry that celebrates cultural artistry. Each piece is a work of art, perfect for those who appreciate unique, handcrafted items.",
                "price": 359.26,
                "sku": "8F3NKH0B",
                "quantity": 80,
                "date_created": "2023-05-23"
            },
            {
                "category": "Watches",
                "product": "Smartwatches",
                "description": "Stay connected and track your fitness with these cutting-edge smartwatches. They offer various features to suit your lifestyle needs.",
                "price": 72.45,
                "sku": "JLGGDW9J",
                "quantity": 4,
                "date_created": "2023-04-06"
            },
            {
                "category": "Earrings",
                "product": "Hoop Earrings",
                "description": "Classic and versatile, these hoop earrings are a staple in any jewelry collection. Perfect for both everyday wear and special occasions.",
                "price": 146.75,
                "sku": "WNY4UROK",
                "quantity": 6,
                "date_created": "2023-04-15"
            },
            {
                "category": "Rings",
                "product": "Wedding Rings",
                "description": "Find your dream wedding ring from our exquisite collection. Each piece symbolizes love and commitment, crafted with precision and care.",
                "price": 179.63,
                "sku": "THNNJTMF",
                "quantity": 52,
                "date_created": "2023-11-08"
            },
            {
                "category": "Fine Jewelry",
                "product": "Wedding Jewelry Sets",
                "description": "Complete your bridal look with these elegant wedding jewelry sets. They add a touch of glamour and sophistication to your special day.",
                "price": 87.05,
                "sku": "8IB6MKH2",
                "quantity": 36,
                "date_created": "2023-07-16"
            },
            {
                "category": "Fashion Jewelry",
                "product": "Vintage Jewelry",
                "description": "Discover the timeless beauty of our vintage jewelry collection. Each piece tells a story and adds a unique charm to your ensemble.",
                "price": 402.38,
                "sku": "G6925XX3",
                "quantity": 30,
                "date_created": "2023-06-14"
            }
        ]
    },
    {
        "category": "Health & Wellness",
        "name": "Wellness & Health Hub",
        "date_created": "2023-08-06",
        "description": "Wellness & Health Hub offers a wide range of products related to its category.",
        "opening_time": "8:00 AM",
        "closing_time": "8:00 PM",
        "website": "www.wellness&healthhub.com",
        "phone_number": "767-666-7145",
        "rating": 3.5,
        "distance": 2.0,
        "cost": 1,
        "payment_methods": 4,
        "products": [
            {
                "category": "Fitness & Yoga Equipment",
                "product": "Resistance Bands",
                "description": "Enhance your workout with these versatile resistance bands, ideal for strength training and improving flexibility.",
                "price": 372.45,
                "sku": "SW9ADX3A",
                "quantity": 91,
                "date_created": "2023-03-05"
            },
            {
                "category": "Fitness & Yoga Equipment",
                "product": "Jump Rope",
                "description": "This high-quality jump rope is perfect for cardio workouts, helping to improve endurance and coordination.",
                "price": 209.73,
                "sku": "CJD0Q7G4",
                "quantity": 87,
                "date_created": "2023-10-22"
            },
            {
                "category": "First Aid & Medical Supplies",
                "product": "CPR Face Shield",
                "description": "A must-have for emergency preparedness, this CPR face shield is designed for safety and effectiveness in critical situations.",
                "price": 382.69,
                "sku": "I7UUUYEY",
                "quantity": 83,
                "date_created": "2023-10-13"
            },
            {
                "category": "Sexual Wellness",
                "product": "Intimate Massagers",
                "description": "Explore a range of intimate massagers designed for personal comfort and relaxation, crafted with discretion and quality in mind.",
                "price": 440.07,
                "sku": "SRHWIYYG",
                "quantity": 10,
                "date_created": "2023-12-25"
            },
            {
                "category": "Weight Management",
                "product": "Bathroom Scale",
                "description": "Keep track of your fitness goals with this accurate and easy-to-use bathroom scale, a perfect tool for any health regimen.",
                "price": 431.65,
                "sku": "JT710U1Y",
                "quantity": 91,
                "date_created": "2023-09-25"
            },
            {
                "category": "Health Monitors & Devices",
                "product": "TENS Unit",
                "description": "Experience relief from pain with this TENS unit, offering various settings to suit your therapeutic needs.",
                "price": 46.3,
                "sku": "P5DH01YT",
                "quantity": 48,
                "date_created": "2023-09-09"
            },
            {
                "category": "Health Monitors & Devices",
                "product": "EKG Monitor",
                "description": "Monitor your heart health conveniently at home with this easy-to-use and accurate EKG monitor.",
                "price": 37.82,
                "sku": "0H25SNTO",
                "quantity": 96,
                "date_created": "2023-07-16"
            },
            {
                "category": "First Aid & Medical Supplies",
                "product": "Tweezers",
                "description": "Precision-engineered tweezers ideal for various uses, from beauty routines to medical applications.",
                "price": 308.55,
                "sku": "0XD2ITYJ",
                "quantity": 97,
                "date_created": "2023-12-29"
            },
            {
                "category": "Herbal & Alternative Remedies",
                "product": "Magnetic Therapy Products",
                "description": "Discover the benefits of magnetic therapy with these products designed to enhance well-being and relieve discomfort.",
                "price": 213.29,
                "sku": "7DY6BQRU",
                "quantity": 87,
                "date_created": "2024-01-10"
            },
            {
                "category": "Fitness & Yoga Equipment",
                "product": "Pull-Up Bar",
                "description": "Strengthen your upper body with this sturdy and easy-to-install pull-up bar, perfect for home workouts.",
                "price": 486.56,
                "sku": "9VT0H0BL",
                "quantity": 11,
                "date_created": "2023-10-22"
            },
            {
                "category": "Mental Wellness",
                "product": "Self-Help Books",
                "description": "Find inspiration and guidance with our selection of self-help books, covering a range of topics from personal development to mental wellness.",
                "price": 300.82,
                "sku": "WE9QJ6CR",
                "quantity": 68,
                "date_created": "2023-12-07"
            },
            {
                "category": "Health Monitors & Devices",
                "product": "Smart Scale",
                "description": "Track your health metrics effectively with this smart scale, featuring advanced technology for accurate measurements.",
                "price": 264.15,
                "sku": "AY6K4VVI",
                "quantity": 69,
                "date_created": "2023-10-29"
            },
            {
                "category": "Fitness & Yoga Equipment",
                "product": "Weight Bench",
                "description": "Enhance your home gym with this durable weight bench, ideal for various strength training exercises.",
                "price": 373.37,
                "sku": "NTOF4K4N",
                "quantity": 99,
                "date_created": "2023-01-29"
            },
            {
                "category": "Sexual Wellness",
                "product": "Sex Toys",
                "description": "Explore a variety of sex toys designed for pleasure and intimacy, with options to suit all preferences and comfort levels.",
                "price": 385.65,
                "sku": "BJ7VR6PV",
                "quantity": 42,
                "date_created": "2023-07-04"
            },
            {
                "category": "Health Monitors & Devices",
                "product": "Pulse Oximeter",
                "description": "Monitor your oxygen levels and pulse rate with ease using this compact and reliable pulse oximeter.",
                "price": 254.78,
                "sku": "W73ETUMD",
                "quantity": 97,
                "date_created": "2023-06-27"
            },
            {
                "category": "Supplements & Vitamins",
                "product": "Calcium Supplements",
                "description": "Support your bone health with these high-quality calcium supplements, essential for a balanced diet.",
                "price": 24.87,
                "sku": "QPZGK7AQ",
                "quantity": 11,
                "date_created": "2023-03-27"
            },
            {
                "category": "Herbal & Alternative Remedies",
                "product": "Homeopathic Remedies",
                "description": "Discover natural relief with our range of homeopathic remedies, catering to a variety of health concerns.",
                "price": 360.0,
                "sku": "G297I09J",
                "quantity": 97,
                "date_created": "2023-09-17"
            },
            {
                "category": "Personal Care",
                "product": "Deodorant",
                "description": "Stay fresh and confident with our selection of deodorants, offering long-lasting protection and pleasant fragrances.",
                "price": 134.56,
                "sku": "XCJOYHSE",
                "quantity": 85,
                "date_created": "2023-04-10"
            },
            {
                "category": "Sexual Wellness",
                "product": "Personal Lubricants",
                "description": "Enhance comfort and pleasure with our personal lubricants, formulated for safety and sensitivity.",
                "price": 41.99,
                "sku": "GGO8UNY6",
                "quantity": 1,
                "date_created": "2023-10-17"
            }
        ]
    },
    {
        "category": "Baby Products",
        "name": "Tiny Tots Baby Store",
        "date_created": "2021-11-29",
        "description": "Tiny Tots Baby Store offers a wide range of products related to its category.",
        "opening_time": "10:00 AM",
        "closing_time": "5:00 PM",
        "website": "www.tinytotsbabystore.com",
        "phone_number": "499-479-5602",
        "rating": 3.2,
        "distance": 1.6,
        "cost": 4,
        "payment_methods": 7,
        "products": [
            {
                "category": "Baby Safety",
                "product": "Safety Corner Protectors",
                "description": "These safety corner protectors are designed to keep babies safe from sharp edges, blending seamlessly with your home decor.",
                "price": 219.42,
                "sku": "CLNXB1TF",
                "quantity": 13,
                "date_created": "2023-03-07"
            },
            {
                "category": "Baby Toys",
                "product": "Soft Toys",
                "description": "Our collection of soft toys is perfect for babies, made with safe, cuddly materials ideal for playtime and comfort.",
                "price": 486.21,
                "sku": "ZULSKPNV",
                "quantity": 64,
                "date_created": "2023-01-15"
            },
            {
                "category": "Maternity Care",
                "product": "Maternity Dresses",
                "description": "Stay stylish and comfortable during pregnancy with our maternity dresses, designed to provide a perfect fit throughout your journey.",
                "price": 410.23,
                "sku": "O98EYN8J",
                "quantity": 43,
                "date_created": "2023-10-26"
            },
            {
                "category": "Maternity Care",
                "product": "Maternity Pillow",
                "description": "This maternity pillow offers support and comfort for expecting mothers, aiding in better sleep and relaxation.",
                "price": 485.96,
                "sku": "UKTTS70B",
                "quantity": 75,
                "date_created": "2024-01-13"
            },
            {
                "category": "Feeding & Nursing",
                "product": "Baby Bottles",
                "description": "Our baby bottles are designed for easy feeding, with safe materials and ergonomic designs for both parents and babies.",
                "price": 324.69,
                "sku": "PCK0TUN3",
                "quantity": 95,
                "date_created": "2023-06-27"
            },
            {
                "category": "Baby Safety",
                "product": "Baby Monitors",
                "description": "Keep a close eye on your baby with our high-tech baby monitors, offering clear audio and video capabilities.",
                "price": 248.86,
                "sku": "MD1ZM9JT",
                "quantity": 82,
                "date_created": "2023-11-28"
            },
            {
                "category": "Feeding & Nursing",
                "product": "Breast Pumps",
                "description": "Our breast pumps are efficient and comfortable, making the breastfeeding journey easier for new mothers.",
                "price": 209.83,
                "sku": "DG6CBJBU",
                "quantity": 17,
                "date_created": "2023-06-19"
            },
            {
                "category": "Baby Toys",
                "product": "Baby Mobiles",
                "description": "Entertain and soothe your baby with our delightful range of baby mobiles, featuring colorful designs and gentle movements.",
                "price": 85.04,
                "sku": "MTZADT17",
                "quantity": 56,
                "date_created": "2023-12-28"
            },
            {
                "category": "Baby Clothing & Accessories",
                "product": "Baby Hats",
                "description": "Protect your baby in style with our range of baby hats, perfect for every season and occasion.",
                "price": 144.26,
                "sku": "09TP00IN",
                "quantity": 23,
                "date_created": "2023-09-05"
            },
            {
                "category": "Strollers & Car Seats",
                "product": "Convertible Car Seats",
                "description": "Ensure your baby's safety during travel with our convertible car seats, designed for comfort and protection.",
                "price": 211.1,
                "sku": "YNOB6L3E",
                "quantity": 72,
                "date_created": "2023-04-15"
            },
            {
                "category": "Nursery Furniture",
                "product": "Bassinets",
                "description": "Our bassinets provide a cozy and safe sleeping environment for your newborn, blending comfort with modern design.",
                "price": 308.04,
                "sku": "BHQ0IWMS",
                "quantity": 63,
                "date_created": "2023-09-04"
            },
            {
                "category": "Maternity Care",
                "product": "Maternity Jeans",
                "description": "Stay fashionable during pregnancy with our maternity jeans, offering both comfort and style.",
                "price": 217.54,
                "sku": "117PATVH",
                "quantity": 57,
                "date_created": "2024-01-03"
            },
            {
                "category": "Diapers & Wipes",
                "product": "Changing Pads",
                "description": "Make diaper changes easy and hygienic with our durable and comfortable changing pads.",
                "price": 65.29,
                "sku": "5TNAT6Z9",
                "quantity": 92,
                "date_created": "2023-10-25"
            },
            {
                "category": "Baby Safety",
                "product": "Window Guards",
                "description": "Keep your baby safe at home with our reliable window guards, designed for easy installation and robust protection.",
                "price": 15.98,
                "sku": "R7DL108H",
                "quantity": 8,
                "date_created": "2023-03-11"
            },
            {
                "category": "Maternity Care",
                "product": "Maternity Leggings",
                "description": "Enjoy comfort and flexibility with our maternity leggings, ideal for everyday wear during pregnancy.",
                "price": 424.15,
                "sku": "2WIQXEQ3",
                "quantity": 91,
                "date_created": "2023-05-29"
            },
            {
                "category": "Maternity Care",
                "product": "Maternity Tops",
                "description": "Our maternity tops are stylish and versatile, perfect for casual outings or relaxing at home.",
                "price": 85.57,
                "sku": "YOQBBW63",
                "quantity": 20,
                "date_created": "2023-11-18"
            },
            {
                "category": "Baby Safety",
                "product": "Baby Proofing Kits",
                "description": "Ensure your home is safe for your little one with our comprehensive baby proofing kits.",
                "price": 307.39,
                "sku": "BR7R4NSY",
                "quantity": 49,
                "date_created": "2023-08-27"
            },
            {
                "category": "Nursery Furniture",
                "product": "Changing Tables",
                "description": "Our changing tables offer convenience and storage, making diaper changes a breeze.",
                "price": 352.68,
                "sku": "NNQ22SCT",
                "quantity": 26,
                "date_created": "2023-07-03"
            }
        ]
    },
    {
        "category": "Books & Stationery",
        "name": "Readers' Retreat Bookstore",
        "date_created": "2020-11-24",
        "description": "Readers' Retreat Bookstore offers a wide range of products related to its category.",
        "opening_time": "10:00 AM",
        "closing_time": "7:00 PM",
        "website": "www.readers'retreatbookstore.com",
        "phone_number": "407-279-6255",
        "rating": 4.6,
        "distance": 2.8,
        "cost": 3,
        "payment_methods": 4,
        "products": [
            {
                "category": "Office Supplies",
                "product": "Notebooks",
                "description": "Perfect for jotting down thoughts or keeping organized, our notebooks come in various designs and sizes.",
                "price": 319.86,
                "sku": "ONHPRDFS",
                "quantity": 88,
                "date_created": "2023-12-18"
            },
            {
                "category": "Calendars & Planners",
                "product": "Academic Planner",
                "description": "Stay on top of your schedule with our academic planners, designed to help students and professionals manage their time efficiently.",
                "price": 220.12,
                "sku": "14H3S317",
                "quantity": 47,
                "date_created": "2023-06-07"
            },
            {
                "category": "Children's Books",
                "product": "The Gruffalo by Julia Donaldson",
                "description": "A beloved children's book that captivates young minds with its charming story and illustrations.",
                "price": 486.98,
                "sku": "C7JULO8A",
                "quantity": 63,
                "date_created": "2023-06-18"
            },
            {
                "category": "Non-Fiction",
                "product": "Bad Blood: Secrets and Lies in a Silicon Valley Startup by John Carreyrou",
                "description": "Uncover the gripping truth behind a Silicon Valley scandal with 'Bad Blood,' a captivating read about ambition, deception, and the collapse of Theranos.",
                "price": 359.89,
                "sku": "4O69JMS2",
                "quantity": 3,
                "date_created": "2023-12-13"
            },
            {
                "category": "Children's Books",
                "product": "Alice's Adventures in Wonderland by Lewis Carroll",
                "description": "A timeless classic that continues to enchant readers of all ages with its whimsical narrative.",
                "price": 270.97,
                "sku": "CBAP1724",
                "quantity": 73,
                "date_created": "2023-04-01"
            },
            {
                "category": "Children's Books",
                "product": "Where the Wild Things Are by Maurice Sendak",
                "description": "A must-have children's book that explores imagination and emotions through a captivating story.",
                "price": 402.75,
                "sku": "AKKZ3IBE",
                "quantity": 21,
                "date_created": "2023-03-19"
            },
            {
                "category": "Writing Instruments",
                "product": "Markers",
                "description": "Our markers come in a spectrum of colors, perfect for all your creative and organizational needs.",
                "price": 360.28,
                "sku": "J277ZHPA",
                "quantity": 60,
                "date_created": "2023-10-02"
            },
            {
                "category": "Fiction",
                "product": "The Da Vinci Code by Dan Brown",
                "description": "A bestselling mystery-thriller novel that explores historical and religious themes.",
                "price": 330.95,
                "sku": "QJOR9A5X",
                "quantity": 81,
                "date_created": "2023-11-25"
            },
            {
                "category": "Journals & Diaries",
                "product": "Happiness Planner",
                "description": "Focus on personal growth and happiness with this planner, designed to inspire and motivate.",
                "price": 433.88,
                "sku": "9I88SVOH",
                "quantity": 59,
                "date_created": "2023-11-06"
            },
            {
                "category": "Writing Instruments",
                "product": "Coloring Pencils",
                "description": "Ideal for artists and hobbyists, our coloring pencils offer a range of vibrant colors for your artwork.",
                "price": 33.87,
                "sku": "Y6UAWW7N",
                "quantity": 59,
                "date_created": "2023-11-21"
            },
            {
                "category": "Office Supplies",
                "product": "Desk Organizer",
                "description": "Keep your workspace tidy and efficient with our stylish and functional desk organizers.",
                "price": 88.48,
                "sku": "71FH2F3X",
                "quantity": 93,
                "date_created": "2023-05-22"
            },
            {
                "category": "Calendars & Planners",
                "product": "Desk Pad Calendar",
                "description": "Plan your days with ease using our desk pad calendars, featuring ample space for notes and appointments.",
                "price": 17.35,
                "sku": "9TRORZRG",
                "quantity": 70,
                "date_created": "2023-09-10"
            },
            {
                "category": "Office Supplies",
                "product": "Desk Calendar",
                "description": "A practical and stylish calendar that sits on a desk, helping to organize dates and appointments.",
                "price": 423.53,
                "sku": "ZZERASMW",
                "quantity": 50,
                "date_created": "2023-01-18"
            },
            {
                "category": "Journals & Diaries",
                "product": "Food Diary",
                "description": "A journal for tracking food intake and eating habits, useful for diet planning and monitoring.",
                "price": 284.03,
                "sku": "B7HADM22",
                "quantity": 87,
                "date_created": "2024-01-13"
            },
            {
                "category": "Non-Fiction",
                "product": "The Immortal Life of Henrietta Lacks by Rebecca Skloot",
                "description": "A non-fiction book telling the story of Henrietta Lacks and her immortal cell line.",
                "price": 293.56,
                "sku": "DU51ONXO",
                "quantity": 75,
                "date_created": "2023-07-28"
            }
        ]
    },
    {
        "category": "Art & Collectibles",
        "name": "Artistic Treasures Gallery",
        "date_created": "2021-03-26",
        "description": "Artistic Treasures Gallery offers a wide range of products related to its category.",
        "opening_time": "10:00 AM",
        "closing_time": "8:00 PM",
        "website": "www.artistictreasuresgallery.com",
        "phone_number": "209-287-5235",
        "rating": 3.8,
        "distance": 3.4,
        "cost": 1,
        "payment_methods": 4,
        "products": [
            {
                "category": "Coins & Stamps",
                "product": "Collectible Coins",
                "description": "A treasure trove for collectors, featuring rare and historical coins from around the world.",
                "price": 130.33,
                "sku": "B5KKROH6",
                "quantity": 82,
                "date_created": "2023-01-20"
            },
            {
                "category": "Prints & Posters",
                "product": "Poster Art",
                "description": "Add character to any space with our diverse range of poster art, suitable for all tastes and styles.",
                "price": 92.76,
                "sku": "XQGH9X4E",
                "quantity": 68,
                "date_created": "2023-12-10"
            },
            {
                "category": "Collectible Cards",
                "product": "Collectible Card Games",
                "description": "Engage in strategic gameplay with our collection of collectible card games, a hit among gamers.",
                "price": 118.89,
                "sku": "RMXCOJ92",
                "quantity": 26,
                "date_created": "2023-10-11"
            },
            {
                "category": "Handmade Crafts",
                "product": "Handmade Pottery",
                "description": "Discover the beauty of craftsmanship with our handmade pottery, each piece unique and full of character.",
                "price": 204.7,
                "sku": "374OB9EL",
                "quantity": 5,
                "date_created": "2023-11-09"
            },
            {
                "category": "Sculptures",
                "product": "Figurative Sculptures",
                "description": "Elevate your decor with our range of figurative sculptures, showcasing artistic brilliance and creativity.",
                "price": 27.92,
                "sku": "WMXTMRMG",
                "quantity": 26,
                "date_created": "2023-06-28"
            },
            {
                "category": "Rare Books",
                "product": "Rare Children's Books",
                "description": "A nostalgic journey awaits with our selection of rare children's books, perfect for collectors and young readers.",
                "price": 380.58,
                "sku": "VFAY6VQ5",
                "quantity": 75,
                "date_created": "2023-12-27"
            },
            {
                "category": "Vintage Collectibles",
                "product": "Vintage Accessories",
                "description": "Explore our vintage accessories, offering a touch of history and elegance to your wardrobe or collection.",
                "price": 245.29,
                "sku": "QTKN5FLC",
                "quantity": 33,
                "date_created": "2023-03-20"
            },
            {
                "category": "Prints & Posters",
                "product": "Music Posters",
                "description": "Celebrate your favorite bands and artists with our collection of music posters, ideal for music enthusiasts.",
                "price": 52.19,
                "sku": "9K3H6425",
                "quantity": 94,
                "date_created": "2023-07-26"
            },
            {
                "category": "Vintage Collectibles",
                "product": "Vintage Vinyl Records",
                "description": "Relive the classics with our vintage vinyl records, a must-have for audiophiles and collectors.",
                "price": 376.81,
                "sku": "4B6AKKGS",
                "quantity": 31,
                "date_created": "2023-04-29"
            },
            {
                "category": "Antiques",
                "product": "Antique Jewelry",
                "description": "Adorn yourself with history with our exquisite collection of antique jewelry, each piece telling its own story.",
                "price": 43.68,
                "sku": "XQD0QUBJ",
                "quantity": 64,
                "date_created": "2023-08-23"
            },
            {
                "category": "Rare Books",
                "product": "Rare Science Fiction Books",
                "description": "Dive into other worlds with our rare science fiction books, a treat for avid readers and collectors.",
                "price": 300.4,
                "sku": "6KOPTU6T",
                "quantity": 22,
                "date_created": "2023-07-24"
            },
            {
                "category": "Collectible Cards",
                "product": "Non-Sports Cards",
                "description": "A unique collectible, our non-sports cards feature a variety of themes and interests.",
                "price": 360.93,
                "sku": "9QYM3GKO",
                "quantity": 81,
                "date_created": "2023-02-26"
            },
            {
                "category": "Sculptures",
                "product": "Metal Sculptures",
                "description": "Our metal sculptures are striking pieces of art, perfect for adding an industrial chic touch to any space.",
                "price": 393.7,
                "sku": "S890U1MA",
                "quantity": 1,
                "date_created": "2023-09-27"
            },
            {
                "category": "Vintage Collectibles",
                "product": "Vintage Postcards",
                "description": "Travel back in time with our collection of vintage postcards, capturing moments and places from the past.",
                "price": 272.44,
                "sku": "5TQUNGWG",
                "quantity": 98,
                "date_created": "2023-02-15"
            },
            {
                "category": "Antiques",
                "product": "Antique Coins",
                "description": "Step back in time with our collection of Antique Coins, perfect for collectors and history enthusiasts alike, each piece telling its own unique story.",
                "price": 35.07,
                "sku": "7OK8JBXU",
                "quantity": 64,
                "date_created": "2023-01-29"
            },
            {
                "category": "Antiques",
                "product": "Antique Rugs",
                "description": "Enhance your home with the timeless beauty of our antique rugs, each with its own unique history and charm.",
                "price": 191.76,
                "sku": "9KROMRR6",
                "quantity": 38,
                "date_created": "2023-12-05"
            },
            {
                "category": "Collectible Cards",
                "product": "Pok\u00e9mon Cards",
                "description": "Join the Pok\u00e9mon craze with our selection of Pok\u00e9mon cards, appealing to fans and collectors of all ages.",
                "price": 337.77,
                "sku": "HBQ1PBAW",
                "quantity": 12,
                "date_created": "2023-11-12"
            },
            {
                "category": "Coins & Stamps",
                "product": "Rare Stamps",
                "description": "A philatelist's dream, our rare stamps are a window to different eras and cultures.",
                "price": 115.66,
                "sku": "VU7STI44",
                "quantity": 28,
                "date_created": "2023-05-15"
            }
        ]
    },
    {
        "category": "Travel & Luggage",
        "name": "Travelers' Luggage Loft",
        "date_created": "2020-11-26",
        "description": "Travelers' Luggage Loft offers a wide range of products related to its category.",
        "opening_time": "9:00 AM",
        "closing_time": "5:00 PM",
        "website": "www.travelers'luggageloft.com",
        "phone_number": "492-757-1003",
        "rating": 4.3,
        "distance": 4.5,
        "cost": 2,
        "payment_methods": 2,
        "products": [
            {
                "category": "Backpacks",
                "product": "Daypacks",
                "description": "Compact and lightweight backpacks suitable for day trips, hiking, or daily commuting.",
                "price": 419.01,
                "sku": "PZD5XY85",
                "quantity": 40,
                "date_created": "2023-05-02"
            },
            {
                "category": "Suitcases & Travel Bags",
                "product": "Hardside Suitcases",
                "description": "Durable and protective luggage options, ideal for securing belongings during travel.",
                "price": 463.03,
                "sku": "T75P404F",
                "quantity": 8,
                "date_created": "2023-09-13"
            },
            {
                "category": "Travel Electronics",
                "product": "Noise-Canceling Headphones",
                "description": "Headphones designed to reduce ambient noise, providing an immersive listening experience.",
                "price": 160.68,
                "sku": "TP2MZPBB",
                "quantity": 67,
                "date_created": "2023-04-09"
            },
            {
                "category": "Travel Electronics",
                "product": "GPS Navigation Devices",
                "description": "Technology that provides directional assistance and route planning for travel and exploration.",
                "price": 176.3,
                "sku": "80EOFFCI",
                "quantity": 55,
                "date_created": "2023-09-05"
            },
            {
                "category": "Backpacks",
                "product": "Hydration Packs",
                "description": "Backpacks equipped with a water reservoir, allowing easy hydration during outdoor activities.",
                "price": 235.29,
                "sku": "8B6AZ9NR",
                "quantity": 24,
                "date_created": "2023-04-28"
            },
            {
                "category": "Camping & Hiking Gear",
                "product": "Backpacks",
                "description": "Versatile and practical, these backpacks are suitable for school, work, or travel.",
                "price": 412.12,
                "sku": "63NN87FF",
                "quantity": 49,
                "date_created": "2023-10-22"
            },
            {
                "category": "Maps & Navigation",
                "product": "City Maps",
                "description": "Detailed maps providing navigation and exploration guides for various cities around the world.",
                "price": 360.68,
                "sku": "WICGQ9XP",
                "quantity": 67,
                "date_created": "2023-04-27"
            },
            {
                "category": "Travel Books & Guides",
                "product": "Travel Maps",
                "description": "Detailed maps that are essential for navigating and exploring new places during travels.",
                "price": 452.64,
                "sku": "EJD4M8J7",
                "quantity": 27,
                "date_created": "2023-07-04"
            },
            {
                "category": "Backpacks",
                "product": "Rolling Backpacks",
                "description": "Backpacks with wheels, providing the convenience of rolling luggage with the versatility of a backpack.",
                "price": 177.29,
                "sku": "50RMLASR",
                "quantity": 53,
                "date_created": "2023-01-29"
            },
            {
                "category": "Backpacks",
                "product": "Travel Backpacks",
                "description": "Durable and functional backpacks designed specifically for travel, offering ample storage and organization features.",
                "price": 206.47,
                "sku": "7X54GUJ0",
                "quantity": 28,
                "date_created": "2023-09-01"
            },
            {
                "category": "Travel Security",
                "product": "Travel Locks",
                "description": "Secure locks designed to keep luggage safe during travel.",
                "price": 175.6,
                "sku": "99OEEWC6",
                "quantity": 29,
                "date_created": "2023-11-06"
            },
            {
                "category": "Travel Accessories",
                "product": "Travel Wallets",
                "description": "Compact wallets designed to keep travel documents, cards, and currency organized and secure.",
                "price": 409.41,
                "sku": "33ET82MX",
                "quantity": 70,
                "date_created": "2023-02-17"
            },
            {
                "category": "Suitcases & Travel Bags",
                "product": "Travel Totes",
                "description": "Spacious and stylish bags ideal for carrying essentials during travel or everyday use.",
                "price": 48.84,
                "sku": "225GPSZK",
                "quantity": 55,
                "date_created": "2023-10-25"
            },
            {
                "category": "Backpacks",
                "product": "Drawstring Backpacks",
                "description": "Lightweight and convenient backpacks with a drawstring closure, ideal for casual use or sports activities.",
                "price": 421.97,
                "sku": "UDWM5N87",
                "quantity": 43,
                "date_created": "2023-03-13"
            },
            {
                "category": "Travel Security",
                "product": "Portable Safes",
                "description": "Compact and secure safes for protecting valuables while traveling or on the go.",
                "price": 487.85,
                "sku": "Z8BDZ0QJ",
                "quantity": 18,
                "date_created": "2023-07-04"
            },
            {
                "category": "Travel Accessories",
                "product": "Travel Adapters",
                "description": "Essential accessories for international travel, allowing electronic devices to be used in different types of power outlets.",
                "price": 117.44,
                "sku": "W3VPT2ZE",
                "quantity": 81,
                "date_created": "2023-08-18"
            },
            {
                "category": "Travel Books & Guides",
                "product": "Road Trip Guides",
                "description": "Comprehensive guides offering tips and routes for planning the perfect road trip adventure.",
                "price": 178.06,
                "sku": "D8PX9SWT",
                "quantity": 24,
                "date_created": "2023-04-11"
            },
            {
                "category": "Travel Clothing",
                "product": "Quick-Dry Underwear",
                "description": "Comfortable underwear designed to dry quickly, ideal for travel or active lifestyles.",
                "price": 407.53,
                "sku": "2SOT25HL",
                "quantity": 61,
                "date_created": "2023-08-18"
            },
            {
                "category": "Camping & Hiking Gear",
                "product": "Hiking Boots",
                "description": "Sturdy and comfortable footwear designed for outdoor treks and hiking adventures.",
                "price": 395.59,
                "sku": "53ZO97YE",
                "quantity": 52,
                "date_created": "2023-02-01"
            }
        ]
    },
    {
        "category": "Beauty & Personal Care",
        "name": "Beauty & Care Boutique",
        "date_created": "2019-09-10",
        "description": "Beauty & Care Boutique offers a wide range of products related to its category.",
        "opening_time": "9:00 AM",
        "closing_time": "8:00 PM",
        "website": "www.beauty&careboutique.com",
        "phone_number": "490-647-4664",
        "rating": 3.2,
        "distance": 5.2,
        "cost": 2,
        "payment_methods": 1,
        "products": [
            {
                "category": "Men's Grooming",
                "product": "Dapper Dan Hair Styling Cream",
                "description": "A high-quality styling cream for achieving a range of hairstyles with a natural finish.",
                "price": 149.05,
                "sku": "VYWM9BLP",
                "quantity": 17,
                "date_created": "2023-06-27"
            },
            {
                "category": "Tools & Accessories",
                "product": "Makeup Organizer",
                "description": "A practical storage solution for organizing and accessing makeup products easily.",
                "price": 305.38,
                "sku": "SVSS68BY",
                "quantity": 16,
                "date_created": "2023-11-08"
            },
            {
                "category": "Makeup",
                "product": "L'Or\u00e9al Paris Foundation",
                "description": "A high-quality makeup foundation offering a range of shades for a flawless complexion.",
                "price": 262.62,
                "sku": "V82MVALY",
                "quantity": 74,
                "date_created": "2023-12-03"
            },
            {
                "category": "Men's Grooming",
                "product": "Baxter of California Pomade",
                "description": "A high-quality hair styling product offering a strong hold and a natural finish.",
                "price": 283.13,
                "sku": "B2FTI1KL",
                "quantity": 16,
                "date_created": "2023-01-23"
            },
            {
                "category": "Oral Care",
                "product": "Crest 3D White Toothpaste",
                "description": "A whitening toothpaste designed to remove surface stains and brighten teeth.",
                "price": 441.55,
                "sku": "SZYBAHBK",
                "quantity": 3,
                "date_created": "2023-03-05"
            },
            {
                "category": "Natural & Organic",
                "product": "Essential Oil Diffuser",
                "description": "A device that disperses essential oils into the air, creating a pleasant aroma and atmosphere.",
                "price": 47.91,
                "sku": "C3N3CFHK",
                "quantity": 32,
                "date_created": "2023-01-18"
            },
            {
                "category": "Haircare",
                "product": "Olaplex Hair Perfector No. 3",
                "description": "A hair treatment product designed to repair and strengthen damaged hair.",
                "price": 30.25,
                "sku": "5JEJTAXP",
                "quantity": 88,
                "date_created": "2023-09-19"
            },
            {
                "category": "Haircare",
                "product": "TRESemm\u00e9 Shampoo and Conditioner",
                "description": "A popular hair care brand offering products for various hair types and concerns.",
                "price": 249.16,
                "sku": "455M5LMH",
                "quantity": 4,
                "date_created": "2023-02-12"
            },
            {
                "category": "Natural & Organic",
                "product": "Organic Lavender Oil",
                "description": "A natural and soothing oil extracted from organic lavender, ideal for relaxation and aromatherapy.",
                "price": 418.34,
                "sku": "3EWGHZH7",
                "quantity": 75,
                "date_created": "2023-11-23"
            },
            {
                "category": "Men's Grooming",
                "product": "Cremo Beard Oil",
                "description": "A nourishing oil that softens and conditions beards, reducing itchiness and promoting growth.",
                "price": 280.57,
                "sku": "DT249B5D",
                "quantity": 84,
                "date_created": "2023-03-04"
            },
            {
                "category": "Bath & Body",
                "product": "Lavender Essential Oil",
                "description": "A soothing and aromatic oil commonly used for relaxation and stress relief.",
                "price": 446.45,
                "sku": "51K8BWF9",
                "quantity": 49,
                "date_created": "2023-09-22"
            },
            {
                "category": "Fragrances",
                "product": "Yves Saint Laurent Black Opium",
                "description": "A luxurious and seductive fragrance for women by Yves Saint Laurent.",
                "price": 237.15,
                "sku": "TRXREF6Y",
                "quantity": 94,
                "date_created": "2023-02-22"
            },
            {
                "category": "Makeup",
                "product": "Makeup Brushes Set",
                "description": "A comprehensive set of makeup brushes for applying a variety of cosmetics with precision.",
                "price": 121.26,
                "sku": "0AN3BV11",
                "quantity": 59,
                "date_created": "2023-12-15"
            },
            {
                "category": "Skincare",
                "product": "The Ordinary Niacinamide Serum",
                "description": "A skincare product known for its ability to improve skin texture and reduce blemishes.",
                "price": 422.24,
                "sku": "JXPG7OJZ",
                "quantity": 40,
                "date_created": "2023-08-26"
            },
            {
                "category": "Oral Care",
                "product": "Oral-B Electric Toothbrush",
                "description": "An advanced toothbrush offering effective cleaning and plaque removal for oral health.",
                "price": 249.58,
                "sku": "7V0QZMWA",
                "quantity": 57,
                "date_created": "2023-03-12"
            },
            {
                "category": "Natural & Organic",
                "product": "Argan Oil Hair Serum",
                "description": "A nourishing hair treatment, this serum uses Argan oil to add shine and reduce frizz.",
                "price": 306.15,
                "sku": "GGUU0A29",
                "quantity": 50,
                "date_created": "2023-08-31"
            },
            {
                "category": "Makeup",
                "product": "Too Faced Blush",
                "description": "A high-quality blush offering a natural and radiant flush of color to the cheeks.",
                "price": 380.22,
                "sku": "V3V70VX8",
                "quantity": 44,
                "date_created": "2023-10-11"
            },
            {
                "category": "Men's Grooming",
                "product": "Beard Trimmer",
                "description": "A convenient tool for maintaining and styling facial hair with precision.",
                "price": 239.15,
                "sku": "D4HU8MV1",
                "quantity": 23,
                "date_created": "2023-09-25"
            }
        ]
    },
    {
        "category": "Jewelry & Accessories",
        "name": "Elegant Accessories Emporium",
        "date_created": "2020-10-07",
        "description": "Elegant Accessories Emporium offers a wide range of products related to its category.",
        "opening_time": "10:00 AM",
        "closing_time": "7:00 PM",
        "website": "www.elegantaccessoriesemporium.com",
        "phone_number": "886-935-9357",
        "rating": 3.7,
        "distance": 0.8,
        "cost": 4,
        "payment_methods": 5,
        "products": [
            {
                "category": "Earrings",
                "product": "Stud Earrings",
                "description": "Simple and elegant earrings that sit directly on the earlobe, suitable for everyday wear.",
                "price": 458.23,
                "sku": "CAUHYDBX",
                "quantity": 89,
                "date_created": "2023-04-11"
            },
            {
                "category": "Scarves & Wraps",
                "product": "Blanket Scarves",
                "description": "Wrap yourself in warmth and style with our Blanket Scarves, a cozy and chic accessory perfect for chilly days and fashionable nights.",
                "price": 251.44,
                "sku": "VV6UJY7C",
                "quantity": 16,
                "date_created": "2023-02-01"
            },
            {
                "category": "Sunglasses",
                "product": "Sport Sunglasses",
                "description": "Durable sunglasses designed to protect eyes during outdoor sports and activities.",
                "price": 47.72,
                "sku": "9ZI4UB1U",
                "quantity": 36,
                "date_created": "2023-10-03"
            },
            {
                "category": "Necklaces & Pendants",
                "product": "Gold Necklaces",
                "description": "Elegant necklaces crafted in gold, ranging from simple chains to intricate designs.",
                "price": 137.39,
                "sku": "TKJ3E8JP",
                "quantity": 80,
                "date_created": "2023-01-20"
            },
            {
                "category": "Fashion Jewelry",
                "product": "Gothic Jewelry",
                "description": "Jewelry pieces featuring dark and intricate designs, often inspired by gothic aesthetics.",
                "price": 131.0,
                "sku": "KPW8193E",
                "quantity": 6,
                "date_created": "2023-12-30"
            },
            {
                "category": "Fashion Jewelry",
                "product": "Tribal Jewelry",
                "description": "Adorn yourself with the spirit of heritage with our Tribal Jewelry, blending traditional craftsmanship with contemporary fashion.",
                "price": 171.91,
                "sku": "6R7013BH",
                "quantity": 98,
                "date_created": "2023-11-12"
            },
            {
                "category": "Fine Jewelry",
                "product": "Custom Jewelry",
                "description": "Unique and personalized jewelry pieces crafted to reflect individual styles and preferences.",
                "price": 139.96,
                "sku": "TAIQKC4M",
                "quantity": 95,
                "date_created": "2023-01-22"
            },
            {
                "category": "Sunglasses",
                "product": "Mirrored Sunglasses",
                "description": "Fashionable sunglasses featuring reflective lenses, providing style and UV protection.",
                "price": 400.94,
                "sku": "OCJP7WGG",
                "quantity": 94,
                "date_created": "2023-04-21"
            },
            {
                "category": "Bracelets & Bangles",
                "product": "Wrap Bracelets",
                "description": "Fashionable bracelets that wrap around the wrist multiple times, often featuring beads or charms.",
                "price": 382.31,
                "sku": "GDQ1ULRN",
                "quantity": 52,
                "date_created": "2023-08-23"
            },
            {
                "category": "Watches",
                "product": "Chronograph Watches",
                "description": "Stylish watches featuring a stopwatch function, combining functionality with fashion.",
                "price": 294.21,
                "sku": "B0PQFZ0W",
                "quantity": 56,
                "date_created": "2023-10-14"
            },
            {
                "category": "Watches",
                "product": "Analog Watches",
                "description": "Timeless and elegant, these watches feature classic analog displays for a traditional look.",
                "price": 272.82,
                "sku": "R2HEPTO3",
                "quantity": 100,
                "date_created": "2023-10-18"
            },
            {
                "category": "Necklaces & Pendants",
                "product": "Nameplate Necklaces",
                "description": "Personalized necklaces featuring a name or word, often worn as a statement piece.",
                "price": 206.67,
                "sku": "EDFBOQ3A",
                "quantity": 58,
                "date_created": "2023-10-23"
            },
            {
                "category": "Rings",
                "product": "Promise Rings",
                "description": "Symbolic rings representing commitment and love, often exchanged between couples.",
                "price": 354.86,
                "sku": "LR1UZJCH",
                "quantity": 33,
                "date_created": "2023-11-21"
            },
            {
                "category": "Earrings",
                "product": "Ear Jackets",
                "description": "Unique earrings that adorn both the front and back of the earlobe, adding a modern twist to ear jewelry.",
                "price": 50.12,
                "sku": "704SKVCQ",
                "quantity": 34,
                "date_created": "2023-09-07"
            },
            {
                "category": "Earrings",
                "product": "Statement Earrings",
                "description": "Bold and eye-catching earrings that make a fashion statement.",
                "price": 336.84,
                "sku": "CBHPOV62",
                "quantity": 82,
                "date_created": "2023-04-02"
            },
            {
                "category": "Bracelets & Bangles",
                "product": "Tennis Bracelets",
                "description": "Elegant and thin bracelets adorned with a row of diamonds or gemstones.",
                "price": 86.75,
                "sku": "MMDQWON1",
                "quantity": 35,
                "date_created": "2023-07-26"
            },
            {
                "category": "Rings",
                "product": "Birthstone Rings",
                "description": "Personalized rings featuring gemstones that correspond to the wearer's birth month.",
                "price": 11.21,
                "sku": "2JQR8HYS",
                "quantity": 2,
                "date_created": "2023-10-30"
            },
            {
                "category": "Necklaces & Pendants",
                "product": "Pearl Necklaces",
                "description": "Classic necklaces featuring pearls, ideal for formal events or as a statement piece.",
                "price": 246.12,
                "sku": "JSP468L8",
                "quantity": 32,
                "date_created": "2024-01-12"
            }
        ]
    },
    {
        "category": "Pet Supplies",
        "name": "Pet Paradise Store",
        "date_created": "2021-12-10",
        "description": "Pet Paradise Store offers a wide range of products related to its category.",
        "opening_time": "10:00 AM",
        "closing_time": "6:00 PM",
        "website": "www.petparadisestore.com",
        "phone_number": "584-320-2384",
        "rating": 4.7,
        "distance": 0.6,
        "cost": 1,
        "payment_methods": 7,
        "products": [
            {
                "category": "Pet Grooming",
                "product": "Pet Bathing Tools",
                "description": "Make pet grooming a breeze with our range of Pet Bathing Tools, designed for a comfortable and efficient cleaning experience for your furry friends.",
                "price": 347.79,
                "sku": "FYE3QT65",
                "quantity": 96,
                "date_created": "2023-08-20"
            },
            {
                "category": "Cat Supplies",
                "product": "Cat Beds",
                "description": "Cozy and comfortable beds designed to provide a perfect sleeping spot for cats.",
                "price": 101.22,
                "sku": "LAXV44WW",
                "quantity": 29,
                "date_created": "2023-08-12"
            },
            {
                "category": "Fish & Aquarium",
                "product": "Aquarium Air Pumps",
                "description": "Essential for maintaining oxygen levels in aquariums, these pumps ensure a healthy environment for aquatic life.",
                "price": 157.07,
                "sku": "FLPG93VC",
                "quantity": 68,
                "date_created": "2023-11-19"
            },
            {
                "category": "Pet Health & Wellness",
                "product": "Joint Supplements for Pets",
                "description": "Supplements designed to support joint health and mobility in pets, particularly in older animals.",
                "price": 187.67,
                "sku": "I7FTNNA4",
                "quantity": 67,
                "date_created": "2023-05-30"
            },
            {
                "category": "Bird Supplies",
                "product": "Bird Cage Accessories",
                "description": "Enhancements for bird cages, including perches, feeders, and toys for avian enrichment.",
                "price": 360.27,
                "sku": "Z4FHX5PK",
                "quantity": 39,
                "date_created": "2024-01-07"
            },
            {
                "category": "Horse Supplies",
                "product": "Horse Stall Supplies",
                "description": "Ensure your equine's comfort with our premium Horse Stall Supplies, catering to all your horse care needs with top-quality products.",
                "price": 403.15,
                "sku": "1TNUGDIF",
                "quantity": 94,
                "date_created": "2023-11-01"
            },
            {
                "category": "Pet Grooming",
                "product": "Pet Towels and Dryers",
                "description": "Specially designed towels and dryers to quickly and gently dry pets after bathing.",
                "price": 35.17,
                "sku": "SEQVBQVV",
                "quantity": 88,
                "date_created": "2023-01-29"
            },
            {
                "category": "Dog Supplies",
                "product": "Dog Toys",
                "description": "A variety of toys designed to entertain and engage dogs, promoting exercise and mental stimulation.",
                "price": 300.89,
                "sku": "GQXRJ7MJ",
                "quantity": 39,
                "date_created": "2023-11-27"
            },
            {
                "category": "Bird Supplies",
                "product": "Bird Feeders",
                "description": "Bring nature closer to home with our charming Bird Feeders, perfect for attracting a variety of birds and adding beauty to your garden.",
                "price": 23.75,
                "sku": "Q3XHP2XB",
                "quantity": 4,
                "date_created": "2023-08-10"
            },
            {
                "category": "Fish & Aquarium",
                "product": "Fish Tank Cleaning Supplies",
                "description": "Keep your aquatic environment pristine with our Fish Tank Cleaning Supplies, essential for maintaining a healthy and clear habitat for your fish.",
                "price": 53.41,
                "sku": "FHJPLJBM",
                "quantity": 27,
                "date_created": "2023-04-14"
            },
            {
                "category": "Pet Grooming",
                "product": "Pet Ear and Eye Cleaners",
                "description": "Gentle and effective, our Pet Ear and Eye Cleaners are specially formulated to keep your pets' sensitive areas clean and healthy.",
                "price": 426.26,
                "sku": "Z0FURGYA",
                "quantity": 63,
                "date_created": "2023-05-17"
            },
            {
                "category": "Dog Supplies",
                "product": "Dog Beds",
                "description": "Spoil your dog with the ultimate comfort of our plush Dog Beds, ensuring your pet a cozy spot to rest and relax.",
                "price": 54.44,
                "sku": "LOLZIQUO",
                "quantity": 5,
                "date_created": "2023-05-18"
            },
            {
                "category": "Dog Supplies",
                "product": "Dog Bowls and Feeders",
                "description": "Essential items for feeding dogs, ensuring they have access to food and water.",
                "price": 353.65,
                "sku": "IXMEMA1R",
                "quantity": 19,
                "date_created": "2023-05-05"
            },
            {
                "category": "Cat Supplies",
                "product": "Cat Bowls and Feeders",
                "description": "Essential items for feeding cats, ensuring they have access to food and water.",
                "price": 193.99,
                "sku": "1QAGB3OW",
                "quantity": 36,
                "date_created": "2023-04-23"
            },
            {
                "category": "Cat Supplies",
                "product": "Cat Health and Wellness Products",
                "description": "Products designed to promote the health and wellbeing of cats, including supplements and grooming tools.",
                "price": 298.26,
                "sku": "CDKKEAOM",
                "quantity": 12,
                "date_created": "2023-08-28"
            },
            {
                "category": "Cat Supplies",
                "product": "Cat Toys",
                "description": "Entertain and stimulate your feline friend with our exciting range of Cat Toys, designed for endless fun and activity.",
                "price": 228.15,
                "sku": "F75XYSJ0",
                "quantity": 57,
                "date_created": "2023-10-12"
            },
            {
                "category": "Pet Health & Wellness",
                "product": "Pet Pain Relief Medications",
                "description": "Safe and effective medications to alleviate pain and discomfort in pets.",
                "price": 410.27,
                "sku": "5WUY6OIX",
                "quantity": 75,
                "date_created": "2023-06-09"
            }
        ]
    },
    {
        "category": "Sports & Outdoors",
        "name": "Active Sports Gear",
        "date_created": "2021-07-27",
        "description": "Active Sports Gear offers a wide range of products related to its category.",
        "opening_time": "10:00 AM",
        "closing_time": "8:00 PM",
        "website": "www.activesportsgear.com",
        "phone_number": "285-705-2949",
        "rating": 3.7,
        "distance": 5.9,
        "cost": 4,
        "payment_methods": 2,
        "products": [
            {
                "category": "Camping & Hiking",
                "product": "Camping Cookware Set",
                "description": "A collection of portable and durable cookware ideal for outdoor cooking.",
                "price": 407.36,
                "sku": "3XHX1SSY",
                "quantity": 6,
                "date_created": "2023-10-25"
            },
            {
                "category": "Team Sports",
                "product": "Volleyball",
                "description": "A popular team sport ball, designed for optimal performance in competitive volleyball games.",
                "price": 241.33,
                "sku": "4GW7YAZ9",
                "quantity": 9,
                "date_created": "2023-11-05"
            },
            {
                "category": "Winter Sports",
                "product": "Snowboard",
                "description": "A winter sports equipment designed for gliding over snow, popular in snowboarding activities.",
                "price": 78.22,
                "sku": "XI15M14P",
                "quantity": 31,
                "date_created": "2023-08-24"
            },
            {
                "category": "Cycling",
                "product": "Bike Lights",
                "description": "Safety accessories for bicycles, providing visibility and illumination during night rides.",
                "price": 431.27,
                "sku": "LJ0J4IBD",
                "quantity": 73,
                "date_created": "2023-12-12"
            },
            {
                "category": "Sports Apparel",
                "product": "Cycling Jerseys",
                "description": "Hit the road in style and comfort with our high-performance Cycling Jerseys, tailored for maximum mobility and breathability.",
                "price": 213.27,
                "sku": "AD6DDI4T",
                "quantity": 16,
                "date_created": "2023-12-15"
            },
            {
                "category": "Team Sports",
                "product": "Basketball",
                "description": "A durable and regulation-sized ball designed for competitive play and recreational use.",
                "price": 430.16,
                "sku": "FR4NMU21",
                "quantity": 13,
                "date_created": "2023-09-07"
            },
            {
                "category": "Golf",
                "product": "Golf Clubs Set",
                "description": "A comprehensive set of golf clubs, including drivers, irons, and putters, for various playing styles.",
                "price": 239.46,
                "sku": "2LHQYVD6",
                "quantity": 76,
                "date_created": "2023-07-03"
            },
            {
                "category": "Team Sports",
                "product": "Hockey Stick",
                "description": "A key piece of equipment for hockey players, designed for handling the puck and shooting goals.",
                "price": 350.63,
                "sku": "U93U38NC",
                "quantity": 81,
                "date_created": "2023-10-02"
            },
            {
                "category": "Team Sports",
                "product": "Baseball Glove",
                "description": "A vital piece of equipment for baseball players, providing protection and enhancing performance.",
                "price": 63.41,
                "sku": "MYWELU7A",
                "quantity": 10,
                "date_created": "2023-03-16"
            },
            {
                "category": "Sports Apparel",
                "product": "Performance Hoodies",
                "description": "Athletic hoodies designed for comfort and functionality during workouts or casual wear.",
                "price": 491.51,
                "sku": "J09STQ1A",
                "quantity": 82,
                "date_created": "2023-07-26"
            },
            {
                "category": "Winter Sports",
                "product": "Snow Sled",
                "description": "Embrace the winter thrill with our Snow Sled, an exciting way to enjoy the snowy slopes and make lasting memories.",
                "price": 284.26,
                "sku": "C90EKPCD",
                "quantity": 23,
                "date_created": "2023-01-20"
            },
            {
                "category": "Outdoor Recreation",
                "product": "Fishing Rod and Reel Combo",
                "description": "Experience the perfect cast with our Fishing Rod and Reel Combo, designed for anglers seeking reliability and precision.",
                "price": 419.33,
                "sku": "G0K8B9PZ",
                "quantity": 51,
                "date_created": "2023-02-02"
            },
            {
                "category": "Golf",
                "product": "Golf Bag",
                "description": "A durable bag designed to carry golf clubs and accessories, essential for any golfer.",
                "price": 148.78,
                "sku": "L6PWPMPE",
                "quantity": 93,
                "date_created": "2023-08-02"
            },
            {
                "category": "Fitness & Exercise Equipment",
                "product": "Dumbbell Set",
                "description": "A set of weights for strength training and fitness routines, suitable for home gyms.",
                "price": 24.9,
                "sku": "SY3GFQTR",
                "quantity": 35,
                "date_created": "2023-07-19"
            },
            {
                "category": "Cycling",
                "product": "Cycling Gloves",
                "description": "Designed to provide comfort and grip for cyclists, these gloves protect hands during rides.",
                "price": 156.61,
                "sku": "SKPN5ETD",
                "quantity": 36,
                "date_created": "2023-04-22"
            },
            {
                "category": "Sports Nutrition",
                "product": "BCAA Supplements",
                "description": "Branched-Chain Amino Acid supplements support muscle recovery and enhance exercise performance.",
                "price": 260.38,
                "sku": "CHF1QET1",
                "quantity": 90,
                "date_created": "2023-08-01"
            }
        ]
    },
    {
        "category": "Baby Products",
        "name": "Baby Joy Boutique",
        "date_created": "2019-07-01",
        "description": "Baby Joy Boutique offers a wide range of products related to its category.",
        "opening_time": "10:00 AM",
        "closing_time": "6:00 PM",
        "website": "www.babyjoyboutique.com",
        "phone_number": "961-659-2302",
        "rating": 3.8,
        "distance": 2.4,
        "cost": 2,
        "payment_methods": 3,
        "products": [
            {
                "category": "Bathing & Skin Care",
                "product": "Baby Lotion",
                "description": "This mild lotion moisturizes and protects baby's sensitive skin, keeping it soft and smooth.",
                "price": 447.61,
                "sku": "MF4GP6U5",
                "quantity": 43,
                "date_created": "2023-08-10"
            },
            {
                "category": "Bathing & Skin Care",
                "product": "Baby Body Wash",
                "description": "Gentle and hypoallergenic, this body wash is formulated to cleanse and soothe baby's delicate skin.",
                "price": 132.52,
                "sku": "0UJZZOCO",
                "quantity": 84,
                "date_created": "2023-10-11"
            },
            {
                "category": "Baby Safety",
                "product": "Baby Proofing Kits",
                "description": "Protect your little explorer with our comprehensive Baby Proofing Kits, ensuring a safe and secure environment for your child.",
                "price": 264.02,
                "sku": "YPNYIBL1",
                "quantity": 59,
                "date_created": "2023-09-12"
            },
            {
                "category": "Diapers & Wipes",
                "product": "Baby Wipes",
                "description": "Convenient and gentle, these wipes are ideal for cleaning and refreshing baby's skin on the go.",
                "price": 91.75,
                "sku": "ZVM8SBOP",
                "quantity": 92,
                "date_created": "2023-07-28"
            },
            {
                "category": "Baby Clothing & Accessories",
                "product": "Baby Rompers",
                "description": "Comfortable and stylish, these one-piece garments are perfect for playtime and naps.",
                "price": 186.86,
                "sku": "BBR77NA8",
                "quantity": 22,
                "date_created": "2023-01-17"
            },
            {
                "category": "Baby Health",
                "product": "Baby Oral Care",
                "description": "Products specifically designed to maintain the oral hygiene of babies, promoting healthy teeth and gums.",
                "price": 38.35,
                "sku": "PNI0BR5P",
                "quantity": 14,
                "date_created": "2024-01-13"
            },
            {
                "category": "Bathing & Skin Care",
                "product": "Baby Powder",
                "description": "Made with gentle ingredients, this powder helps absorb moisture and prevent diaper rash.",
                "price": 120.75,
                "sku": "F62YTB00",
                "quantity": 25,
                "date_created": "2023-05-21"
            },
            {
                "category": "Nursery Furniture",
                "product": "Cradles",
                "description": "A secure and soothing sleeping option for infants, often featuring gentle rocking motions.",
                "price": 448.82,
                "sku": "M8F8XNCS",
                "quantity": 30,
                "date_created": "2023-11-29"
            },
            {
                "category": "Strollers & Car Seats",
                "product": "Umbrella Strollers",
                "description": "Lightweight and compact strollers, perfect for quick trips and easy maneuverability.",
                "price": 497.5,
                "sku": "PPEVN89H",
                "quantity": 2,
                "date_created": "2023-12-23"
            },
            {
                "category": "Nursery Furniture",
                "product": "Crib Mobiles",
                "description": "Decorative and entertaining mobiles that hang above cribs to soothe and engage babies.",
                "price": 211.9,
                "sku": "53H3VPFH",
                "quantity": 18,
                "date_created": "2023-05-02"
            },
            {
                "category": "Baby Safety",
                "product": "Cabinet Locks",
                "description": "Safety devices to secure cabinets and prevent children from accessing dangerous items.",
                "price": 263.25,
                "sku": "8ROFMYHZ",
                "quantity": 30,
                "date_created": "2023-11-19"
            },
            {
                "category": "Nursery Furniture",
                "product": "Baby Cribs",
                "description": "Designed for safety and comfort, these cribs provide a cozy sleeping area for infants.",
                "price": 104.02,
                "sku": "AK0BFOGZ",
                "quantity": 70,
                "date_created": "2023-02-05"
            },
            {
                "category": "Baby Safety",
                "product": "Door Locks",
                "description": "Devices that provide security and privacy for homes and buildings.",
                "price": 426.7,
                "sku": "NI4XPCGN",
                "quantity": 35,
                "date_created": "2023-06-11"
            },
            {
                "category": "Baby Safety",
                "product": "Baby Gates",
                "description": "Essential for childproofing, these gates prevent babies from accessing potentially dangerous areas.",
                "price": 99.2,
                "sku": "CJAZ6DNU",
                "quantity": 100,
                "date_created": "2023-11-16"
            },
            {
                "category": "Strollers & Car Seats",
                "product": "Convertible Car Seats",
                "description": "Travel with peace of mind with our Convertible Car Seats, combining safety, comfort, and versatility for your growing child.",
                "price": 329.27,
                "sku": "4LDI026Z",
                "quantity": 18,
                "date_created": "2023-11-14"
            },
            {
                "category": "Bathing & Skin Care",
                "product": "Baby Washcloths",
                "description": "Soft and absorbent, these washcloths are perfect for gently cleaning baby's skin.",
                "price": 258.4,
                "sku": "T33R70Q0",
                "quantity": 87,
                "date_created": "2023-03-18"
            },
            {
                "category": "Diapers & Wipes",
                "product": "Diaper Rash Creams",
                "description": "Creams formulated to soothe and heal diaper rash, providing relief for babies.",
                "price": 394.29,
                "sku": "K111SDDS",
                "quantity": 57,
                "date_created": "2023-11-03"
            },
            {
                "category": "Feeding & Nursing",
                "product": "Baby Spoons",
                "description": "Soft-tipped and easy to handle, these spoons are ideal for introducing solid foods to babies.",
                "price": 198.63,
                "sku": "FPWSLSKB",
                "quantity": 95,
                "date_created": "2023-09-13"
            },
            {
                "category": "Feeding & Nursing",
                "product": "Nursing Covers",
                "description": "Discreet and comfortable covers for breastfeeding mothers, providing privacy and convenience.",
                "price": 311.0,
                "sku": "2HF3M6VN",
                "quantity": 32,
                "date_created": "2023-02-24"
            }
        ]
    },
    {
        "category": "Art & Collectibles",
        "name": "Collector's Art & Craft",
        "date_created": "2020-04-21",
        "description": "Collector's Art & Craft offers a wide range of products related to its category.",
        "opening_time": "8:00 AM",
        "closing_time": "5:00 PM",
        "website": "www.collector'sart&craft.com",
        "phone_number": "111-271-9201",
        "rating": 2.0,
        "distance": 4.5,
        "cost": 1,
        "payment_methods": 1,
        "products": [
            {
                "category": "Sculptures",
                "product": "Stone Sculptures",
                "description": "Enhance your kitchen decor with our stone sculptures. These exquisite pieces are designed with attention to detail and offer exceptional aesthetics.",
                "price": 109.45,
                "sku": "E2VY2NHL",
                "quantity": 66,
                "date_created": "2023-11-02"
            },
            {
                "category": "Coins & Stamps",
                "product": "Gold Coins",
                "description": "Explore our collection of gold coins, perfect for collectors and investors alike. Each coin is of high quality and offers a valuable addition to your collection.",
                "price": 191.1,
                "sku": "GIBA6NO7",
                "quantity": 41,
                "date_created": "2024-01-11"
            },
            {
                "category": "Coins & Stamps",
                "product": "Vintage Stamps",
                "description": "Discover vintage stamps that tell the stories of the past. Our collection features rare and historical stamps that are a must-have for philatelists.",
                "price": 220.83,
                "sku": "UNNG4TZL",
                "quantity": 26,
                "date_created": "2023-01-23"
            },
            {
                "category": "Vintage Collectibles",
                "product": "Vintage Postcards",
                "description": "Step into the world of vintage postcards with our curated selection. These postcards capture moments in history and offer a glimpse into the past.",
                "price": 387.29,
                "sku": "HUMKV72H",
                "quantity": 39,
                "date_created": "2023-11-22"
            },
            {
                "category": "Vintage Collectibles",
                "product": "Vintage Toys",
                "description": "Relive nostalgia with our vintage toy collection. From classic action figures to timeless toys, they make perfect additions to any collection.",
                "price": 460.83,
                "sku": "TR42GAWP",
                "quantity": 2,
                "date_created": "2023-02-10"
            },
            {
                "category": "Antiques",
                "product": "Antique Jewelry",
                "description": "Adorn yourself with our antique jewelry pieces. These timeless accessories exude elegance and are perfect for special occasions.",
                "price": 316.99,
                "sku": "NGIZZQQX",
                "quantity": 41,
                "date_created": "2023-09-25"
            },
            {
                "category": "Rare Books",
                "product": "Collectible Books",
                "description": "Expand your library with our collectible books. From rare editions to literary gems, our collection caters to book enthusiasts.",
                "price": 490.89,
                "sku": "AH0O072I",
                "quantity": 69,
                "date_created": "2023-03-31"
            },
            {
                "category": "Antiques",
                "product": "Antique Watches",
                "description": "Elevate your style with our antique watches. Each timepiece is a work of art and a testament to timeless craftsmanship.",
                "price": 198.41,
                "sku": "A23VKFR6",
                "quantity": 34,
                "date_created": "2023-08-30"
            },
            {
                "category": "Paintings",
                "product": "Modern Art Paintings",
                "description": "Experience the world of modern art with our curated paintings. These pieces reflect contemporary artistic expressions.",
                "price": 149.5,
                "sku": "UKLTVE03",
                "quantity": 72,
                "date_created": "2023-07-06"
            },
            {
                "category": "Rare Books",
                "product": "First Edition Books",
                "description": "Add to your literary collection with first edition books. These rare and valuable books are a treasure for book collectors.",
                "price": 427.13,
                "sku": "PJUCT9HO",
                "quantity": 3,
                "date_created": "2023-04-15"
            },
            {
                "category": "Paintings",
                "product": "Watercolor Paintings",
                "description": "Enhance your living space with watercolor paintings. These artworks bring a touch of color and beauty to your home.",
                "price": 21.15,
                "sku": "DP5V1SBO",
                "quantity": 78,
                "date_created": "2023-07-09"
            },
            {
                "category": "Antiques",
                "product": "Antique Coins",
                "description": "Explore our collection of antique coins from various eras and regions. Each coin has a unique history and significance.",
                "price": 269.49,
                "sku": "LDS9ZK7S",
                "quantity": 17,
                "date_created": "2023-03-20"
            },
            {
                "category": "Prints & Posters",
                "product": "Canvas Prints",
                "description": "Decorate your space with canvas prints that showcase art in a visually stunning way. These prints are both beautiful and durable.",
                "price": 395.13,
                "sku": "R7H25RHA",
                "quantity": 19,
                "date_created": "2023-03-03"
            },
            {
                "category": "Rare Books",
                "product": "Rare Children's Books",
                "description": "Introduce young readers to the world of rare children's books. Our collection includes cherished stories for all ages.",
                "price": 277.74,
                "sku": "7GU1RAY1",
                "quantity": 49,
                "date_created": "2023-06-12"
            },
            {
                "category": "Collectible Cards",
                "product": "Magic: The Gathering Cards",
                "description": "Dive into the world of card gaming with Magic: The Gathering cards. These collectible cards offer strategic gameplay and excitement.",
                "price": 386.4,
                "sku": "AJO9778R",
                "quantity": 67,
                "date_created": "2023-04-08"
            },
            {
                "category": "Antiques",
                "product": "Antique Lamps",
                "description": "Illuminate your home with antique lamps that exude charm and sophistication. These lamps are both functional and decorative.",
                "price": 428.21,
                "sku": "JBCMRD88",
                "quantity": 10,
                "date_created": "2024-01-04"
            },
            {
                "category": "Handmade Crafts",
                "product": "Handmade Jewelry",
                "description": "Adorn yourself with our handmade jewelry. Each piece is crafted with care and offers a unique and personal touch.",
                "price": 225.85,
                "sku": "INN0RWFT",
                "quantity": 8,
                "date_created": "2023-07-15"
            },
            {
                "category": "Handmade Crafts",
                "product": "Handmade Pottery",
                "description": "Decorate your kitchen with handmade pottery. These pieces are not only functional but also works of art.",
                "price": 458.4,
                "sku": "5S6TSYA7",
                "quantity": 20,
                "date_created": "2023-09-14"
            },
            {
                "category": "Sculptures",
                "product": "Metal Sculptures",
                "description": "Add a touch of artistry to your kitchen with metal sculptures. These sculptures are both decorative and conversation-starters.",
                "price": 262.57,
                "sku": "FB66KQPE",
                "quantity": 91,
                "date_created": "2023-11-30"
            },
            {
                "category": "Collectible Cards",
                "product": "Non-Sports Cards",
                "description": "Collect non-sports cards that feature various themes and characters. These cards are a great addition to any card collection.",
                "price": 257.8,
                "sku": "F09WQEW6",
                "quantity": 4,
                "date_created": "2023-10-06"
            }
        ]
    },
    {
        "category": "Jewelry & Accessories",
        "name": "Luxury Jewelry Corner",
        "date_created": "2023-02-11",
        "description": "Luxury Jewelry Corner offers a wide range of products related to its category.",
        "opening_time": "8:00 AM",
        "closing_time": "8:00 PM",
        "website": "www.luxuryjewelrycorner.com",
        "phone_number": "391-910-7027",
        "rating": 2.8,
        "distance": 2.8,
        "cost": 3,
        "payment_methods": 5,
        "products": [
            {
                "category": "Scarves & Wraps",
                "product": "Silk Scarves",
                "description": "Luxurious scarves made from silk, adding a touch of elegance to any outfit.",
                "price": 231.24,
                "sku": "QNOCZRBH",
                "quantity": 24,
                "date_created": "2023-05-09"
            },
            {
                "category": "Handbags & Wallets",
                "product": "Crossbody Bags",
                "description": "Trendy and convenient bags worn across the body, ideal for everyday use.",
                "price": 329.78,
                "sku": "00CYHPDA",
                "quantity": 54,
                "date_created": "2023-01-18"
            },
            {
                "category": "Watches",
                "product": "Dress Watches",
                "description": "Elevate your style with our exquisite Dress Watches, the perfect blend of elegance and sophistication for any formal occasion.",
                "price": 173.9,
                "sku": "X95NXY7U",
                "quantity": 75,
                "date_created": "2023-06-08"
            },
            {
                "category": "Necklaces & Pendants",
                "product": "Pearl Necklaces",
                "description": "Classic necklaces featuring pearls, ideal for formal events or as a statement piece.",
                "price": 339.62,
                "sku": "QSUUYKMM",
                "quantity": 41,
                "date_created": "2024-01-13"
            },
            {
                "category": "Bracelets & Bangles",
                "product": "Link Bracelets",
                "description": "Stylish bracelets consisting of linked pieces, suitable for both casual and formal wear.",
                "price": 93.95,
                "sku": "TMGGVQU8",
                "quantity": 95,
                "date_created": "2023-12-11"
            },
            {
                "category": "Scarves & Wraps",
                "product": "Blanket Scarves",
                "description": "Wrap yourself in warmth and style with our Blanket Scarves, a cozy and chic accessory perfect for chilly days and fashionable nights.",
                "price": 455.21,
                "sku": "NBLR4L1N",
                "quantity": 15,
                "date_created": "2023-12-15"
            },
            {
                "category": "Fashion Jewelry",
                "product": "Retro Jewelry",
                "description": "Vintage-inspired jewelry pieces that bring a nostalgic charm to any fashion ensemble.",
                "price": 480.94,
                "sku": "2JIIJNKE",
                "quantity": 58,
                "date_created": "2023-12-10"
            },
            {
                "category": "Fashion Jewelry",
                "product": "Costume Jewelry",
                "description": "Fashionable and affordable jewelry pieces that add a touch of glamour to any outfit.",
                "price": 332.6,
                "sku": "HP3JDRDI",
                "quantity": 37,
                "date_created": "2023-04-24"
            },
            {
                "category": "Necklaces & Pendants",
                "product": "Heart Necklaces",
                "description": "Express your love and affection with our elegant Heart Necklaces, a timeless symbol of romance and devotion.",
                "price": 314.03,
                "sku": "PF84U71T",
                "quantity": 62,
                "date_created": "2023-12-21"
            },
            {
                "category": "Earrings",
                "product": "Dangle Earrings",
                "description": "Elegant earrings that hang below the earlobe, adding a touch of sophistication to any look.",
                "price": 72.65,
                "sku": "7DHSJGAV",
                "quantity": 82,
                "date_created": "2023-05-16"
            },
            {
                "category": "Fine Jewelry",
                "product": "Silver Jewelry",
                "description": "Beautiful jewelry pieces crafted from silver, offering a sleek and modern aesthetic.",
                "price": 26.94,
                "sku": "5QDJ4E2J",
                "quantity": 96,
                "date_created": "2023-09-10"
            },
            {
                "category": "Rings",
                "product": "Midi Rings",
                "description": "Trendy rings worn on the middle section of the fingers, adding a fashionable touch to any outfit.",
                "price": 329.28,
                "sku": "RQ4OIICN",
                "quantity": 38,
                "date_created": "2023-03-10"
            },
            {
                "category": "Fine Jewelry",
                "product": "Diamond Jewelry",
                "description": "Exquisite jewelry pieces adorned with diamonds, symbolizing luxury and elegance.",
                "price": 95.99,
                "sku": "VH31NMYL",
                "quantity": 75,
                "date_created": "2023-03-23"
            },
            {
                "category": "Bracelets & Bangles",
                "product": "ID Bracelets",
                "description": "Personalized bracelets featuring identification details, often used for medical or safety purposes.",
                "price": 21.03,
                "sku": "5SAT2NLO",
                "quantity": 33,
                "date_created": "2023-01-31"
            },
            {
                "category": "Earrings",
                "product": "Pearl Earrings",
                "description": "Elegant earrings featuring pearls, perfect for adding a touch of class to any outfit.",
                "price": 223.07,
                "sku": "EQ7ZLK7T",
                "quantity": 66,
                "date_created": "2023-03-26"
            },
            {
                "category": "Watches",
                "product": "Automatic Watches",
                "description": "Sophisticated timepieces powered by the natural motion of the wearer's wrist.",
                "price": 258.62,
                "sku": "4GC4YQY0",
                "quantity": 72,
                "date_created": "2023-12-29"
            },
            {
                "category": "Earrings",
                "product": "Stud Earrings",
                "description": "Simple and elegant earrings that sit directly on the earlobe, suitable for everyday wear.",
                "price": 256.07,
                "sku": "NNTFPKR4",
                "quantity": 43,
                "date_created": "2023-10-15"
            },
            {
                "category": "Sunglasses",
                "product": "Wayfarer Sunglasses",
                "description": "A classic sunglasses style known for its timeless design and versatile appeal.",
                "price": 104.17,
                "sku": "PWHX4PRI",
                "quantity": 32,
                "date_created": "2023-05-12"
            },
            {
                "category": "Fashion Jewelry",
                "product": "Statement Jewelry",
                "description": "Jewelry pieces that stand out and add a distinctive touch to any outfit.",
                "price": 344.51,
                "sku": "U09P5R8G",
                "quantity": 92,
                "date_created": "2023-03-01"
            }
        ]
    },
    {
        "category": "Home & Kitchen",
        "name": "Cozy Home Decor Studio",
        "date_created": "2023-12-17",
        "description": "Cozy Home Decor Studio offers a wide range of products related to its category.",
        "opening_time": "10:00 AM",
        "closing_time": "7:00 PM",
        "website": "www.cozyhomedecorstudio.com",
        "phone_number": "194-335-8370",
        "rating": 4.6,
        "distance": 2.2,
        "cost": 2,
        "payment_methods": 6,
        "products": [
            {
                "category": "Smart Home Devices",
                "product": "Wireless Security Camera",
                "description": "A camera that operates without cords, allowing for flexible placement and remote monitoring.",
                "price": 253.75,
                "sku": "OV3PK18I",
                "quantity": 55,
                "date_created": "2023-08-27"
            },
            {
                "category": "Bedding & Linens",
                "product": "Duvet Cover Set",
                "description": "A stylish and practical set for dressing a duvet, often including pillow shams for a coordinated look.",
                "price": 465.54,
                "sku": "SQCYRK3S",
                "quantity": 7,
                "date_created": "2023-06-12"
            },
            {
                "category": "Cleaning Supplies",
                "product": "Mop and Bucket",
                "description": "Essential cleaning tools for maintaining clean and hygienic floors in homes and offices.",
                "price": 305.18,
                "sku": "COM3XALO",
                "quantity": 11,
                "date_created": "2023-08-16"
            },
            {
                "category": "Kitchen Appliances",
                "product": "Keurig Coffee Maker",
                "description": "A convenient and modern coffee brewing system, allowing for single-cup coffee preparation.",
                "price": 108.76,
                "sku": "LOC8HMAY",
                "quantity": 52,
                "date_created": "2023-08-05"
            },
            {
                "category": "Bedding & Linens",
                "product": "Bedspread",
                "description": "A decorative and comfortable covering for beds, adding warmth and style to the bedroom.",
                "price": 61.25,
                "sku": "NLDB05E6",
                "quantity": 23,
                "date_created": "2023-01-28"
            },
            {
                "category": "Bedding & Linens",
                "product": "Bed Skirt",
                "description": "An elegant addition to a bed set, hiding the bed frame and creating a polished look.",
                "price": 321.62,
                "sku": "ZSN15N81",
                "quantity": 83,
                "date_created": "2023-11-28"
            },
            {
                "category": "Dining & Tableware",
                "product": "Dinnerware Set",
                "description": "A complete set of plates, bowls, and other tableware, perfect for everyday use or special occasions.",
                "price": 209.23,
                "sku": "2FAFNR7W",
                "quantity": 55,
                "date_created": "2023-12-07"
            },
            {
                "category": "Home D\u00e9cor",
                "product": "Artificial Plants",
                "description": "Lifelike and maintenance-free, these plants add a touch of greenery to any space without the need for watering.",
                "price": 441.19,
                "sku": "FODQD6B2",
                "quantity": 86,
                "date_created": "2023-05-23"
            },
            {
                "category": "Home Improvement Tools",
                "product": "Cordless Drill",
                "description": "A versatile and powerful tool for various drilling and screw-driving tasks around the home.",
                "price": 475.65,
                "sku": "K97OHTUH",
                "quantity": 57,
                "date_created": "2023-06-25"
            },
            {
                "category": "Storage & Organization",
                "product": "Storage Bins",
                "description": "Practical containers for organizing and storing various items in homes or offices.",
                "price": 257.35,
                "sku": "GOZFSQ8K",
                "quantity": 10,
                "date_created": "2023-08-26"
            },
            {
                "category": "Furniture",
                "product": "TV Stand",
                "description": "A piece of furniture designed to hold and display a television set, often with additional storage.",
                "price": 461.19,
                "sku": "RHHTPND9",
                "quantity": 33,
                "date_created": "2023-12-15"
            },
            {
                "category": "Dining & Tableware",
                "product": "Serving Platter",
                "description": "A large dish ideal for presenting and serving food at gatherings or family meals.",
                "price": 253.39,
                "sku": "L5G45HVS",
                "quantity": 59,
                "date_created": "2023-10-28"
            },
            {
                "category": "Cookware & Bakeware",
                "product": "KitchenAid Stand Mixer",
                "description": "A versatile and powerful kitchen appliance for mixing, kneading, and whipping a variety of ingredients.",
                "price": 190.6,
                "sku": "72RM6BXK",
                "quantity": 92,
                "date_created": "2023-12-13"
            },
            {
                "category": "Home D\u00e9cor",
                "product": "Wall Clock",
                "description": "A functional and decorative item, wall clocks are used to display time and enhance room decor.",
                "price": 459.05,
                "sku": "NB8OLN41",
                "quantity": 57,
                "date_created": "2023-03-02"
            },
            {
                "category": "Cleaning Supplies",
                "product": "Trash Bags",
                "description": "Essential for waste management, these bags are designed to contain and dispose of trash.",
                "price": 279.2,
                "sku": "ZJWBAFTV",
                "quantity": 63,
                "date_created": "2023-01-26"
            },
            {
                "category": "Smart Home Devices",
                "product": "Mesh WiFi System",
                "description": "A network solution that provides extensive and reliable WiFi coverage throughout a home or office.",
                "price": 493.74,
                "sku": "PCM8JM1B",
                "quantity": 41,
                "date_created": "2023-12-11"
            },
            {
                "category": "Bedding & Linens",
                "product": "Down Comforter",
                "description": "A warm and luxurious bedding option filled with down feathers for ultimate comfort.",
                "price": 125.77,
                "sku": "1PV6AL8H",
                "quantity": 31,
                "date_created": "2023-08-25"
            },
            {
                "category": "Kitchen Appliances",
                "product": "Vitamix Blender",
                "description": "A high-performance blender known for its durability and versatility in the kitchen.",
                "price": 358.52,
                "sku": "WY8AUC66",
                "quantity": 65,
                "date_created": "2023-07-11"
            },
            {
                "category": "Dining & Tableware",
                "product": "Flatware Set",
                "description": "A complete collection of utensils including forks, knives, and spoons for dining.",
                "price": 480.48,
                "sku": "Z2575YBI",
                "quantity": 44,
                "date_created": "2023-11-16"
            }
        ]
    },
    {
        "category": "Grocery & Gourmet Food",
        "name": "Gourmet Delights Grocery",
        "date_created": "2020-04-20",
        "description": "Gourmet Delights Grocery offers a wide range of products related to its category.",
        "opening_time": "10:00 AM",
        "closing_time": "8:00 PM",
        "website": "www.gourmetdelightsgrocery.com",
        "phone_number": "892-803-5223",
        "rating": 2.5,
        "distance": 4.3,
        "cost": 4,
        "payment_methods": 7,
        "products": [
            {
                "category": "Dairy & Eggs",
                "product": "Eggs",
                "description": "A staple food rich in protein, perfect for a variety of cooking and baking recipes.",
                "price": 276.67,
                "sku": "86G8946L",
                "quantity": 90,
                "date_created": "2023-05-14"
            },
            {
                "category": "International Foods",
                "product": "Japanese Ramen Ingredients",
                "description": "Essential ingredients for preparing authentic Japanese ramen dishes at home.",
                "price": 11.64,
                "sku": "U72FY9ET",
                "quantity": 56,
                "date_created": "2023-12-30"
            },
            {
                "category": "Meat & Seafood",
                "product": "Pork Chops",
                "description": "A popular cut of pork, ideal for grilling, frying, or baking, known for its tenderness and flavor.",
                "price": 143.95,
                "sku": "BZCI86OR",
                "quantity": 78,
                "date_created": "2023-02-09"
            },
            {
                "category": "Organic Foods",
                "product": "Organic Fruits",
                "description": "Savor the taste of health with our Organic Fruits, naturally grown for the best in flavor and nutritional goodness.",
                "price": 219.09,
                "sku": "BAM5DAZD",
                "quantity": 81,
                "date_created": "2023-03-20"
            },
            {
                "category": "Special Diet Foods",
                "product": "Vegan Snacks",
                "description": "Delicious and cruelty-free snacks, made without any animal products, suitable for vegans and health-conscious individuals.",
                "price": 319.87,
                "sku": "I9DW2AU2",
                "quantity": 8,
                "date_created": "2023-01-31"
            },
            {
                "category": "Snacks & Sweets",
                "product": "Potato Chips",
                "description": "A crunchy and savory snack, perfect for munching on during movies or gatherings.",
                "price": 112.94,
                "sku": "BA0O3XLU",
                "quantity": 39,
                "date_created": "2023-05-18"
            },
            {
                "category": "International Foods",
                "product": "Chinese Cuisine Ingredients",
                "description": "A range of authentic ingredients essential for preparing traditional Chinese dishes.",
                "price": 348.1,
                "sku": "MBACSWKR",
                "quantity": 82,
                "date_created": "2023-07-12"
            },
            {
                "category": "International Foods",
                "product": "Middle Eastern Cuisine Ingredients",
                "description": "Key ingredients for cooking traditional Middle Eastern dishes, rich in flavors and spices.",
                "price": 157.32,
                "sku": "O96NG15O",
                "quantity": 97,
                "date_created": "2023-01-19"
            },
            {
                "category": "Meat & Seafood",
                "product": "Salmon Fillet",
                "description": "A healthy and delicious fish option, perfect for grilling, baking, or pan-frying.",
                "price": 223.5,
                "sku": "0HPWAX5U",
                "quantity": 25,
                "date_created": "2023-01-25"
            },
            {
                "category": "Special Diet Foods",
                "product": "Sugar-Free Snacks",
                "description": "Healthier snack options without added sugars, catering to dietary preferences and needs.",
                "price": 247.93,
                "sku": "TDNNDF9X",
                "quantity": 52,
                "date_created": "2023-05-29"
            },
            {
                "category": "Organic Foods",
                "product": "Organic Vegetables",
                "description": "Fresh and nutritious vegetables grown without the use of synthetic pesticides or fertilizers.",
                "price": 149.13,
                "sku": "PU68KG3G",
                "quantity": 35,
                "date_created": "2023-08-09"
            },
            {
                "category": "Pantry Staples",
                "product": "Olive Oil",
                "description": "A versatile and healthy cooking oil, known for its flavor and nutritional benefits.",
                "price": 259.67,
                "sku": "6J7RQQVT",
                "quantity": 48,
                "date_created": "2023-11-22"
            },
            {
                "category": "Snacks & Sweets",
                "product": "Chocolate Bars",
                "description": "Delicious and indulgent, these bars are a perfect treat for those with a sweet tooth.",
                "price": 272.17,
                "sku": "8FJWZY1U",
                "quantity": 100,
                "date_created": "2023-11-21"
            },
            {
                "category": "Beverages",
                "product": "Energy Drinks",
                "description": "Beverages designed to boost energy and increase alertness, often containing caffeine and vitamins.",
                "price": 167.78,
                "sku": "CPH2W635",
                "quantity": 4,
                "date_created": "2023-07-18"
            },
            {
                "category": "Snacks & Sweets",
                "product": "Granola Bars",
                "description": "Convenient and nutritious snack bars made with granola and other wholesome ingredients.",
                "price": 168.12,
                "sku": "16ZWHAGV",
                "quantity": 67,
                "date_created": "2023-11-28"
            },
            {
                "category": "Organic Foods",
                "product": "Organic Cereals",
                "description": "Nutritious cereals made with organic ingredients, offering a healthy start to the day.",
                "price": 145.74,
                "sku": "0UIOBQHR",
                "quantity": 55,
                "date_created": "2023-08-04"
            },
            {
                "category": "Snacks & Sweets",
                "product": "Cookies",
                "description": "A delightful assortment of baked treats, perfect for snacking or sharing.",
                "price": 332.46,
                "sku": "0K9NFNO8",
                "quantity": 52,
                "date_created": "2023-03-08"
            },
            {
                "category": "Beverages",
                "product": "Green Tea",
                "description": "A healthy and refreshing beverage, rich in antioxidants and known for its calming effects.",
                "price": 74.56,
                "sku": "K0ZE0VXF",
                "quantity": 87,
                "date_created": "2023-05-15"
            },
            {
                "category": "Fresh Produce",
                "product": "Bell Peppers",
                "description": "Colorful and nutritious, these vegetables are versatile in cooking and rich in vitamins.",
                "price": 386.6,
                "sku": "7E0O8FUN",
                "quantity": 40,
                "date_created": "2023-10-17"
            }
        ]
    },
    {
        "category": "Office Supplies",
        "name": "Office Essentials Mart",
        "date_created": "2023-09-01",
        "description": "Office Essentials Mart offers a wide range of products related to its category.",
        "opening_time": "9:00 AM",
        "closing_time": "8:00 PM",
        "website": "www.officeessentialsmart.com",
        "phone_number": "883-400-6240",
        "rating": 3.7,
        "distance": 2.8,
        "cost": 2,
        "payment_methods": 5,
        "products": [
            {
                "category": "Office Electronics",
                "product": "External Hard Drives",
                "description": "Store your data securely with External Hard Drives. These high-quality drives offer exceptional performance and durability.",
                "price": 86.86,
                "sku": "5MVI6H7H",
                "quantity": 76,
                "date_created": "2023-10-30"
            },
            {
                "category": "Educational Supplies",
                "product": "STEM Education Kits",
                "description": "Enhance education with STEM Education Kits. They are designed to provide hands-on learning experiences.",
                "price": 433.31,
                "sku": "9XE2K1BN",
                "quantity": 47,
                "date_created": "2023-01-20"
            },
            {
                "category": "Desk Accessories",
                "product": "Desk Lamps",
                "description": "Illuminate your workspace with Desk Lamps. These lamps are designed for both functionality and style.",
                "price": 64.09,
                "sku": "NFL0WU2Q",
                "quantity": 18,
                "date_created": "2023-04-27"
            },
            {
                "category": "Educational Supplies",
                "product": "Art Supplies for Schools",
                "description": "Fuel creativity with Art Supplies for Schools. These supplies are designed for aspiring artists and students.",
                "price": 222.41,
                "sku": "N0Y0ZM4R",
                "quantity": 6,
                "date_created": "2023-08-29"
            },
            {
                "category": "Organizers & Planners",
                "product": "Yearly Planners",
                "description": "Stay organized with Yearly Planners. They are designed to help you plan your year efficiently.",
                "price": 439.89,
                "sku": "1WPTV3B5",
                "quantity": 79,
                "date_created": "2024-01-03"
            },
            {
                "category": "Desk Accessories",
                "product": "Desk Plants",
                "description": "Bring a touch of nature to your desk with Desk Plants. They are designed to enhance your workspace.",
                "price": 204.58,
                "sku": "EPI53XBZ",
                "quantity": 9,
                "date_created": "2023-08-31"
            },
            {
                "category": "Paper Products",
                "product": "Journals",
                "description": "Capture your thoughts and ideas with Journals. These high-quality journals are designed for writing enthusiasts.",
                "price": 282.43,
                "sku": "IQ1O9ZHA",
                "quantity": 38,
                "date_created": "2024-01-10"
            },
            {
                "category": "Office Furniture",
                "product": "Office Desks",
                "description": "Create a productive workspace with Office Desks. They are designed for both comfort and functionality.",
                "price": 473.98,
                "sku": "BYS8Z3CJ",
                "quantity": 83,
                "date_created": "2023-02-07"
            },
            {
                "category": "Mailing & Shipping Supplies",
                "product": "Mailroom Carts",
                "description": "Streamline your mailing and shipping processes with Mailroom Carts. They are designed for efficiency.",
                "price": 110.0,
                "sku": "1598KOV0",
                "quantity": 34,
                "date_created": "2023-06-23"
            },
            {
                "category": "Binders & Folders",
                "product": "Binders",
                "description": "Organize your documents with Binders. These high-quality binders are designed for durability.",
                "price": 272.02,
                "sku": "6NBNEFZF",
                "quantity": 84,
                "date_created": "2023-04-28"
            },
            {
                "category": "Printers & Scanners",
                "product": "Document Scanners",
                "description": "Digitize your documents with Document Scanners. They are designed to provide reliable scanning solutions.",
                "price": 287.94,
                "sku": "7OG6DRKX",
                "quantity": 80,
                "date_created": "2023-05-04"
            },
            {
                "category": "Desk Accessories",
                "product": "Desk Organizers",
                "description": "Keep your desk clutter-free with Desk Organizers. They are designed to help you stay organized.",
                "price": 188.91,
                "sku": "N6X70MT1",
                "quantity": 82,
                "date_created": "2023-09-18"
            },
            {
                "category": "Writing Instruments",
                "product": "Mechanical Pencils",
                "description": "Write with precision using Mechanical Pencils. They are designed for smooth and efficient writing.",
                "price": 423.12,
                "sku": "33ERG80X",
                "quantity": 12,
                "date_created": "2023-12-16"
            },
            {
                "category": "Organizers & Planners",
                "product": "Weekly Planners",
                "description": "Plan your week effectively with Weekly Planners. They are designed to help you stay on top of your tasks.",
                "price": 36.48,
                "sku": "FN01FD6P",
                "quantity": 22,
                "date_created": "2023-05-25"
            },
            {
                "category": "Mailing & Shipping Supplies",
                "product": "Mailing Labels",
                "description": "Label your mail efficiently with Mailing Labels. They are designed for clear and reliable labeling.",
                "price": 54.05,
                "sku": "WPOJMG7N",
                "quantity": 65,
                "date_created": "2023-12-14"
            },
            {
                "category": "Organizers & Planners",
                "product": "Appointment Books",
                "description": "Manage your appointments with Appointment Books. They are designed to keep your schedule organized.",
                "price": 443.71,
                "sku": "D7AD9DZ8",
                "quantity": 4,
                "date_created": "2023-08-25"
            },
            {
                "category": "Printers & Scanners",
                "product": "Wide-Format Printers",
                "description": "Print large documents with Wide-Format Printers. They are designed for high-quality printing.",
                "price": 35.6,
                "sku": "ES79I8RB",
                "quantity": 12,
                "date_created": "2023-06-06"
            },
            {
                "category": "Mailing & Shipping Supplies",
                "product": "Envelopes",
                "description": "Send mail securely with Envelopes. They are designed for reliable mail protection.",
                "price": 377.47,
                "sku": "PMAGAUY6",
                "quantity": 73,
                "date_created": "2023-04-10"
            }
        ]
    },
    {
        "category": "Electronics",
        "name": "Tech Innovations Emporium",
        "date_created": "2019-10-20",
        "description": "Tech Innovations Emporium offers a wide range of products related to its category.",
        "opening_time": "10:00 AM",
        "closing_time": "7:00 PM",
        "website": "www.techinnovationsemporium.com",
        "phone_number": "231-780-3576",
        "rating": 4.3,
        "distance": 1.7,
        "cost": 1,
        "payment_methods": 1,
        "products": [
            {
                "category": "Video Games & Consoles",
                "product": "Sony DualSense Controller",
                "description": "An advanced game controller with immersive haptic feedback and adaptive triggers.",
                "price": 9.74,
                "sku": "STKPEKNM",
                "quantity": 86,
                "date_created": "2023-07-10"
            },
            {
                "category": "Smartphones & Accessories",
                "product": "iPhone 13",
                "description": "The latest model of Apple's iPhone, featuring advanced technology and innovative features.",
                "price": 482.89,
                "sku": "AV6U4GWK",
                "quantity": 33,
                "date_created": "2023-07-26"
            },
            {
                "category": "Wearable Technology",
                "product": "Whoop Strap 4.0",
                "description": "A high-tech wearable device designed to track physical activity, sleep, and overall health.",
                "price": 272.97,
                "sku": "M5PKCP84",
                "quantity": 88,
                "date_created": "2023-11-30"
            },
            {
                "category": "Home Automation & Security",
                "product": "Arlo Pro 4 Security Camera",
                "description": "A high-definition security camera offering wireless connectivity and advanced motion detection features.",
                "price": 324.83,
                "sku": "WQRD4AEG",
                "quantity": 9,
                "date_created": "2023-03-05"
            },
            {
                "category": "Cameras & Photography",
                "product": "Rode VideoMic Pro",
                "description": "A professional-grade microphone designed for high-quality audio recording on cameras.",
                "price": 435.54,
                "sku": "DDRUZ273",
                "quantity": 17,
                "date_created": "2023-03-29"
            },
            {
                "category": "Video Games & Consoles",
                "product": "Nintendo Joy-Con",
                "description": "Transform your gaming experience with the versatile Nintendo Joy-Con, offering innovative ways to play and connect.",
                "price": 46.99,
                "sku": "14YBLBZ1",
                "quantity": 11,
                "date_created": "2023-06-28"
            },
            {
                "category": "Video Games & Consoles",
                "product": "Xbox Game Pass Subscription",
                "description": "Unlock a world of gaming with the Xbox Game Pass Subscription, your gateway to endless entertainment and adventure.",
                "price": 244.72,
                "sku": "YQKMD57B",
                "quantity": 2,
                "date_created": "2023-04-15"
            },
            {
                "category": "Home Automation & Security",
                "product": "Philips Hue Smart Bulbs",
                "description": "Innovative light bulbs that can be controlled remotely for customized lighting settings.",
                "price": 498.25,
                "sku": "K60BS64H",
                "quantity": 77,
                "date_created": "2024-01-03"
            },
            {
                "category": "Wearable Technology",
                "product": "Oculus Quest 2",
                "description": "Step into the future of gaming with Oculus Quest 2, where virtual reality meets limitless possibilities.",
                "price": 349.31,
                "sku": "POVAU87G",
                "quantity": 100,
                "date_created": "2023-03-06"
            },
            {
                "category": "Tablets & E-Readers",
                "product": "Lenovo Tab M10",
                "description": "A versatile and user-friendly tablet, ideal for entertainment, work, and daily use.",
                "price": 185.01,
                "sku": "GWJEV27I",
                "quantity": 15,
                "date_created": "2023-01-31"
            },
            {
                "category": "Home Automation & Security",
                "product": "SimpliSafe Home Security System",
                "description": "A user-friendly home security system for monitoring and protecting your home.",
                "price": 107.1,
                "sku": "JTUHZ0CM",
                "quantity": 24,
                "date_created": "2023-11-30"
            },
            {
                "category": "Home Automation & Security",
                "product": "Wyze Cam Outdoor",
                "description": "Secure your home effortlessly with the Wyze Cam Outdoor, delivering smart surveillance and peace of mind.",
                "price": 315.87,
                "sku": "GDOWTYQ1",
                "quantity": 32,
                "date_created": "2023-05-03"
            },
            {
                "category": "Wearable Technology",
                "product": "Withings Body+ Smart Scale",
                "description": "Track your health journey with precision using the Withings Body+ Smart Scale, your partner in fitness and well-being.",
                "price": 346.08,
                "sku": "ER7SH24R",
                "quantity": 11,
                "date_created": "2023-12-08"
            },
            {
                "category": "Computers & Laptops",
                "product": "Microsoft Surface Pro",
                "description": "A high-performance tablet with laptop capabilities, suitable for work and creativity.",
                "price": 252.03,
                "sku": "1UYP901V",
                "quantity": 61,
                "date_created": "2023-06-14"
            },
            {
                "category": "Networking & Wireless",
                "product": "Orbi Mesh WiFi System",
                "description": "A state-of-the-art WiFi system that ensures seamless and robust internet connectivity throughout your home.",
                "price": 417.29,
                "sku": "4AZ3EWTO",
                "quantity": 100,
                "date_created": "2023-12-15"
            },
            {
                "category": "Home Automation & Security",
                "product": "Nest Learning Thermostat",
                "description": "An intelligent thermostat that learns and adapts to your heating and cooling preferences.",
                "price": 401.79,
                "sku": "IERFY99J",
                "quantity": 67,
                "date_created": "2023-08-27"
            },
            {
                "category": "Audio & Hi-Fi",
                "product": "Bose QuietComfort 35 II",
                "description": "Advanced noise-canceling headphones providing superior sound quality and comfort.",
                "price": 412.19,
                "sku": "5J9X6ZFO",
                "quantity": 60,
                "date_created": "2023-12-16"
            }
        ]
    },
    {
        "category": "Electronics",
        "name": "Electronics & Gadgets Zone",
        "date_created": "2019-12-08",
        "description": "Electronics & Gadgets Zone offers a wide range of products related to its category.",
        "opening_time": "9:00 AM",
        "closing_time": "7:00 PM",
        "website": "www.electronics&gadgetszone.com",
        "phone_number": "347-103-7918",
        "rating": 3.7,
        "distance": 2.0,
        "cost": 1,
        "payment_methods": 5,
        "products": [
            {
                "category": "Audio & Hi-Fi",
                "product": "FiiO Hi-Res Player",
                "description": "Experience high-quality audio with the FiiO Hi-Res Player. Designed for exceptional performance and durability, it's perfect for audiophiles.",
                "price": 290.01,
                "sku": "JDWZ2IX7",
                "quantity": 21,
                "date_created": "2023-11-19"
            },
            {
                "category": "Video Games & Consoles",
                "product": "Xbox Game Pass Subscription",
                "description": "Get access to a vast library of games with the Xbox Game Pass Subscription. It's designed to offer reliable and efficient gaming experiences.",
                "price": 344.33,
                "sku": "D1W2W1H0",
                "quantity": 70,
                "date_created": "2023-04-08"
            },
            {
                "category": "Smartphones & Accessories",
                "product": "Spigen Phone Case",
                "description": "Protect your smartphone with the Spigen Phone Case. It's a high-quality product designed for both reliability and style.",
                "price": 220.46,
                "sku": "Q3IXMML6",
                "quantity": 54,
                "date_created": "2023-05-24"
            },
            {
                "category": "Video Games & Consoles",
                "product": "Nintendo Switch",
                "description": "Enjoy gaming on the go with the Nintendo Switch. This console is designed to provide exceptional gaming experiences.",
                "price": 145.91,
                "sku": "IBQV4VYC",
                "quantity": 21,
                "date_created": "2023-06-09"
            },
            {
                "category": "Video Games & Consoles",
                "product": "Gaming Headset",
                "description": "Immerse yourself in gaming with the Gaming Headset. It's designed for exceptional audio quality and comfort during extended gaming sessions.",
                "price": 378.51,
                "sku": "NXDVO93O",
                "quantity": 79,
                "date_created": "2023-06-29"
            },
            {
                "category": "Wearable Technology",
                "product": "Suunto 7 Smartwatch",
                "description": "Stay connected and active with the Suunto 7 Smartwatch. It offers a range of features and is built for durability.",
                "price": 315.12,
                "sku": "KSO4B79V",
                "quantity": 14,
                "date_created": "2023-07-05"
            },
            {
                "category": "Smartphones & Accessories",
                "product": "Screen Protector",
                "description": "Protect your smartphone screen with the Screen Protector. It's designed to offer reliable protection without compromising touch sensitivity.",
                "price": 367.0,
                "sku": "M6I807K9",
                "quantity": 18,
                "date_created": "2023-12-24"
            },
            {
                "category": "Computers & Laptops",
                "product": "HP Envy x360",
                "description": "Experience powerful computing with the HP Envy x360 laptop. It's designed to provide reliability and efficiency for various tasks.",
                "price": 255.51,
                "sku": "OXMKTIZ2",
                "quantity": 20,
                "date_created": "2023-01-22"
            },
            {
                "category": "Smartphones & Accessories",
                "product": "OnePlus 9",
                "description": "Upgrade your smartphone with the OnePlus 9. It's designed to offer a premium smartphone experience.",
                "price": 70.47,
                "sku": "H5B9XTUN",
                "quantity": 76,
                "date_created": "2023-12-24"
            },
            {
                "category": "Wearable Technology",
                "product": "Withings Body+ Smart Scale",
                "description": "Monitor your health with the Withings Body+ Smart Scale. It's designed to provide accurate measurements and sync with your devices.",
                "price": 303.56,
                "sku": "CZV3LUOE",
                "quantity": 49,
                "date_created": "2023-06-05"
            },
            {
                "category": "Networking & Wireless",
                "product": "TP-Link Archer C4000 Router",
                "description": "Enhance your home network with the TP-Link Archer C4000 Router. It's designed for reliability and high-performance networking.",
                "price": 439.51,
                "sku": "ZIETS7UA",
                "quantity": 17,
                "date_created": "2023-08-09"
            },
            {
                "category": "Wearable Technology",
                "product": "Oculus Quest 2",
                "description": "Experience virtual reality with the Oculus Quest 2. It offers immersive VR experiences and is designed for durability.",
                "price": 218.96,
                "sku": "7ZYKEW7Z",
                "quantity": 14,
                "date_created": "2023-02-25"
            },
            {
                "category": "Home Automation & Security",
                "product": "Wyze Cam Outdoor",
                "description": "Enhance your home security with the Wyze Cam Outdoor. It's a reliable and efficient outdoor security camera.",
                "price": 127.77,
                "sku": "1W0357P6",
                "quantity": 39,
                "date_created": "2023-10-25"
            },
            {
                "category": "Cameras & Photography",
                "product": "Canon EOS 5D Mark IV",
                "description": "Capture stunning photos with the Canon EOS 5D Mark IV camera. It's designed for professional photographers.",
                "price": 195.14,
                "sku": "I7GNE91V",
                "quantity": 13,
                "date_created": "2023-01-21"
            },
            {
                "category": "Smartphones & Accessories",
                "product": "Apple AirPods Pro",
                "description": "Enjoy premium audio with the Apple AirPods Pro. They're designed for exceptional sound quality and comfort.",
                "price": 452.28,
                "sku": "R6D810IC",
                "quantity": 26,
                "date_created": "2023-12-20"
            },
            {
                "category": "Televisions & Home Theater",
                "product": "Universal Remote Control",
                "description": "Simplify your home entertainment with the Universal Remote Control. It's designed for efficiency and ease of use.",
                "price": 216.11,
                "sku": "AROHRUX5",
                "quantity": 51,
                "date_created": "2023-06-02"
            },
            {
                "category": "Computers & Laptops",
                "product": "Asus ROG Gaming Laptop",
                "description": "Take gaming to the next level with the Asus ROG Gaming Laptop. It's designed for high-performance gaming experiences.",
                "price": 150.41,
                "sku": "K7H6QO0C",
                "quantity": 99,
                "date_created": "2023-12-23"
            },
            {
                "category": "Smartphones & Accessories",
                "product": "Bluetooth Selfie Stick",
                "description": "Capture memorable moments with the Bluetooth Selfie Stick. It's designed for ease of use and reliability.",
                "price": 386.25,
                "sku": "R2E8QIT7",
                "quantity": 49,
                "date_created": "2023-04-05"
            },
            {
                "category": "Video Games & Consoles",
                "product": "Nintendo Joy-Con",
                "description": "Enhance your Nintendo gaming experience with Nintendo Joy-Con controllers. They're designed for responsive and efficient gameplay.",
                "price": 5.69,
                "sku": "5GGIAFGH",
                "quantity": 88,
                "date_created": "2023-07-05"
            }
        ]
    },
    {
        "category": "Pet Supplies",
        "name": "Pet Care & Supplies Warehouse",
        "date_created": "2022-09-23",
        "description": "Pet Care & Supplies Warehouse offers a wide range of products related to its category.",
        "opening_time": "10:00 AM",
        "closing_time": "7:00 PM",
        "website": "www.petcare&supplieswarehouse.com",
        "phone_number": "762-533-2229",
        "rating": 4.8,
        "distance": 1.3,
        "cost": 2,
        "payment_methods": 5,
        "products": [
            {
                "category": "Horse Supplies",
                "product": "Horse Stall Supplies",
                "description": "Keep your horses comfortable with our horse stall supplies. These high-quality products are designed with attention to detail for exceptional performance and durability.",
                "price": 174.7,
                "sku": "4WV9K6JV",
                "quantity": 43,
                "date_created": "2023-10-02"
            },
            {
                "category": "Small Animal Supplies",
                "product": "Small Animal Food",
                "description": "Ensure your small animals get the nutrition they need with our small animal food. Our products are of the highest quality, providing the best for your pets.",
                "price": 368.44,
                "sku": "YZ3SR74U",
                "quantity": 9,
                "date_created": "2023-09-03"
            },
            {
                "category": "Pet Health & Wellness",
                "product": "Pet First Aid Kits",
                "description": "Be prepared for emergencies with our pet first aid kits. Designed with reliability and efficiency in mind, our kits are a must-have for pet owners.",
                "price": 241.73,
                "sku": "QL8P3HM2",
                "quantity": 78,
                "date_created": "2023-08-04"
            },
            {
                "category": "Dog Supplies",
                "product": "Dog Health and Wellness Products",
                "description": "Maintain your dog's health and wellness with our range of products. We offer top-quality items designed to enhance your dog's life.",
                "price": 486.11,
                "sku": "IEB32WYL",
                "quantity": 90,
                "date_created": "2023-05-18"
            },
            {
                "category": "Bird Supplies",
                "product": "Bird Feeders",
                "description": "Attract beautiful birds to your space with our bird feeders. Our products are designed for durability and efficiency, ensuring a delightful bird-watching experience.",
                "price": 173.08,
                "sku": "F6BKZRXD",
                "quantity": 21,
                "date_created": "2023-12-31"
            },
            {
                "category": "Cat Supplies",
                "product": "Cat Toys",
                "description": "Keep your feline friends entertained with our cat toys. These toys are designed to provide hours of fun and excitement for your cats.",
                "price": 134.36,
                "sku": "49IJJSEU",
                "quantity": 34,
                "date_created": "2023-08-28"
            },
            {
                "category": "Pet Grooming",
                "product": "Pet Bathing Tools",
                "description": "Make pet grooming a breeze with our pet bathing tools. Our high-quality tools are designed for efficiency and ease of use.",
                "price": 25.45,
                "sku": "Z4VJDO07",
                "quantity": 53,
                "date_created": "2023-03-27"
            },
            {
                "category": "Pet Health & Wellness",
                "product": "Pet Vitamins and Supplements",
                "description": "Support your pet's health with our vitamins and supplements. We offer top-quality products to meet the specific needs of your pets.",
                "price": 390.73,
                "sku": "E2C640J9",
                "quantity": 86,
                "date_created": "2023-04-22"
            },
            {
                "category": "Bird Supplies",
                "product": "Bird Food",
                "description": "Provide the best nutrition for your feathered friends with our bird food. Our products are carefully selected for their quality and appeal to a variety of bird species.",
                "price": 162.39,
                "sku": "2C1SJ0BH",
                "quantity": 10,
                "date_created": "2023-11-20"
            },
            {
                "category": "Fish & Aquarium",
                "product": "Fish Tank Cleaning Supplies",
                "description": "Maintain a clean and healthy aquarium with our fish tank cleaning supplies. Our products are designed for aquarium enthusiasts who demand reliability.",
                "price": 477.59,
                "sku": "UYNQ4RVP",
                "quantity": 32,
                "date_created": "2023-12-05"
            },
            {
                "category": "Pet Food & Treats",
                "product": "Wet Dog Food",
                "description": "Treat your dogs to our wet dog food. Our products are made with care to provide a delicious and nutritious meal for your canine companions.",
                "price": 153.83,
                "sku": "FGEBE7LF",
                "quantity": 82,
                "date_created": "2023-06-07"
            },
            {
                "category": "Pet Food & Treats",
                "product": "Raw Pet Food",
                "description": "Explore the benefits of raw pet food with our selection. We offer high-quality raw pet food to support your pet's overall well-being.",
                "price": 429.07,
                "sku": "0IHR7QGG",
                "quantity": 26,
                "date_created": "2023-02-27"
            },
            {
                "category": "Dog Supplies",
                "product": "Dog Beds",
                "description": "Ensure your dogs have a comfortable place to rest with our dog beds. Our products are designed for both style and comfort.",
                "price": 6.89,
                "sku": "WAUZLDTZ",
                "quantity": 100,
                "date_created": "2023-07-30"
            },
            {
                "category": "Pet Grooming",
                "product": "Pet Ear and Eye Cleaners",
                "description": "Maintain your pet's hygiene with our ear and eye cleaners. Our products are designed to be gentle and effective.",
                "price": 52.1,
                "sku": "Z7229ZCW",
                "quantity": 74,
                "date_created": "2023-07-02"
            },
            {
                "category": "Pet Grooming",
                "product": "Pet Dental Care Products",
                "description": "Take care of your pet's dental health with our dental care products. We prioritize efficiency and effectiveness in our offerings.",
                "price": 34.35,
                "sku": "JL0R07SZ",
                "quantity": 4,
                "date_created": "2023-01-18"
            },
            {
                "category": "Pet Health & Wellness",
                "product": "Pet Antibiotics",
                "description": "Address your pet's health needs with our pet antibiotics. We provide reliable and high-quality antibiotics to support your pet's recovery.",
                "price": 203.82,
                "sku": "D4V3F9DF",
                "quantity": 89,
                "date_created": "2023-01-31"
            },
            {
                "category": "Fish & Aquarium",
                "product": "Live Aquarium Plants",
                "description": "Enhance your aquarium's beauty and health with our live aquarium plants. We offer a selection that caters to aquarists looking for quality.",
                "price": 135.84,
                "sku": "LWCQVSM9",
                "quantity": 2,
                "date_created": "2023-08-23"
            },
            {
                "category": "Pet Grooming",
                "product": "Pet Grooming Gloves",
                "description": "Simplify pet grooming with our pet grooming gloves. These gloves are designed to be efficient and comfortable for both you and your pet.",
                "price": 83.97,
                "sku": "D587NHKL",
                "quantity": 11,
                "date_created": "2023-02-18"
            }
        ]
    }
]

new_descriptions = {
"Bad Blood: Secrets and Lies in a Silicon Valley Startup by John Carreyrou": "Uncover the gripping truth behind a Silicon Valley scandal with 'Bad Blood,' a captivating read about ambition, deception, and the collapse of Theranos.",
    "Antique Coins": "Step back in time with our collection of Antique Coins, perfect for collectors and history enthusiasts alike, each piece telling its own unique story.",
    "Blanket Scarves": "Wrap yourself in warmth and style with our Blanket Scarves, a cozy and chic accessory perfect for chilly days and fashionable nights.",
    "Tribal Jewelry": "Adorn yourself with the spirit of heritage with our Tribal Jewelry, blending traditional craftsmanship with contemporary fashion.",
    "Pet Bathing Tools": "Make pet grooming a breeze with our range of Pet Bathing Tools, designed for a comfortable and efficient cleaning experience for your furry friends.",
    "Horse Stall Supplies": "Ensure your equine's comfort with our premium Horse Stall Supplies, catering to all your horse care needs with top-quality products.",
    "Bird Feeders": "Bring nature closer to home with our charming Bird Feeders, perfect for attracting a variety of birds and adding beauty to your garden.",
    "Fish Tank Cleaning Supplies": "Keep your aquatic environment pristine with our Fish Tank Cleaning Supplies, essential for maintaining a healthy and clear habitat for your fish.",
    "Pet Ear and Eye Cleaners": "Gentle and effective, our Pet Ear and Eye Cleaners are specially formulated to keep your pets' sensitive areas clean and healthy.",
    "Dog Beds": "Spoil your dog with the ultimate comfort of our plush Dog Beds, ensuring your pet a cozy spot to rest and relax.",
    "Cat Toys": "Entertain and stimulate your feline friend with our exciting range of Cat Toys, designed for endless fun and activity.",
    "Cycling Jerseys": "Hit the road in style and comfort with our high-performance Cycling Jerseys, tailored for maximum mobility and breathability.",
    "Snow Sled": "Embrace the winter thrill with our Snow Sled, an exciting way to enjoy the snowy slopes and make lasting memories.",
    "Fishing Rod and Reel Combo": "Experience the perfect cast with our Fishing Rod and Reel Combo, designed for anglers seeking reliability and precision.",
    "Baby Proofing Kits": "Protect your little explorer with our comprehensive Baby Proofing Kits, ensuring a safe and secure environment for your child.",
    "Convertible Car Seats": "Travel with peace of mind with our Convertible Car Seats, combining safety, comfort, and versatility for your growing child.",
    "Dress Watches": "Elevate your style with our exquisite Dress Watches, the perfect blend of elegance and sophistication for any formal occasion.",
    "Heart Necklaces": "Express your love and affection with our elegant Heart Necklaces, a timeless symbol of romance and devotion.",
    "Organic Fruits": "Savor the taste of health with our Organic Fruits, naturally grown for the best in flavor and nutritional goodness.",
    "Nintendo Joy-Con": "Transform your gaming experience with the versatile Nintendo Joy-Con, offering innovative ways to play and connect.",
    "Xbox Game Pass Subscription": "Unlock a world of gaming with the Xbox Game Pass Subscription, your gateway to endless entertainment and adventure.",
    "Oculus Quest 2": "Step into the future of gaming with Oculus Quest 2, where virtual reality meets limitless possibilities.",
    "Wyze Cam Outdoor": "Secure your home effortlessly with the Wyze Cam Outdoor, delivering smart surveillance and peace of mind.",
    "Withings Body+ Smart Scale": "Track your health journey with precision using the Withings Body+ Smart Scale, your partner in fitness and well-being."

}

new_descriptions_websites = {
    'Sporty Outdoor Essentials': {
        'description': 'Your ultimate destination for outdoor and sports gear. From camping equipment to athletic apparel, we have everything for the outdoor enthusiast.',
        'website': 'www.sportyoutdoressentials.com'
    },
    'Glamour Jewelry Haven': {
        'description': 'A dazzling world of jewelry and accessories. Explore our collection of elegant and contemporary pieces for every occasion.',
        'website': 'www.glamourjewelryhaven.com'
    },
    'Wellness & Health Hub': {
        'description': 'Dedicated to your health and wellness. Find a wide range of fitness gear, nutritional supplements, and wellness products.',
        'website': 'www.wellnesshealthhub.com'
    },
    'Tiny Tots Baby Store': {
        'description': 'Everything for your baby in one place. From baby clothes and toys to nursery furniture and feeding supplies.',
        'website': 'www.tinytotsbabystore.com'
    },
    "Readers' Retreat Bookstore": {
        'description': 'A paradise for book lovers. Browse our vast collection of books across all genres, along with a selection of stationery and reading accessories.',
        'website': 'www.readersretreatbookstore.com'
    },
    'Artistic Treasures Gallery': {
        'description': 'An exquisite collection of art and collectibles. Find unique pieces to adorn your home and office spaces.',
        'website': 'www.artistictreasuresgallery.com'
    },
    "Travelers' Luggage Loft": {
        'description': 'The one-stop shop for all your travel needs. Offering a range of luggage options, travel accessories, and gear for your adventures.',
        'website': 'www.travelersluggageloft.com'
    },
    'Beauty & Care Boutique': {
        'description': 'Indulge in beauty and personal care. From skincare products to beauty tools, everything you need to look and feel your best.',
        'website': 'www.beautycareboutique.com'
    },
    'Elegant Accessories Emporium': {
        'description': 'Accessorize in style. Discover our selection of fashionable accessories to complement your every look.',
        'website': 'www.elegantaccessoriesemporium.com'
    },
    'Pet Paradise Store': {
        'description': 'All things pets under one roof. Quality food, toys, and supplies for your furry, feathered, or scaled friends.',
        'website': 'www.petparadisestore.com'
    },
    'Active Sports Gear': {
        'description': 'Gear up for every game. Shop our wide range of sports equipment, fitness wear, and athletic accessories.',
        'website': 'www.activesportsgear.com'
    },
    'Baby Joy Boutique': {
        'description': 'Celebrate the joy of parenting. Find premium baby clothing, toys, and nursery essentials for your little bundle of joy.',
        'website': 'www.babyjoyboutique.com'
    },
    "Collector's Art & Craft": {
        'description': 'A realm of creativity and artistry. Explore our diverse collection of art supplies, crafts, and unique artistic pieces.',
        'website': 'www.collectorsartcraft.com'
    },
    'Luxury Jewelry Corner': {
        'description': 'Exquisite jewelry for every occasion. Our selection of luxury pieces will add elegance and charm to your ensemble.',
        'website': 'www.luxuryjewelrycorner.com'
    },
    'Cozy Home Decor Studio': {
        'description': 'Transform your home into a cozy haven. Browse our selection of home decor, furniture, and lifestyle products.',
        'website': 'www.cozyhomedecorstudio.com'
    },
    'Gourmet Delights Grocery': {
        'description': 'A gourmet\'s dream destination. Indulge in our selection of fine foods, organic produce, and gourmet specialties.',
        'website': 'www.gourmetdelightsgrocery.com'
    },
    'Office Essentials Mart': {
        'description': 'Everything for your office needs. From stationery to technology, we cater to all your professional requirements.',
        'website': 'www.officeessentialsmart.com'
    },
    'Tech Innovations Emporium': {
        'description': 'The future of technology at your fingertips. Shop the latest in electronics, gadgets, and tech innovations.',
        'website': 'www.techinnovationsemporium.com'
    },
    'Electronics & Gadgets Zone': {
        'description': 'Your go-to place for all electronic needs. From the latest gadgets to essential electronics, we have it all.',
        'website': 'www.electronicsgadgetszone.com'
    },

    "Pet Care & Supplies Warehouse": {
        "description": "Comprehensive care for your pets. We offer a wide range of pet supplies, health products, and accessories for your beloved animals.",
        "website": "www.petcareandsupplieswarehouse.com"
    }
}


# Define the prefix to search for
prefix = "Details about"

# Initialize a list to store product names with descriptions starting with the prefix
products_with_prefix = []

# Iterate through the data and find products with descriptions starting with the prefix
for store in data:

    # store["description"] = new_descriptions_websites[store["name"]]["description"]
    # store["website"] = new_descriptions_websites[store["name"]]["website"]

    for i, product in enumerate(store["products"]):
        new_dict = {"name": product["product"]}
        del product["product"]
        new_dict.update(product)
        store["products"][i] = new_dict

        # if product["description"].startswith(prefix):
        #     product["description"] = new_descriptions[product["product"]]


print(data)


