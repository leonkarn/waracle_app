CREATE TABLE cakes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    comment VARCHAR(200) NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    yum_factor INTEGER NOT NULL CHECK (yum_factor >= 1 AND yum_factor <= 5)
);


INSERT INTO cakes (name, comment, image_url, yum_factor) VALUES
('Chocolate Cake', 'Rich and moist chocolate layer cake', 'http://example.com/chocolate.jpg', 5);

INSERT INTO cakes (name, comment, image_url, yum_factor) VALUES
('Vanilla Sponge Cake', 'Light and fluffy vanilla sponge', 'http://example.com/vanilla.jpg', 4);
