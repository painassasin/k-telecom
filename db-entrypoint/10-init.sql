USE WebApp;
CREATE TABLE equipment_types
(
    code INT AUTO_INCREMENT,
    type_name VARCHAR(100) NOT NULL UNIQUE,
    sn_mask VARCHAR(50) NOT NULL,
    PRIMARY KEY(code)
);
INSERT INTO equipment_types(type_name, sn_mask) VALUES('TP-Link TL-WR74', 'XXAAAAAXAA');
INSERT INTO equipment_types(type_name, sn_mask) VALUES('D-Link DIR-300', 'NXXAAXZXaa');
INSERT INTO equipment_types(type_name, sn_mask) VALUES('D-Link DIR-300 S', 'NXXAAXZXXX');
COMMIT;
