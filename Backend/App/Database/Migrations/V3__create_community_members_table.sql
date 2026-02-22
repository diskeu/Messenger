-- Community Members
CREATE TABLE IF NOT EXISTS community_members (
    community_id INT NOT NULL,
    user_id INT NOT NULL,
    role ENUM ("member", "moderator") NOT NULL DEFAULT "member",
    member_since TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (community_id, user_id),
    FOREIGN KEY (community_id) REFERENCES community(community_id)
        ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
        ON DELETE CASCADE
)
;