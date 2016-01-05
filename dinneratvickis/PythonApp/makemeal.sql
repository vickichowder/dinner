CREATE TABLE meals 
(
	meal_id int(3) NOT NULL AUTO_INCREMENT PRIMARY KEY,
	donation int(3) NOT NULL,
	guests varchar(100) NOT NULL,
	meal_date datetime
); 