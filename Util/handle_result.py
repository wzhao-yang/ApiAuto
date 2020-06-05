# coding=utf-8
import os
import sys

from deepdiff import DeepDiff

from Util.handle_json import get_value

base_path = os.getcwd()
sys.path.append(base_path)


# 定义获取返回结果集得方法
def handle_result(url, code):
    # print("打印返回得code------->", code, type(code))
    data = get_value(url, "../Config/code_message.json")
    if data is not None:
        for i in data:
            message = i.get(int(code))
            # message = i.get(str(code))
            if message:
                return message
    return None


# 获取请求返回值得字典，进行比较
def get_result_json(url, status):
    data = get_value(url, "../Config/result.json")
    if data is not None:
        for i in data:
            message = i.get(status)
            if message:
                return message
    return None


#  校验返回数据格式，进行递归
def handle_result_json(dict1, dict2):
    # 判断如果dict1和dict2有一个不是字典格式得情况下，就不进行比较
    # dict1 = {"resultCode":2000,"errMsg":"null","content":[{"orderId":146631,"orderNo":"200558728226","status":6,"title":"Apple iPhone XS 双卡双待 智能手机【预定】","subtitle":"null","price":100.000000,"totalFee":100.000000,"originalPrice":"null","picPath":"https://img.gouta.cn/2d3bdd6a-f6e7-4f1c-8211-6e7ab06deace","color":"null","goodsSize":"null","orderType":3,"fqStatus":"null","attrList":[{"attrCategoryId":1,"attrId":1308,"attrName":"金色","attrUrl":"https://img.gouta.cn/2d3bdd6a-f6e7-4f1c-8211-6e7ab06deace"}],"paymentType":2,"cashPaymentType":3,"orderCreateTime":"null","isIntereFree":"null","isPreRepay":"null","preRepayBusinessId":"null"}]}
    # dict2 = {"resultCode":2000,"errMsg":"null","content":[{"orderId":146631,"orderNo":"200558728226","status":6,"title":"Apple iPhone XS 双卡双待 智能手机【预定】","subtitle":"null","price":100.000000,"totalFee":100.000000,"originalPrice":"null","picPath":"https://img.gouta.cn/2d3bdd6a-f6e7-4f1c-8211-6e7ab06deace","color":"null","goodsSize":"null","orderType":3,"fqStatus":"null","attrList":[{"attrCategoryId":1,"attrId":1308,"attrName":"金色","attrUrl":"https://img.gouta.cn/2d3bdd6a-f6e7-4f1c-8211-6e7ab06deace"}],"paymentType":2,"cashPaymentType":3,"orderCreateTime":"null","isIntereFree":"null","isPreRepay":"null","preRepayBusinessId":"null"}]}

    if isinstance(dict1, dict) and isinstance(dict2, dict):
        # ignore_order diff不同得地方，并且忽略重复得地方，直接判断格式是否相同就行
        cmp_dict = DeepDiff(dict1, dict2, ignore_order=True).to_dict()
        # print(cmp_dict)
        # 判断values_changed并且字典格式dictionary_item_added，case就认为失败
        # if cmp_dict.get("values_changed") and cmp_dict.get("dictionary_item_added"):
        # 判断如果只是key发生变化，case失败，只是values发生变化，case通过
        if cmp_dict.get("dictionary_item_added"):
            print("比较后-------->case失败，发现dictionary_item_added变化,", cmp_dict)
            return False
            # print("case测试失败")
        else:
            print("比较后-------->case成功，只有value变化,", cmp_dict)
            return True
            # print("Case测试通过")
        # print(cmp_dict)
    return False


if __name__ == '__main__':
    dict1 = {"resultCode":2000,"errMsg":"null","content":[{"orderId":146631,"orderNo":"200558728226","status":6,"title":"Apple iPhone XS 双卡双待 智能手机【预定】","subtitle":"null","price":100.000000,"totalFee":100.000000,"originalPrice":"null","picPath":"https://img.gouta.cn/2d3bdd6a-f6e7-4f1c-8211-6e7ab06deace","color":"null","goodsSize":"null","orderType":3,"fqStatus":"null","attrList":[{"attrCategoryId":1,"attrId":1308,"attrName":"金色","attrUrl":"https://img.gouta.cn/2d3bdd6a-f6e7-4f1c-8211-6e7ab06deace"}],"paymentType":2,"cashPaymentType":3,"orderCreateTime":"null","isIntereFree":"null","isPreRepay":"null","preRepayBusinessId":"null"}]}
    dict2 = {"resultCode":2000,"errMsg":"null","content":[{"orderId":146631,"orderNo":"200558728226","status":6,"title":"Apple iPhone XS 双卡双待 智能手机【预定】","subtitle":"null","price":100.000000,"totalFee":100.000000,"originalPrice":"null","picPath":"https://img.gouta.cn/2d3bdd6a-f6e7-4f1c-8211-6e7ab06deace","color":"null","goodsSize":"null","orderType":3,"fqStatus":"null","attrList":[{"attrCategoryId":1,"attrId":1308,"attrName":"金色","attrUrl":"https://img.gouta.cn/2d3bdd6a-f6e7-4f1c-8211-6e7ab06deace"}],"paymentType":2,"cashPaymentType":3,"orderCreateTime":"null","isIntereFree":"null","isPreRepay":"null","preRepayBusinessId":"null"}]}
    # # 测试接口code返回值
    # data = handle_result("api/v1/login/loginWithSms", "2000")
    # print(data)
    print(handle_result_json(dict1, dict2))
    print(get_result_json("api/v1/order/myOrderList?", "content"))
    # print(json.dumps(data,sort_keys=True,indent=2))
