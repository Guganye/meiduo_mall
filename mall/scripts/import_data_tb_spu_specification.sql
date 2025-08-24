use meiduo_mall;
drop procedure if exists import_data_tb_spu_specification;
CREATE PROCEDURE import_data_tb_spu_specification()
BEGIN
    DECLARE num INT;
    SELECT COUNT(1) INTO num FROM tb_spu_specification;

    IF num = 0 THEN
        -- iPhone 15 Pro 规格
        INSERT INTO tb_spu_specification (id, create_time, update_time, spu_id, name) VALUES
        (1, NOW(), NOW(), 1, '颜色'),
        (2, NOW(), NOW(), 1, '存储容量'),

        -- 华为Mate 60 Pro 规格
        (3, NOW(), NOW(), 2, '颜色'),
        (4, NOW(), NOW(), 2, '存储容量'),

        -- 小米14 Pro 规格
        (5, NOW(), NOW(), 3, '颜色'),
        (6, NOW(), NOW(), 3, '存储容量'),

        -- 大疆Pocket 3 规格
        (7, NOW(), NOW(), 4, '版本'),

        -- 索尼A7M4 规格
        (8, NOW(), NOW(), 5, '套装类型'),

        -- 佳能EOS R50 规格
        (9, NOW(), NOW(), 6, '颜色'),
        (10, NOW(), NOW(), 6, '套装类型');

        SELECT '数据导入成功！' AS result;
    ELSE
        SELECT '表中已有数据，跳过导入。' AS result;
    END IF;
ENd;
call import_data_tb_spu_specification();

