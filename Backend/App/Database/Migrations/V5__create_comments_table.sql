
-- Comments Table
-- Comments are refrences to posts in an isolated Table
CREATE TABLE IF NOT EXISTS comments (
    comment_id INT NOT NULL,
    parent_post INT NOT NULL,
    PRIMARY KEY (comment_id),
    FOREIGN KEY (parent_post) REFERENCES posts(post_id)
        ON DELETE CASCADE, -- comment will be removed if parent does
    FOREIGN KEY (comment_id) REFERENCES posts(post_id)
        ON DELETE CASCADE, -- comment will get removed if post does
    CHECK (comment_id <> parent_post)
)
;