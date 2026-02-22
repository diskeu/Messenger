-- Update the member-since column in members table to not null

ALTER TABLE messenger.community_members
MODIFY COLUMN member_since TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP;
