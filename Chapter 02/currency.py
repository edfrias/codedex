# A currency app to convert yuan, yen and won to USDs
yuan = int(input('How much cash do you have in yuan? ')) # 0,14 dólar
yen = int(input('How much cash do you have in yen? ')) # 0,0068 dólar
won = int(input('How much cash do you have in won? ')) # 0,00070 dólar

usds = (yuan * 0.14) + (yen * 0.0068) + (won * 0.0007)

print('you have ', usds, 'USDs')

