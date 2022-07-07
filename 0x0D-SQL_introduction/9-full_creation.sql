-- creates second table in hbtn_0c_0
-- add multiple rows and if second_table exists should not fail
CREATE TABLE IF NOT EXISTS second_table(
  id INT,
  name VARCHAR(256),
  score INT
);

-- Insert values
INSERT INTO second_table (
  id,
  name,
  score
)
VALUES
(
  1,"John", 10
),
(
  2,"Alex",3
),
(
  3,"Bob",14
),
(
  4,"George",8
);
