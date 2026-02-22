-- Posts Table
CREATE TABLE IF NOT EXISTS posts (
    post_id INT AUTO_INCREMENT,
    post_creator INT NOT NULL,
    community_id INT NULL DEFAULT NULL, -- Null = posted in no community
    post_title VARCHAR(255) NULL DEFAULT NULL,
    post_content VARCHAR(512) NOT NULL,
    post_score INT NOT NULL DEFAULT 0,
    is_sticky BOOLEAN DEFAULT FALSE, -- pinned posts
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (post_id),
    FOREIGN KEY (post_creator) REFERENCES users(user_id)
        ON DELETE CASCADE,
    FOREIGN KEY (community_id) REFERENCES community(community_id)
        ON DELETE CASCADE -- post will get removed if community get's deleted
)
;