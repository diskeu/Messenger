-- Images Table
CREATE TABLE IF NOT EXISTS images (
    image_id INT AUTO_INCREMENT,
    image_path VARCHAR(255) NOT NULL,
    post_id INT NOT NULL,
    PRIMARY KEY (image_id),
    FOREIGN KEY (post_id) REFERENCES posts(post_id)
        ON DELETE CASCADE
)
;