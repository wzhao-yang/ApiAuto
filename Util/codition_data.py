# coding=utf-8
import json

from jsonpath_rw import parse

from Util.handle_excel import excel_data


def split_data(data):
    """
    拆分单元格数据
    :param data:
    :return:
    """
    case_id = data.split(">")[0]
    rule_data = data.split(">")[1]
    return case_id, rule_data


def depend_data(data):
    '''
    获取依赖结果集
    '''
    case_id = split_data(data)[0]
    row_number = excel_data.get_rows_number(case_id)
    data = excel_data.get_cell_value(row_number, 14)
    return data


def get_depend_data(res_data, key):
    """
    获取依赖字段
    :param res_data:
    :param key:
    :return:
    """
    res_data = json.loads(res_data)

    json_exe = parse(key)
    madle = json_exe.find(res_data)  # 查找数据
    return [math.value for math in madle][0]
    # for math in madle:
    #     print(math.value)


def get_data(data):
    """
    获取依赖数据
    :param data:
    :return:
    """
    res_data = depend_data(data)
    rule_data = split_data(data)[1]
    return get_depend_data(res_data, rule_data)


if __name__ == "__main__":
    # print(depend_data("test_001>data:banner:id"))
    data = {
        "a": "a1",
        "b": "b1",
        "c": [
            {
                "d": "d1"
        },
            {
                "d": "d2"
            }
        ]
    }
    key = 'c.[1].d'
    print(get_depend_data(data, key))
