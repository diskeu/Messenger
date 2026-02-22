-- Updating some default values to be NOT NULL

-- Updating posts Table
ALTER TABLE messenger.posts
MODIFY COLUMN is_sticky BOOLEAN NOT NULL DEFAULT FALSE,
MODIFY COLUMN created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
;

-- Updating users Table
ALTER TABLE messenger.users
MODIFY COLUMN created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
;

-- Updating community Table
ALTER TABLE messenger.community
MODIFY COLUMN created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
;
