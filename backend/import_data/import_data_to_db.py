import os
import django
import pandas as pd
from django.utils import timezone
from datetime import datetime, timedelta

# 设置 Django 的环境变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings.dev")

django.setup()  # 确保在导入任何模型之前调用

from backend.api.models import Water_Quality_Data, Fish_Data


def import_water_quality_data(file_path):
    # 使用pandas读取Excel文件
    df = pd.read_excel(file_path, engine='openpyxl')

    # 遍历DataFrame中的每一行
    for index, row in df.iterrows():
        # 将字符串日期转换为DateTime对象，如果监测时间是日期格式的话,这种写法和row['监测时间']没区别
        # monitoring_time = pd.to_datetime(row['监测时间'])
        # Excel中日期被存储为自1899年12月30日以来的天数!!!!!
        monitoring_time_num = row['监测时间']

        # 如果检测时间为空,直接不存储这一行数据
        if pd.isnull(monitoring_time_num):
            continue

        monitoring_time = datetime(1899, 12, 30) + timedelta(days=monitoring_time_num)

        if isinstance(monitoring_time, datetime):
            # 处理日期数据
            formatted_date = monitoring_time.strftime('%Y-%m-%d')  # 将日期格式化为YYYY-MM-DD
            # print(formatted_date)



        # 创建WaterQualityData模型实例
        water_data = Water_Quality_Data(
            monitoring_time=monitoring_time,
            water_quality_category=row['水质类别'] if row['水质类别'] != '--' else None,
            water_temperature=row['水温（℃）'] if row['水温（℃）'] != '--' else None,
            pH=row['pH(无量纲)'] if row['pH(无量纲)'] != '--' else None,
            dissolved_oxygen=row['溶氧量(mg/L)'] if row['溶氧量(mg/L)'] != '--' else None,
            conductivity=row['电导率（μS/cm）'] if row['电导率（μS/cm）'] != '--' else None,
            turbidity=row['浊度（NTU）'] if row['浊度（NTU）'] != '--' else None,
            permanganate_index=row['高锰酸盐指数（mg/L）'] if row['高锰酸盐指数（mg/L）'] != '--' else None,
            ammonia_nitrogen=row['氨氮（mg/L）'] if row['氨氮（mg/L）'] != '--' else None,
            total_phosphorus=row['总磷（mg/L）'] if row['总磷（mg/L）'] != '--' else None,
            total_nitrogen=row['总氮（mg/L）'] if row['总氮（mg/L）'] != '--' else None,
            site_status=row['站点情况'] if row['站点情况'] != '--' else None
        )

        # 保存模型实例到数据库
        water_data.save()


# 导入鱼类数据
def import_fish_data(file_path):
    # 使用pandas读取Excel文件
    df = pd.read_excel(file_path, engine='openpyxl')

    # 遍历DataFrame中的每一行
    for index, row in df.iterrows():
        # 创建FishData模型实例
        fish_data = Fish_Data(

            species=row['品种'] if row['品种'] != '--' else None,
            body_length=row['体长(cm)'] if row['体长(cm)'] != '--' else None,
            body_weight=row['体重(kg)'] if row['体重(kg)'] != '--' else None,
            health_status=row['健康状况'] if row['健康状况'] != '--' else None,
            fish_group_status=row['鱼群状况'] if row['鱼群状况'] != '--' else None,
            breeding_period=row['繁殖期'] if row['繁殖期'] != '--' else None,
            fish_group_total=row['鱼群总量(t)'] if row['鱼群总量(t)'] != '--' else None,
            fry_number=row['鱼苗数量'] if row['鱼苗数量'] != '--' else None,
            adult_fish_number=row['成鱼数量'] if row['成鱼数量'] != '--' else None

        )

        # 保存模型实例到数据库
        fish_data.save()

# # 执行数据导入
# import_water_quality_data('water_quality_data.xlsx')


def main():
    # 调用函数
    # import_water_quality_data('water_quality_data.xlsx')

    # 再次执行相当于插入数据
    # import_water_quality_data('water_test.xlsx')

    # 导入鱼类数据
    import_fish_data('fish_data.xlsx')

if __name__ == '__main__':
    main()