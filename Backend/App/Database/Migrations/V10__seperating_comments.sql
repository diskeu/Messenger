-- Updating the Comments Table to be independent and not just pointers to posts

ALTER TABLE messenger.comments
-- Droping CHECKs
DROP CHECK comments_chk_1,
-- Droping old Columns ForeignKeys and PrimaryKey
DROP COLUMN parent_post,
DROP PRIMARY KEY,
DROP FOREIGN KEY comments_ibfk_1,
DROP FOREIGN KEY comments_ibfk_2,
-- Modifying existing Table
MODIFY COLUMN comment_id INT NOT NULL AUTO_INCREMENT,
-- Adding new Columns
ADD COLUMN comment_creator_id INT NOT NULL,          -- Author of the comment         
ADD COLUMN post_id INT NOT NULL,                     -- Id of the orignal commented Post (Easier listing of all comments of one post)
ADD COLUMN parent_comment_id INT NULL DEFAULT NULL,  -- Id of the parent comment -> Null if the parent is the post 
-- Adding content related stuff
ADD COLUMN comment_content VARCHAR(255) NOT NULL,
ADD COLUMN created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
-- Adding primary key
ADD CONSTRAINT pk_comment_id
    PRIMARY KEY (comment_id),
-- Adding foreign keys
ADD CONSTRAINT fk_comment_creator_id
    FOREIGN KEY (comment_creator_id)
    REFERENCES messenger.users(user_id)
        ON DELETE CASCADE, 
ADD CONSTRAINT fk_post_id
    FOREIGN KEY (post_id)
    REFERENCES messenger.posts(post_id)
        ON DELETE CASCADE,
ADD CONSTRAINT fk_parent_comment_id
    FOREIGN KEY (parent_comment_id)
    REFERENCES messenger.comments(comment_id)
        ON DELETE CASCADE
;
-- Creating Indexes
CREATE INDEX comment_creator_idx                -- Listing of all comments of an User
    ON messenger.comments (comment_creator_id);
CREATE INDEX parent_comment_idx                 -- Efficent listing of all comments of a comment
    ON messenger.comments (parent_comment_id);
CREATE INDEX post_idx                           -- Listing of all comments of an User
    ON messenger.comments (post_id);

