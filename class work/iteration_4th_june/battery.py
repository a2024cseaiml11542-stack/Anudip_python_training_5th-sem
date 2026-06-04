#prograam for  displaying battery  charging level
charging_level=20
electricity_status= True
while (charging_level<=100):
    if(electricity_status):
        print("Battery level :",charging_level,"%")
        charging_level =charging_level +10
    else:
        print("Electricity is not availaible to the device")
        break

print("Full Charged")
    