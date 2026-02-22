
-- Votes Table
CREATE TABLE IF NOT EXISTS votes (
    user_id INT NOT NULL,
    post_id INT NOT NULL,
    vote TINYINT NOT NULL, -- -1 Downvote, 1 upvote
    PRIMARY KEY (user_id, post_id), -- One vote per user
    FOREIGN KEY (user_id) REFERENCES users(user_id)
        ON DELETE CASCADE,
    FOREIGN KEY (post_id) REFERENCES posts(post_id)
        ON DELETE CASCADE
)
;