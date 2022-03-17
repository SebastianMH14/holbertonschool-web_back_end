-- SQL script that creates a stored procedure AddBonus
-- that adds a new correction for a student
DELIMITER $$ CREATE PROCEDURE AddBonus(
  IN user_id INT,
  project_name varchar(255),
  score INT
) BEGIN
UPDATE
  corrections
SET
  NEW.user_id = user_id,
  NEW.score = score
END;
$$
