use meiduo_mall;
drop procedure if exists import_data_tb_sku_image;
CREATE PROCEDURE import_data_tb_sku_image()
BEGIN
    DECLARE num INT;
    SELECT COUNT(1) INTO num FROM tb_sku_image;

    IF num = 0 THEN
        -- iPhone 15 Pro 图片
        INSERT INTO tb_sku_image (id, create_time, update_time, sku_id, image) VALUES
        (1, NOW(), NOW(), 1, 'skuImages/phone.webp'),
        (2, NOW(), NOW(), 1, 'skuImages/phone.webp'),
        (3, NOW(), NOW(), 1, ''),
        (4, NOW(), NOW(), 2, 'skuImages/phone.webp'),
        (5, NOW(), NOW(), 2, 'skuImages/phone.webp'),
        (6, NOW(), NOW(), 3, 'skuImages/phone.webp'),
        (7, NOW(), NOW(), 3, 'skuImages/phone.webp'),

        -- 华为Mate 60 Pro 图片
        (8, NOW(), NOW(), 4, 'skuImages/phone.webp'),
        (9, NOW(), NOW(), 4, 'skuImages/phone.webp'),
        (10, NOW(), NOW(), 5, 'skuImages/phone.webp'),
        (11, NOW(), NOW(), 5, 'skuImages/phone.webp'),

        -- 小米14 Pro 图片
        (12, NOW(), NOW(), 6, 'skuImages/phone.webp'),
        (13, NOW(), NOW(), 6, 'skuImages/phone.webp'),
        (14, NOW(), NOW(), 7, 'skuImages/phone.webp'),
        (15, NOW(), NOW(), 7, 'skuImages/phone.webp'),

        -- 大疆Pocket 3 图片
        (16, NOW(), NOW(), 8, 'skuImages/camera.webp'),
        (17, NOW(), NOW(), 8, 'skuImages/camera.webp'),
        (18, NOW(), NOW(), 9, 'skuImages/camera.webp'),
        (19, NOW(), NOW(), 9, 'skuImages/camera.webp'),

        -- 索尼A7M4 图片
        (20, NOW(), NOW(), 10, 'skuImages/camera.webp'),
        (21, NOW(), NOW(), 10, 'skuImages/camera.webp'),
        (22, NOW(), NOW(), 11, 'skuImages/camera.webp'),
        (23, NOW(), NOW(), 11, 'skuImages/camera.webp'),

        -- 佳能EOS R50 图片
        (24, NOW(), NOW(), 12, 'skuImages/camera.webp'),
        (25, NOW(), NOW(), 12, 'skuImages/camera.webp'),
        (26, NOW(), NOW(), 13, 'skuImages/camera.webp'),
        (27, NOW(), NOW(), 13, 'skuImages/camera.webp');
        SELECT '数据导入成功！' AS result;
    ELSE
        SELECT '表中已有数据，跳过导入。' AS result;
    END IF;
ENd;
call import_data_tb_sku_image();

