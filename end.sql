-- Create the plants table
CREATE TABLE plants (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    medicinal_use TEXT,
    culinary_use TEXT
);

-- Create the plant_images table to store multiple images for each plant
CREATE TABLE plant_images (
    id INT PRIMARY KEY AUTO_INCREMENT,
    plant_id INT,
    image_path VARCHAR(255),
    FOREIGN KEY (plant_id) REFERENCES plants(id)
);

-- Insert plant data
INSERT INTO plants (name, description, medicinal_use, culinary_use)
VALUES 
('Aloe Vera', 'A succulent plant species', 'Used for skin treatment', 'Smoothies, skin care products');


-- Insert image paths for Aloe Vera
INSERT INTO plant_images (plant_id, image_path)
VALUES 
(1, 'plantdata/alovera/a1(1).png'),
(1, 'plantdata/alovera/a1(2).png'),
(1, 'plantdata/alovera/a1(3).png');
