use meiduo_mall;
drop procedure if exists import_data_tb_spu;
CREATE PROCEDURE import_data_tb_spu()
BEGIN
    DECLARE num INT;
    SELECT COUNT(1) INTO num FROM tb_spu;

    IF num = 0 THEN
        INSERT INTO tb_spu (id, create_time, update_time, name, brand_id, category1_id, category2_id, category3_id, sales, comments, desc_detail, desc_pack, desc_service, category_id) VALUES
        (1, NOW(), NOW(), 'iPhone 15 Pro', 1, 1, 2, 3, 0, 0, 'iPhone 15 Pro采用航空级钛金属设计，A17 Pro芯片，性能强劲，支持5G网络', '原装充电器、数据线、说明书、取卡针', '一年保修，7天无理由退货，15天换货', 8),
        (2, NOW(), NOW(), '华为Mate 60 Pro', 2, 1, 2, 3, 0, 0, '华为Mate 60 Pro搭载麒麟9000S芯片，支持卫星通话，鸿蒙操作系统', '充电器、数据线、保护壳、贴膜', '一年保修，15天换货，30天价保', 7),
        (3, NOW(), NOW(), '小米14 Pro', 3, 1, 2, 3, 0, 0, '小米14 Pro搭载骁龙8 Gen 3处理器，徕卡影像系统，2K屏幕', '充电器、数据线、贴膜、保护壳', '一年保修，30天价保，7天无理由退货', 9),
        (4, NOW(), NOW(), '大疆Pocket 3', 4, 4, 5, 6, 0, 0, '大疆Pocket 3口袋云台相机，一英寸传感器，4K/120fps', '主机、保护壳、三脚架、充电线、腕带', '一年保修，7天无理由退货', 10),
        (5, NOW(), NOW(), '索尼A7M4', 5, 4, 5, 6, 0, 0, '索尼A7M4全画幅微单相机，3300万像素，4K视频', '机身、电池、充电器、肩带、说明书', '一年保修，清洁服务', 11),
        (6, NOW(), NOW(), '佳能EOS R50', 6, 4, 5, 6, 0, 0, '佳能EOS R50入门微单，轻便易用，4K视频', '机身、镜头、电池、充电器、数据线', '一年保修', 12);

            SELECT '数据导入成功！' AS result;
    ELSE
        SELECT '表中已有数据，跳过导入。' AS result;
    END IF;
ENd;
call import_data_tb_spu();

