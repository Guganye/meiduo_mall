use meiduo_mall;
drop procedure if exists import_data_tb_brand;
CREATE PROCEDURE import_data_tb_brand()
BEGIN
    DECLARE num INT;
    SELECT COUNT(1) INTO num FROM tb_brand;

    IF num = 0 THEN
        INSERT INTO tb_brand (id, create_time, update_time, name, logo, first_letter) VALUES
        (1, NOW(), NOW(), '苹果', 'logos/A.webp', 'A'),
        (2, NOW(), NOW(), '华为', 'logos/H.webp', 'H'),
        (3, NOW(), NOW(), '小米', 'logos/X.webp', 'X'),
        (4, NOW(), NOW(), '大疆', 'logos/D.webp', 'D'),
        (5, NOW(), NOW(), '索尼', 'logos/S.webp', 'S'),
        (6, NOW(), NOW(), '佳能', 'logos/J.webp', 'J');

        SELECT '数据导入成功！' AS result;
    ELSE
        SELECT '表中已有数据，跳过导入。' AS result;
    END IF;
ENd;
call import_data_tb_brand();

