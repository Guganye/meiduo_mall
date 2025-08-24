use meiduo_mall;
drop procedure if exists import_data_tb_sku_specification;
CREATE PROCEDURE import_data_tb_sku_specification()
BEGIN
    DECLARE num INT;
    SELECT COUNT(1) INTO num FROM tb_sku_specification;

    IF num = 0 THEN
        -- 插入省级数据
        -- iPhone 15 Pro SKU规格
        INSERT INTO tb_sku_specification (id, create_time, update_time, sku_id, option_id) VALUES
        (1, NOW(), NOW(), 1, 1), (2, NOW(), NOW(), 1, 4),  -- 黑色 128GB
        (3, NOW(), NOW(), 2, 2), (4, NOW(), NOW(), 2, 5),  -- 蓝色 256GB
        (5, NOW(), NOW(), 3, 3), (6, NOW(), NOW(), 3, 6),  -- 白色 512GB

        -- 华为Mate 60 Pro SKU规格
        (7, NOW(), NOW(), 4, 7), (8, NOW(), NOW(), 4, 9),  -- 雅丹黑 256GB
        (9, NOW(), NOW(), 5, 8), (10, NOW(), NOW(), 5, 10), -- 南糯紫 512GB

        -- 小米14 Pro SKU规格
        (11, NOW(), NOW(), 6, 11), (12, NOW(), NOW(), 6, 13), -- 黑色 256GB
        (13, NOW(), NOW(), 7, 12), (14, NOW(), NOW(), 7, 14), -- 白色 512GB

        -- 大疆Pocket 3 SKU规格
        (15, NOW(), NOW(), 8, 15), -- 标准版
        (16, NOW(), NOW(), 9, 16), -- 全能套装

        -- 索尼A7M4 SKU规格
        (17, NOW(), NOW(), 10, 17), -- 单机身
        (18, NOW(), NOW(), 11, 18), -- 套机

        -- 佳能EOS R50 SKU规格
        (19, NOW(), NOW(), 12, 19), (20, NOW(), NOW(), 12, 21), -- 黑色 单机身
        (21, NOW(), NOW(), 13, 20), (22, NOW(), NOW(), 13, 22); -- 白色 套机


        SELECT '数据导入成功！' AS result;
    ELSE
        SELECT '表中已有数据，跳过导入。' AS result;
    END IF;
ENd;
call import_data_tb_sku_specification();

