# 该脚本将终端输出的结果文件保存为excel方便查看不同模型的准确率
import os
import re
import pandas as pd


def get_values(metric_and_std):
    """ 解开列表套元组指标里的值和标准差 """
    metric = []
    std = []
    for i in range(len(metric_and_std)):
        num_str = metric_and_std[i][0][-1]
        num_str = num_str.replace(' ', '').split("+-");
        metric.append(float(num_str[0]))
        std.append(float(num_str[1]))
    return metric, std


if __name__ == "__main__":
    logsList = os.listdir("../logs")

    model = []
    dataset = []
    oa_and_std = []
    aa_and_std = []
    kappa_and_std = []

    # 遍历所有文件，获取相关信息
    for file in logsList:
        model.append(file.split('_')[0])
        dataset.append(file.split('_')[-1].split('.')[0])
        with open("../logs/"+file, 'r') as f:
            for line in f.readlines():
                line = line.strip('\n')
                if len(re.findall("(Accuracy:) (\d+.\d+ \+\- \d+\.\d+)", line)) != 0:
                    oa_and_std.append(re.findall("(Accuracy:) (\d+.\d+ \+\- \d+\.\d+)", line))
                if len(re.findall("(AA:) (\d+.\d+ \+\- \d+\.\d+)", line)) != 0:
                    aa_and_std.append(re.findall("(AA:) (\d+.\d+ \+\- \d+\.\d+)", line))
                if len(re.findall("(Kappa:) (\d+.\d+ \+\- \d+\.\d+)", line)) != 0:
                    kappa_and_std.append(re.findall("(Kappa:) (\d+.\d+ \+\- \d+\.\d+)", line))

    oa, oa_std = get_values(oa_and_std)
    aa, aa_std = get_values(aa_and_std)
    kappa, kappa_std = get_values(kappa_and_std)

    # 所有数据存储为一个字典
    data_dict = {
        'model': model,
        'dataset': dataset,
        'oa': oa,
        'oa_std': oa_std,
        'aa': aa,
        'aa_std': aa_std,
        'kappa': kappa,
        'kappa_std': kappa_std,
    }
    
    # 用字典创建df
    df = pd.DataFrame.from_dict(data_dict)
    print(df)

    # 保存为excel
    df.to_excel("./models_datasets_metrics.xlsx")
    print("finished")
    