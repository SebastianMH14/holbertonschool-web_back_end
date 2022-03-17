-- script that creates a trigger that decreases the quantity of an item after adding a new order
CREATE TRIGGER deduct_item BEFORE
INSERT
  ON orders
UPDATE
  items
SET
  quantity = quantity - NEW.number
WHERE
  name = NEW.item_name;
