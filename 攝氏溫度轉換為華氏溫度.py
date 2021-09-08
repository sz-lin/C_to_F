#攝氏溫度轉換為華氏溫度
temperture_C = input('請輸入攝氏溫度: ')
# temperture = int(temperture)  -->原寫法--要注意溫度不一定是整數
temperture_C = float(temperture_C) #要用浮點數

temperture_F = (temperture_C*9/5)+32
print('華氏溫度為:',temperture_F)