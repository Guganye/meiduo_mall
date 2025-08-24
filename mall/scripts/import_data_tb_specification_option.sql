use meiduo_mall;
drop procedure if exists import_data_tb_specification_option;
CREATE PROCEDURE import_data_tb_specification_option()
BEGIN
    DECLARE num INT;
    SELECT COUNT(1) INTO num FROM tb_specification_option;

    IF num = 0 THEN
        -- iPhone 15 Pro 选项
        INSERT INTO tb_specification_option (id, create_time, update_time, spec_id, value) VALUES
        (1, NOW(), NOW(), 1, '黑色钛金属'),
        (2, NOW(), NOW(), 1, '蓝色钛金属'),
        (3, NOW(), NOW(), 1, '白色钛金属'),
        (4, NOW(), NOW(), 2, '128GB'),
        (5, NOW(), NOW(), 2, '256GB'),
        (6, NOW(), NOW(), 2, '512GB'),

        -- 华为Mate 60 Pro 选项
        (7, NOW(), NOW(), 3, '雅丹黑'),
        (8, NOW(), NOW(), 3, '南糯紫'),
        (9, NOW(), NOW(), 4, '256GB'),
        (10, NOW(), NOW(), 4, '512GB'),

        -- 小米14 Pro 选项
        (11, NOW(), NOW(), 5, '黑色'),
        (12, NOW(), NOW(), 5, '白色'),
        (13, NOW(), NOW(), 6, '256GB'),
        (14, NOW(), NOW(), 6, '512GB'),

        -- 大疆Pocket 3 选项
        (15, NOW(), NOW(), 7, '标准版'),
        (16, NOW(), NOW(), 7, '全能套装'),

        -- 索尼A7M4 选项
        (17, NOW(), NOW(), 8, '单机身'),
        (18, NOW(), NOW(), 8, '套机(28-70mm)'),

        -- 佳能EOS R50 选项
        (19, NOW(), NOW(), 9, '黑色'),
        (20, NOW(), NOW(), 9, '白色'),
        (21, NOW(), NOW(), 10, '单机身'),
        (22, NOW(), NOW(), 10, '套机(18-45mm)');
        SELECT '数据导入成功！' AS result;
    ELSE
        SELECT '表中已有数据，跳过导入。' AS result;
    END IF;
ENd;
call import_data_tb_specification_option();

