-- script that creates a trigger that resets the attribute
-- valid_email only when the email has been changed
CREATE TRIGGER reset_valid_email
AFTER
INSERT
  ON users
UPDATE
  valid_email
SET
  valid_email = valid_email - 1
WHERE
  email = NEW.email;
