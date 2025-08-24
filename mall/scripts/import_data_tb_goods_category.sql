use meiduo_mall;
drop procedure if exists import_data_tb_goods_category;
CREATE PROCEDURE import_data_tb_goods_category()
BEGIN
    DECLARE num INT;
    SELECT COUNT(1) INTO num FROM tb_goods_category;

    IF num = 0 THEN
        insert into tb_goods_category(id, create_time, update_time, name, parent_id)
        values(1, now(), now(), '手机', NULL), (2, now(), now(), '通讯', 1),(3, now(), now(), '老人机', 2),
        (4, now(), now(), '相机', NULL), (5, now(), now(), '摄影', 4),(6, now(), now(), '拍立得', 5),
        (7, now(), now(), '华为老人机', 3),(8, now(), now(), '苹果老人机', 3),(9, now(), now(), '小米老人机', 3),
        (10, now(), now(), '大疆拍立得', 6),(11, now(), now(), '索尼拍立得', 6),(12, now(), now(), '佳能拍立得', 6);

        SELECT '数据导入成功！' AS result;
    ELSE
        SELECT '表中已有数据，跳过导入。' AS result;
    END IF;
ENd;
call import_data_tb_goods_category();

