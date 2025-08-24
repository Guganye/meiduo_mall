use meiduo_mall;
drop procedure if exists import_data_tb_sku;
CREATE PROCEDURE import_data_tb_sku()
BEGIN
    DECLARE num INT;
    SELECT COUNT(1) INTO num FROM tb_sku;

    IF num = 0 THEN
        -- iPhone 15 Pro SKU
        INSERT INTO tb_sku (id, create_time, update_time, name, caption, url, spu_id, price, cost_price, market_price, stock, sales, comments, is_launched) VALUES
        (1, NOW(), NOW(), 'iPhone 15 Pro 128GB 黑色钛金属', 'A17 Pro芯片，钛金属设计', concat('https://www.baidu.com/s?wd=', name), 1, 7999.00, 6500.00, 8999.00, 50, 0, 0, TRUE),
        (2, NOW(), NOW(), 'iPhone 15 Pro 256GB 蓝色钛金属', '大存储空间，流畅体验', concat('https://www.baidu.com/s?wd=', name), 1, 8999.00, 7500.00, 9999.00, 40, 0, 0, TRUE),
        (3, NOW(), NOW(), 'iPhone 15 Pro 512GB 白色钛金属', '超大存储，专业体验', concat('https://www.baidu.com/s?wd=', name), 1, 10999.00, 9000.00, 11999.00, 30, 0, 0, TRUE),

        -- 华为Mate 60 Pro SKU
        (4, NOW(), NOW(), '华为Mate 60 Pro 256GB 雅丹黑', '卫星通话，鸿蒙系统', concat('https://www.baidu.com/s?wd=', name), 2, 6999.00, 5800.00, 7999.00, 60, 0, 0, TRUE),
        (5, NOW(), NOW(), '华为Mate 60 Pro 512GB 南糯紫', '大存储，流畅体验', concat('https://www.baidu.com/s?wd=', name), 2, 7999.00, 6800.00, 8999.00, 45, 0, 0, TRUE),

        -- 小米14 Pro SKU
        (6, NOW(), NOW(), '小米14 Pro 256GB 黑色', '徕卡影像，骁龙8 Gen 3', concat('https://www.baidu.com/s?wd=', name), 3, 4299.00, 3500.00, 4999.00, 80, 0, 0, TRUE),
        (7, NOW(), NOW(), '小米14 Pro 512GB 白色', '大存储，流畅体验', concat('https://www.baidu.com/s?wd=', name), 3, 4799.00, 3900.00, 5499.00, 65, 0, 0, TRUE),

        -- 大疆Pocket 3 SKU
        (8, NOW(), NOW(), '大疆Pocket 3 标准版', '一英寸传感器，4K拍摄', concat('https://www.baidu.com/s?wd=', name), 4, 3499.00, 2800.00, 3999.00, 25, 0, 0, TRUE),
        (9, NOW(), NOW(), '大疆Pocket 3 全能套装', '全套配件，创作无忧', concat('https://www.baidu.com/s?wd=', name), 4, 4499.00, 3600.00, 4999.00, 20, 0, 0, TRUE),

        -- 索尼A7M4 SKU
        (10, NOW(), NOW(), '索尼A7M4 单机身', '全画幅微单，专业摄影', concat('https://www.baidu.com/s?wd=', name), 5, 16999.00, 14000.00, 18999.00, 15, 0, 0, TRUE),
        (11, NOW(), NOW(), '索尼A7M4 套机(28-70mm)', '入门套装，即买即用', concat('https://www.baidu.com/s?wd=', name), 5, 18999.00, 15500.00, 20999.00, 12, 0, 0, TRUE),

        -- 佳能EOS R50 SKU
        (12, NOW(), NOW(), '佳能EOS R50 黑色单机身', '入门微单，轻便易用', concat('https://www.baidu.com/s?wd=', name), 6, 4599.00, 3800.00, 5199.00, 35, 0, 0, TRUE),
        (13, NOW(), NOW(), '佳能EOS R50 白色套机(18-45mm)', '白色时尚，套装优惠', concat('https://www.baidu.com/s?wd=', name), 6, 5599.00, 4600.00, 6199.00, 28, 0, 0, TRUE);

        # default_image_id后续设置
        SELECT '数据导入成功！' AS result;
    ELSE
        SELECT '表中已有数据，跳过导入。' AS result;
    END IF;
ENd;
call import_data_tb_sku();


