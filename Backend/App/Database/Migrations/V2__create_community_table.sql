-- Communitys Table
CREATE TABLE IF NOT EXISTS community (
    community_id INT AUTO_INCREMENT,
    community_description VARCHAR (255) NULL DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    community_owner INT NULL, -- Null if community owner get's deleted
    PRIMARY KEY (community_id),
    FOREIGN KEY (community_owner) REFERENCES users(user_id)
        ON DELETE SET NULL -- community won't get removed if user gets deleted
)
;