import pandas as pd
import matplotlib.pyplot as plt
path = r'C:\Users\sun weiting\Desktop\教育程度.csv'
df = pd.read_csv(path)

# 設定字形
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
#doctor, master, university total
for i in range(6):
    match i:
        case 0:
            degree='edu_doctor_GT' # GT=graduated total
            df[degree] = 0
        case 1:
            degree='edu_doctor_UT' # UT=ungraduated total
            df[degree] = 0
        case 2:
            degree='edu_master_GT'
            df[degree] = 0
        case 3:
            degree='edu_master_UT'
            df[degree] = 0
        case 4:
            degree='edu_university_GT'
            df[degree] = 0
        case 5:
            degree='edu_university_UT'
            df[degree] = 0
    for j in range(2):
        column_name = df.columns[5]
        df[degree] += df[column_name].astype(int)
        df.drop(column_name,axis=1,inplace=True)

# 1. 112年全台灣Doctor, Master, University分別總人數
df['edu_doctor_T'] = df["edu_doctor_GT"]+df["edu_doctor_UT"]
df['edu_master_T'] = df["edu_master_GT"]+df["edu_master_UT"]
df['edu_university_T'] = df["edu_university_GT"]+df["edu_university_UT"]
print('112年全台灣Doctor, Master, University分別總人數: ')
SD = sum(df["edu_doctor_T"])
SM = sum(df["edu_master_T"])
SU = sum(df["edu_university_T"])
print(f'doctor total = {SD}')
print(f'master total = {SM}')
print(f'university total = {SU}')
print('')
DMU_LIST = [SU, SM, SD]
DMU_NAME = ['universitys', 'masters', 'doctors']
plt.title('112年全台灣Doctor, Master, University分別總人數')
plt.barh(DMU_NAME, DMU_LIST,height=0.3)
plt.xlabel('People')
plt.show()
plt.close()

# 2. Doctor, Master, University畢業率
print('Doctor, Master, University畢業率: ')
DR = round(sum(df["edu_doctor_GT"])/sum(df["edu_doctor_T"]),5)
MR = round(sum(df["edu_master_GT"])/sum(df["edu_master_T"]), 5)
UR = round(sum(df["edu_university_GT"])/sum(df["edu_university_T"]),5)
DMU_RATE = [UR, MR, DR]
DMU_NAME = ['universitys', 'masters', 'doctors']
print(f'doctor rate = {DR}')
print(f'master rate = {MR}')
print(f'university rate = {UR}')
print('')
plt.title('Doctor, Master, University畢業率')
plt.ylabel('Rate')
plt.bar(DMU_NAME,DMU_RATE,width=0.3)
plt.show()
plt.close()

# 3. 有讀大學跟沒讀大學的比例
df1 = df.loc[:,'edu_senior_graduated_m':'edu_illiterate_f']
total_one = sum(df1.sum()) # No
df2 = df.loc[:,'edu_doctor_T':'edu_university_T']
total_two = sum(df2.sum()) # Yes
Y_N_RATE = round(total_two/total_one,5)
print('有讀大學跟沒讀大學的比例: ')
print(Y_N_RATE)
print('')
plt.title('有讀大學跟沒讀大學的比例')
plt.pie([total_one,total_two],labels=['No','Yes'],autopct='%1.1f%%')
plt.show()
plt.close()

# 4. 各縣畢業博士生人數
# 迴圈功能為將縣市名縮短至兩個字
for i in range(len(df)): 
    df.loc[i,'site_id']=df['site_id'][i][0:2]
new_df = df.groupby('site_id').sum()['edu_doctor_GT']
N_list = new_df.sort_values()
print('各縣畢業博士生人數: ')
print(N_list)
print('')
plt.title('各縣畢業博士生人數')
plt.barh(N_list.index, N_list)
plt.xlabel('People')
plt.show()
plt.close()

# 5. 各縣有大學學歷以上的人數
new_df = df.groupby('site_id').sum()[['edu_doctor_T','edu_master_T','edu_university_GT']].sum(axis=1).sort_values()
print('各縣有大學學歷以上的人數: ')
print(new_df)
print('')
plt.title('各縣有大學學歷以上的人數')
plt.barh(new_df.index,new_df)
plt.xlabel('People')
plt.show()
plt.close()

# 6. 六都與非六都差距(以大學學歷以上的人數作為判斷標準)
capitals_list=['新北', '臺北', '臺中', '高雄', '桃園', '臺南']
capitals_total=0
non_capital_total=0
# 迴圈功能為六都與非六都人數加總
for i in range(len(new_df)):
    if (new_df.index[i] in capitals_list):
        capitals_total += new_df[i]
    else:
        non_capital_total += new_df[i]
print('六都與非六都差距: ')
print('六都人數 = ',capitals_total)
print('非六都人數 = ',non_capital_total)
plt.title('六都與非六都差距(以大學學歷以上的人數作為判斷標準)')
plt.pie([capitals_total,non_capital_total],labels=['Capitals_total','Non-capitals_total'],autopct='%1.1f%%')
plt.show()
plt.close()