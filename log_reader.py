#! /usr/bin/python3

from datetime import datetime 

def main():
    arr = []

    with open('log_param02.txt') as f:
        for lini in f:
            l = lini.strip().replace(',','.').split(';')
            l[0] = l[0].replace('\ufeff', '')

            if len(l[0])<16:
                l[0] = f'{l[0][0:11]}0{l[0][11:]}'

            log = {
                    "date":datetime.strptime(l[0], "%d.%m.%Y %H:%M"),
                    "line":int(l[1]) + 1,
                    "temprature_inlet":float(l[2]),
                    "pressure_pump":float(l[3]),
                    "pressure_f1":float(l[4]),
                    "pressure_f2":float(l[5]),
                    "pressure_f3":float(l[6]),
                    "pressure_inlet_RO":float(l[7]),
                    "pressure_RO":float(l[8]),
                    "permeat_flow":float(l[9]),
                    "concentrate_flow":float(l[10]),
                    "conductivity_inlet_RO":float(l[11]),
                    "conductivity_permeat_RO":float(l[12]),
                    "pressure_Din":float(l[13]),
                    "pressure_Cin":float(l[14]),
                    "pressure_Dout":float(l[15]),
                    "flow_Din":float(l[16]),
                    "flow_Cin":float(l[17]),
                    "conductivity_Din":float(l[18]),
                    "temprature_Din":float(l[19]),
                    "temprature_Cin":float(l[20])
            }

            arr.append(log)

    print(arr)


if __name__ == '__main__':
    main()