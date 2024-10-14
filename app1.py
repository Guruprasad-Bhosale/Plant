import os
import pymysql

# MySQL connection using pymysql
db = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="plantpedia"
)
cursor = db.cursor()

# Path to the plant data folder
plant_data_path = "plantdata/"

# Loop through each plant folder
for plant_folder in os.listdir(plant_data_path):
    plant_name = plant_folder.capitalize()

    # Insert the plant info (you can retrieve description/uses from your CSV)
    cursor.execute(f"INSERT INTO plants (name, description, medicinal_use, culinary_use) VALUES ('{plant_name}', 'Description here', 'Medicinal use here', 'Culinary use here')")
    plant_id = cursor.lastrowid

    # Insert all images for the plant
    image_folder = os.path.join(plant_data_path, plant_folder)
    for image_file in os.listdir(image_folder):
        image_path = f"plantdata/{plant_folder}/{image_file}"
        cursor.execute(f"INSERT INTO plant_images (plant_id, image_path) VALUES ({plant_id}, '{image_path}')")

# Commit changes and close connection
db.commit()
cursor.close()
db.close()
