-- Users Table
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT,
    user_name VARCHAR(12) NOT NULL,
    hashed_password VARCHAR(64) NOT NULL,
    email VARCHAR(64) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_seen TIMESTAMP NULL DEFAULT NULL,
    birth_date DATE NOT NULL,
    PRIMARY KEY (user_id),
    UNIQUE (user_name),
    UNIQUE (email)
) AUTO_INCREMENT = 1000
;