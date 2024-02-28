import os
import csv
import shutil
from datetime import datetime

def load_test_plan():
    # 指定計劃檔案的路徑
    plan_file_path = 'plan/general.csv'

    # 初始化一個空列表來存儲讀取到的數據
    test_plan_list = []

    # 開啟CSV檔案並讀取
    with open(plan_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)

        # 跳過標題列
        next(reader)

        # 讀取第一列的數據（從第二行開始）
        for row in reader:
            test_plan_list.append(row[1])

    return test_plan_list

def generate_report(list_test_report):
    # 確定報告檔案的資料夾
    report_folder = 'report'
    os.makedirs(report_folder, exist_ok=True)  # 如果資料夾不存在，則創建它

    # 生成報告檔案的檔名，包含當前的日期和時間
    timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    report_filename = f'{report_folder}/report-{timestamp}.csv'

    # 開啟報告檔案並寫入
    with open(report_filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # 寫入標題列
        writer.writerow(['item', 'response', 'screenshot'])

        # 寫入測試報告
        for row in list_test_report:
            writer.writerow([row['item'], row['response'], row['screenshot']])
