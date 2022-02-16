import xlrd
import subprocess
import time



def date_converter(cell):
    if isinstance(cell, str):
        return cell
    else:
        conver = str(xlrd.xldate_as_datetime(cell, workbook.datemode)).split(" ")[1].split(":")
        conver2 = str(conver[0] + ":" + conver[1])
        return conver2


workbook = xlrd.open_workbook('Schedule.xls')
worksheet = workbook.sheet_by_index(0)
data = [[worksheet.cell_value(r, c) for c in range(worksheet.ncols)] for r in range(worksheet.nrows)]

Zoom_Room = str(data[0][1]).split(".")[0]

# Sunday Schedule:
Sun1 = date_converter(data[2][1])
Sun2 = date_converter(data[4][1])
Sun3 = date_converter(data[6][1])
Sun4 = date_converter(data[8][1])
Sun5 = date_converter(data[10][1])
Sun6 = date_converter(data[12][1])
Sun7 = date_converter(data[14][1])
SunK1 = date_converter(data[3][1])
SunK2 = date_converter(data[5][1])
SunK3 = date_converter(data[7][1])
SunK4 = date_converter(data[9][1])
SunK5 = date_converter(data[11][1])
SunK6 = date_converter(data[13][1])
SunK7 = date_converter(data[15][1])

# Monday Schedule:
Mon1 = date_converter(data[2][2])
Mon2 = date_converter(data[4][2])
Mon3 = date_converter(data[6][2])
Mon4 = date_converter(data[8][2])
Mon5 = date_converter(data[10][2])
Mon6 = date_converter(data[12][2])
Mon7 = date_converter(data[14][2])
MonK1 = date_converter(data[3][2])
MonK2 = date_converter(data[5][2])
MonK3 = date_converter(data[7][2])
MonK4 = date_converter(data[9][2])
MonK5 = date_converter(data[11][2])
MonK6 = date_converter(data[13][2])
MonK7 = date_converter(data[15][2])

# Tuesday Schedule:
Tue1 = date_converter(data[2][3])
Tue2 = date_converter(data[4][3])
Tue3 = date_converter(data[6][3])
Tue4 = date_converter(data[8][3])
Tue5 = date_converter(data[10][3])
Tue6 = date_converter(data[12][3])
Tue7 = date_converter(data[14][3])
TueK1 = date_converter(data[3][3])
TueK2 = date_converter(data[5][3])
TueK3 = date_converter(data[7][3])
TueK4 = date_converter(data[9][3])
TueK5 = date_converter(data[11][3])
TueK6 = date_converter(data[13][3])
TueK7 = date_converter(data[15][3])


# Wednesday Schedule:
Wed1 = date_converter(data[2][4])
Wed2 = date_converter(data[4][4])
Wed3 = date_converter(data[6][4])
Wed4 = date_converter(data[8][4])
Wed5 = date_converter(data[10][4])
Wed6 = date_converter(data[12][4])
Wed7 = date_converter(data[14][4])
WedK1 = date_converter(data[3][4])
WedK2 = date_converter(data[5][4])
WedK3 = date_converter(data[7][4])
WedK4 = date_converter(data[9][4])
WedK5 = date_converter(data[11][4])
WedK6 = date_converter(data[13][4])
WedK7 = date_converter(data[15][4])

# Thursday Schedule:
Thu1 = date_converter(data[2][5])
Thu2 = date_converter(data[4][5])
Thu3 = date_converter(data[6][5])
Thu4 = date_converter(data[8][5])
Thu5 = date_converter(data[10][5])
Thu6 = date_converter(data[12][5])
Thu7 = date_converter(data[14][5])
ThuK1 = date_converter(data[3][5])
ThuK2 = date_converter(data[5][5])
ThuK3 = date_converter(data[7][5])
ThuK4 = date_converter(data[9][5])
ThuK5 = date_converter(data[11][5])
ThuK6 = date_converter(data[13][5])
ThuK7 = date_converter(data[15][5])

# Friday Schedule:
Fri1 = date_converter(data[2][6])
Fri2 = date_converter(data[4][6])
Fri3 = date_converter(data[6][6])
Fri4 = date_converter(data[8][6])
Fri5 = date_converter(data[10][6])
Fri6 = date_converter(data[12][6])
Fri7 = date_converter(data[14][6])
FriK1 = date_converter(data[3][6])
FriK2 = date_converter(data[5][6])
FriK3 = date_converter(data[7][6])
FriK4 = date_converter(data[9][6])
FriK5 = date_converter(data[11][6])
FriK6 = date_converter(data[13][6])
FriK7 = date_converter(data[15][6])

# Saturday Schedule:
Sat1 = date_converter(data[2][7])
Sat2 = date_converter(data[4][7])
Sat3 = date_converter(data[6][7])
Sat4 = date_converter(data[8][7])
Sat5 = date_converter(data[10][7])
Sat6 = date_converter(data[12][7])
Sat7 = date_converter(data[14][7])
SatK1 = date_converter(data[3][7])
SatK2 = date_converter(data[5][7])
SatK3 = date_converter(data[7][7])
SatK4 = date_converter(data[9][7])
SatK5 = date_converter(data[11][7])
SatK6 = date_converter(data[13][7])
SatK7 = date_converter(data[15][7])