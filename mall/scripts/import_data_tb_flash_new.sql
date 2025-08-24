use meiduo_mall;
drop procedure if exists import_data_tb_flash_new;
CREATE PROCEDURE import_data_tb_flash_new()
BEGIN
    DECLARE num INT;
    SELECT COUNT(1) INTO num FROM tb_flash_new;

    IF num = 0 THEN
        INSERT INTO tb_flash_new (id, create_time, update_time, sku_id, content, sequence, status) VALUES
        (1, NOW(), NOW(), 1, '🔥 新品上市！iPhone 15 Pro 128GB 黑色钛金属限时优惠', 1, TRUE),
        (2, NOW(), NOW(), 2, '🎉 iPhone 15 Pro 256GB 蓝色钛金属，库存有限先到先得', 2, TRUE),
        (3, NOW(), NOW(), 4, '🚀 华为Mate 60 Pro 256GB 雅丹黑，支持卫星通话', 3, TRUE),
        (4, NOW(), NOW(), 5, '🌟 华为Mate 60 Pro 512GB 南糯紫，大存储畅享体验', 4, TRUE),
        (5, NOW(), NOW(), 6, '📱 小米14 Pro 256GB 黑色，徕卡影像旗舰', 5, TRUE),
        (6, NOW(), NOW(), 7, '💫 小米14 Pro 512GB 白色，超大存储性能强劲', 6, TRUE),
        (7, NOW(), NOW(), 8, '🎬 大疆Pocket 3 标准版，vlog创作神器', 7, TRUE),
        (8, NOW(), NOW(), 9, '🎁 大疆Pocket 3 全能套装，配件齐全创作无忧', 8, TRUE),
        (9, NOW(), NOW(), 10, '📸 索尼A7M4 单机身，专业摄影首选', 9, TRUE),
        (10, NOW(), NOW(), 11, '👍 索尼A7M4 套机，入门即用性价比高', 10, TRUE),
        (11, NOW(), NOW(), 12, '📷 佳能EOS R50 黑色单机身，轻便入门微单', 11, TRUE),
        (12, NOW(), NOW(), 13, '✨ 佳能EOS R50 白色套机，时尚外观即买即用', 12, TRUE),
        (13, NOW(), NOW(), 3, '💎 iPhone 15 Pro 512GB 白色钛金属，尊贵体验', 13, FALSE);

        SELECT '数据导入成功！' AS result;
    ELSE
        SELECT '表中已有数据，跳过导入。' AS result;
    END IF;
ENd;
call import_data_tb_flash_new();

