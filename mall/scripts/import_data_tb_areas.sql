use meiduo_mall;
drop procedure if exists import_data_tb_areas;
CREATE PROCEDURE import_data_tb_areas()
BEGIN
    DECLARE num INT;
    SELECT COUNT(1) INTO num FROM tb_areas;

    IF num = 0 THEN
        -- 插入省级数据
        INSERT INTO tb_areas(id, name, parent_id, create_time, update_time) VALUES
        ('110000', '北京市', NULL, NOW(), NOW()),
        ('120000', '天津市', NULL, NOW(), NOW()),
        ('130000', '河北省', NULL, NOW(), NOW()),
        ('140000', '山西省', NULL, NOW(), NOW()),
        ('150000', '内蒙古自治区', NULL, NOW(), NOW()),
        ('210000', '辽宁省', NULL, NOW(), NOW()),
        ('220000', '吉林省', NULL, NOW(), NOW()),
        ('230000', '黑龙江省', NULL, NOW(), NOW()),
        ('310000', '上海市', NULL, NOW(), NOW()),
        ('320000', '江苏省', NULL, NOW(), NOW()),
        ('330000', '浙江省', NULL, NOW(), NOW()),
        ('340000', '安徽省', NULL, NOW(), NOW()),
        ('350000', '福建省', NULL, NOW(), NOW()),
        ('360000', '江西省', NULL, NOW(), NOW()),
        ('370000', '山东省', NULL, NOW(), NOW()),
        ('410000', '河南省', NULL, NOW(), NOW()),
        ('420000', '湖北省', NULL, NOW(), NOW()),
        ('430000', '湖南省', NULL, NOW(), NOW()),
        ('440000', '广东省', NULL, NOW(), NOW()),
        ('450000', '广西壮族自治区', NULL, NOW(), NOW()),
        ('460000', '海南省', NULL, NOW(), NOW()),
        ('500000', '重庆市', NULL, NOW(), NOW()),
        ('510000', '四川省', NULL, NOW(), NOW()),
        ('520000', '贵州省', NULL, NOW(), NOW()),
        ('530000', '云南省', NULL, NOW(), NOW()),
        ('540000', '西藏自治区', NULL, NOW(), NOW()),
        ('610000', '陕西省', NULL, NOW(), NOW()),
        ('620000', '甘肃省', NULL, NOW(), NOW()),
        ('630000', '青海省', NULL, NOW(), NOW()),
        ('640000', '宁夏回族自治区', NULL, NOW(), NOW()),
        ('650000', '新疆维吾尔自治区', NULL, NOW(), NOW()),
        ('710000', '台湾省', NULL, NOW(), NOW()),
        ('810000', '香港特别行政区', NULL, NOW(), NOW()),
        ('820000', '澳门特别行政区', NULL, NOW(), NOW());

        -- 插入北京市数据
        INSERT INTO tb_areas(id, name, parent_id, create_time, update_time) VALUES
        ('110100', '北京市', '110000', NOW(), NOW()),
        ('110101', '东城区', '110100', NOW(), NOW()),
        ('110102', '西城区', '110100', NOW(), NOW()),
        ('110105', '朝阳区', '110100', NOW(), NOW()),
        ('110106', '丰台区', '110100', NOW(), NOW()),
        ('110107', '石景山区', '110100', NOW(), NOW()),
        ('110108', '海淀区', '110100', NOW(), NOW()),
        ('110109', '门头沟区', '110100', NOW(), NOW()),
        ('110111', '房山区', '110100', NOW(), NOW()),
        ('110112', '通州区', '110100', NOW(), NOW()),
        ('110113', '顺义区', '110100', NOW(), NOW()),
        ('110114', '昌平区', '110100', NOW(), NOW()),
        ('110115', '大兴区', '110100', NOW(), NOW()),
        ('110116', '怀柔区', '110100', NOW(), NOW()),
        ('110117', '平谷区', '110100', NOW(), NOW()),
        ('110118', '密云区', '110100', NOW(), NOW()),
        ('110119', '延庆区', '110100', NOW(), NOW());

        -- 插入天津市数据
        INSERT INTO tb_areas(id, name, parent_id, create_time, update_time) VALUES
        ('120100', '天津市', '120000', NOW(), NOW()),
        ('120101', '和平区', '120100', NOW(), NOW()),
        ('120102', '河东区', '120100', NOW(), NOW()),
        ('120103', '河西区', '120100', NOW(), NOW()),
        ('120104', '南开区', '120100', NOW(), NOW()),
        ('120105', '河北区', '120100', NOW(), NOW()),
        ('120106', '红桥区', '120100', NOW(), NOW()),
        ('120110', '东丽区', '120100', NOW(), NOW()),
        ('120111', '津南区', '120100', NOW(), NOW()),
        ('120112', '西青区', '120100', NOW(), NOW()),
        ('120113', '北辰区', '120100', NOW(), NOW()),
        ('120114', '武清区', '120100', NOW(), NOW()),
        ('120115', '宝坻区', '120100', NOW(), NOW()),
        ('120116', '滨海新区', '120100', NOW(), NOW()),
        ('120117', '宁河区', '120100', NOW(), NOW()),
        ('120118', '静海区', '120100', NOW(), NOW()),
        ('120119', '蓟州区', '120100', NOW(), NOW());

        -- 可以继续添加其他省份的数据...

        SELECT '数据导入成功！' AS result;
    ELSE
        SELECT '表中已有数据，跳过导入。' AS result;
    END IF;
ENd;
call import_data_tb_areas();

