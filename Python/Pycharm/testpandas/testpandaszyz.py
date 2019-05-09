import pandas as pd
import numpy as np

#1重复值的处理
def test_drop_duplicates():
    print("利用drop_duplicates()函数删除数据表中重复多余的记录, 比如删除重复多余的ID.")
    df = pd.DataFrame({"ID": ["A1000","A1001","A1002", "A1002"],
        "departmentId": [60001,60001, 60001, 60001]})
    print(df)
    print(df.drop_duplicates())
#2补齐缺失值
def test_fillna():
    df=pd.DataFrame({'ID':['A10001', 'A10002', 'A10003', 'A10004'], "Salary":[11560, np.NaN, 12988, 12080]})
    print(df)
    print("用Salary字段的样本均值填充缺失值")
    df["Salary"]=df["Salary"].fillna(df["Salary"].mean())
    print(df)
#3删除缺失值
def test_dropna():
    df=pd.DataFrame({"ID": ["A1000","A1001","A1002"],
             "entrytime": ["2015-05-06",pd.NaT,"2016-07-01" ]})
    print(df)
    print("示例: 删除entrytime中缺失的值,采用dropna函数对缺失值进行删除:")
    print(df.dropna())

#4 查看数据类型
def test_dtypes():
    df=pd.DataFrame({"ID": [100000,100101,100201],"Surname": [" Zhao ","Qian"," Sun " ]})
    print("所有列用dtypes")
    print(df.dtypes)
    print("某一列用dtype")
    print(df["ID"].dtype)

#5 修改数据类型
def test_astype():
    df=pd.DataFrame({"ID": [100000,100101,100201],"Surname": [" Zhao ","Qian"," Sun " ]})
    print(df.dtypes)
    print("将ID列类型转为字符串")
    df["ID"].astype(str)
    print(df.dtypes)

#6 字段的抽取
def test_slice():
    df= pd.DataFrame({"ID": [100000,100101,100201],"Surname": [" Zhao ","Qian"," Sun " ]})
    print("需要将ID列的类型转换为字符串, 否则无法使用slice()函数")
    df["ID"]= df["ID"].astype(str)
    print(df)
    print("抽取ID前两位")
    print(df["ID"].str.slice(0,2))

#7 字段的拆分
#使用split() 第一个参数是分隔的字符串 默认空格；
#第二个参数是分隔符的使用次数 默认分隔所有；
#第三个参数是True 在不同列展开，否则 以序列形式展开
def test_split():
    df=pd.DataFrame({"ID": [100000,100101,100201],"Surname_Age": ["Zhao_23","Qian_33","Sun_28" ]})
    print(df)
    print("对Surname_Age字段进行拆分")
    df_new = df["Surname_Age"].str.split("_", expand =True)
    print(df_new)

#8. 字段的命名
#有两种方式一种是使用rename()函数, 另一种是直接设置columns参数
def test_rename_columns():
    df = pd.DataFrame({"ID": [100000,100101,100201],"Surname_Age": ["Zhao_23","Qian_33","Sun_28" ]})
    print(df)
    print("第一种方法使用rename()函数")
    df_new = df["Surname_Age"].str.split("_", expand =True).rename(columns={0: "Surname", 1: "Age"})
    print(df_new)
    print("第二种方法直接设置columns参数")
    df_new = df["Surname_Age"].str.split("_", expand =True)
    df_new.columns = ["Surname","Age"]
    print(df_new)

#9. 字段的合并
#使用merge()函数对字段进行合并操作.
def test_merge():
    df = pd.DataFrame({"ID": [100000,100101,100201],"Surname_Age": ["Zhao_23","Qian_33","Sun_28" ]})
    print(df)
    df_new = df["Surname_Age"].str.split("_", expand =True)
    df_new.columns = ["Surname","Age"]
    print(df_new)
    print("使用merge函数对两表的字段进行合并操作.")
    print(pd.merge(df, df_new, left_index =True, right_index=True))

#10. 字段的删除
#利用drop()函数对字段进行删除.
def test_drop():
    df = pd.DataFrame({"ID": [100000,100101,100201],"Surname_Age": ["Zhao_23","Qian_33","Sun_28" ]})
    print(df)
    df_new = df["Surname_Age"].str.split("_", expand =True)
    df_new.columns = ["Surname","Age"]
    print(df_new)
    df_mer= pd.merge(df, df_new, left_index =True, right_index=True)
    print(df_mer)
    print("drop()删除字段,第一个参数指要删除的字段,axis=1表示字段所在列,inplace为True表示在当前表执行删除.")
    df_mer.drop("Surname_Age", axis = 1, inplace =True)
    print(df_mer)

