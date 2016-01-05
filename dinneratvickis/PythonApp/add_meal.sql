USE dinneratvickis;
DROP procedure IF EXISTS dinneratvickis.add_meal;

DELIMITER //
USE dinneratvickis//
CREATE DEFINER=root@localhost PROCEDURE add_meal(
	IN guests varchar(100),
	IN donation int(3))
BEGIN
	INSERT INTO meals (
		guests,
		donation)
	VALUES (
		guests,
		donation,
		NOW());
END//
DELIMITER ;
;