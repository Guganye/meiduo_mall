use meiduo_mall;
drop procedure if exists import_data_tb_goods_channel;
CREATE PROCEDURE import_data_tb_goods_channel()
BEGIN
    DECLARE num INT;
    SELECT COUNT(1) INTO num FROM tb_goods_channel;

    IF num = 0 THEN
        insert into tb_goods_channel(create_time, update_time, url, sequence, category_id, group_id)
        values(now(), now(), 'https://www.baidu.com/s?wd=%E6%89%8B%E6%9C%BA', 1, 1, 1), # 手机
              (now(), now(), 'https://www.baidu.com/s?wd=%E7%9B%B8%E6%9C%BA', 2, 4, 1); # 相机

        SELECT '数据导入成功！' AS result;
    ELSE
        SELECT '表中已有数据，跳过导入。' AS result;
    END IF;
ENd;
call import_data_tb_goods_channel();