#11. 记录的抽取
def test_chouqu():
    print("1) 关系运算: df[df.字段名 关系运算符 数值], 比如抽取年龄大于30岁的记录.")
    df = pd.DataFrame({"ID": [100000,100101,100201],"Surname_Age": ["Zhao_23","Qian_33","Sun_28" ]})
    print(df)
    df_new = df["Surname_Age"].str.split("_", expand =True)
    print(df_new)
    df_new.columns = ["Surname","Age"]
    print(df_new)
    df_mer= pd.merge(df, df_new, left_index =True, right_index=True)
    print(df_mer)
    df_mer.drop("Surname_Age", axis = 1, inplace =True)
    print(df_mer)
    print("将Age字段数据类型转化为整型")
    df_mer["Age"] = df_mer["Age"].astype(int)
    print(df_mer)
    print("抽取Age中大于30的记录")
    df_mer[df_mer.Age > 30]
    print(df_mer)
    print("2) 范围运算: df[df.字段名.between(s1, s2)], 注意既包含s1又包含s2, 比如抽取年龄大于等于23小于等于28的记录. ")
    df_mer[df_mer.Age.between(23,28)]
    print(df_mer)
    print("3) 逻辑运算: 与(&) 或(|) 非(not)")
    print("比如上面的范围运算df_mer[df_mer.Age.between(23,28)]就等同于df_mer[(df_mer.Age >= 23) & (df_mer.Age <= 28)]")
    df_mer[(df_mer.Age >= 23 ) & (df_mer.Age <= 28)]
    print(df_mer)
    print("4) 字符匹配: df[df.字段名.str.contains(\"字符\", case = True, na =False)] contains()函数中case=True表示区分大小写, 默认为True; na = False表示不匹配缺失值.")
    df = pd.DataFrame({"ID": [100000,100101,100201],"Surname_Age": ["Zhao_23","Qian_33","Sun_28"],"SpouseAge":[np.NaN,"32",np.NaN]})
    print(df)
    print("匹配SpouseAge中包含2的记录")
    df[df.SpouseAge.str.contains("2",na = False)]
    print(df)
    print("5) 缺失值匹配:df[pd.isnull(df.字段名)]表示匹配该字段中有缺失值的记录.")
    df = pd.DataFrame({"ID": [100000,100101,100201],"Surname_Age": ["Zhao_23","Qian_33","Sun_28"],"SpouseAge":[np.NaN,"32",np.NaN]})
    print(df)
    print("匹配SpouseAge中有缺失值的记录")
    df[pd.isnull(df.SpouseAge)]
    print(df)

#12.记录的合并
def test_concat():
    #使用concat()函数可以将两个或者多个数据表的记录合并一起, 用法: pandas.concat([df1, df2, df3.....])
    df1 = pd.DataFrame({"ID": ["A10006","A10001"],"Salary": [12000, 20000]})
    df2 = pd.DataFrame({"ID": ["A10008"], "Salary": [10000]})
    print("使用concat()函数将df1与df2的记录进行合并")
    print(pd.concat([df1, df2]))

#13.	 简单计算新建一个数据表df
def test_newdataframe():
    df = pd.DataFrame({"地区": ["A区","B区","C区"],
    "前半年销量": [3500, 4500,3800],
    "后半年销量": [3000, 6000,5000],
    "单价": [10, 18, 15]})
    print(df)


test_drop_duplicates()
test_fillna()
test_dropna()
test_dtypes()
test_astype()
test_slice()
test_split()
test_rename_columns()
test_merge()
test_drop()
test_chouqu()
test_concat()
test_newdataframe()
#xuanxiang={"1":"重复值的处理","2":"补齐缺失值","3":"删除缺失值","4":"查看数据类型","5":"修改数据类型","6":"字段的抽取",
           #"7":"字段的拆分","8":"字段的命名","9":"字段的合并","10":"字段的删除","11":"记录的抽取","12":"记录的合并","13":"简单创建数据表"}
#print(xuanxiang)
#c=input("输入第几个测试\n")

#print(c)
#if c=='1':
#    test_drop_duplicates()
#elif c=='2':
#    test_fillna()
#elif c=='3':
#    test_dropna()
#elif c=='4':
#    test_dtypes()
#elif c=='5':
#    test_astype()
#elif c=='6':
#    test_slice()
#elif c=='7':
#    test_split()
#elif c=='8':
#    test_rename_columns()
#elif c=='9':
#    test_merge()
#elif c=='10':
#    test_drop()
#elif c=='11':
#    test_chouqu()
#elif c=='12':
#    test_concat()
#elif c=='13':
#    test_newdataframe()
#else:
#    print("选择有误")
