use meiduo_mall;
drop procedure if exists import_data_tb_channel_group;
CREATE PROCEDURE import_data_tb_channel_group()
BEGIN
    DECLARE num INT;
    SELECT COUNT(1) INTO num FROM tb_channel_group;

    IF num = 0 THEN
        insert into tb_channel_group(create_time, update_time, name)
        values(now(), now(), '数码');

        SELECT '数据导入成功！' AS result;
    ELSE
        SELECT '表中已有数据，跳过导入。' AS result;
    END IF;
ENd;
call import_data_tb_channel_group();

