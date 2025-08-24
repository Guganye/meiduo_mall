use meiduo_mall;
drop procedure if exists import_data_tb_banner;
CREATE PROCEDURE import_data_tb_banner()
BEGIN
    DECLARE num INT;
    SELECT COUNT(1) INTO num FROM tb_banner;

    IF num = 0 THEN
        INSERT INTO tb_banner (id, create_time, update_time, image_id, description, sequence, status) VALUES
        (1, NOW(), NOW(), 1, 'iPhone 15 Pro 黑色钛金属，A17 Pro芯片强劲性能', 1, TRUE),
        (2, NOW(), NOW(), 4, 'iPhone 15 Pro 蓝色钛金属，大存储空间', 2, TRUE),
        (3, NOW(), NOW(), 8, '华为Mate 60 Pro 雅丹黑，卫星通话技术', 3, TRUE),
        (4, NOW(), NOW(), 12, '小米14 Pro 黑色，徕卡影像系统', 4, TRUE),
        (5, NOW(), NOW(), 16, '大疆Pocket 3 标准版，4K口袋云台相机', 5, TRUE),
        (6, NOW(), NOW(), 20, '索尼A7M4 单机身，全画幅专业微单', 6, TRUE),
        (7, NOW(), NOW(), 24, '佳能EOS R50 黑色，入门微单轻便易用', 7, TRUE),
        (8, NOW(), NOW(), 10, '华为Mate 60 Pro 南糯紫，鸿蒙操作系统', 8, FALSE);
        SELECT '数据导入成功！' AS result;
    ELSE
        SELECT '表中已有数据，跳过导入。' AS result;
    END IF;
ENd;
call import_data_tb_banner();
select * from tb_banner;

