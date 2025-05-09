def calculate_average(values):
    return sum(values) / len(values)

readings = [72, 55, 101, 90]
average = calculate_average(readings)
print("Average:", average)
stations = [
    ["A1", 62],
    ["B2", 85],
    ["C3", 47],

]
for station in stations:
    print(f"{station[0]} ==> {station[1]}") def report_status(stations, threshold):
    for station in stations:
        station_id = station[0]
        pm25 = station[1]
        if pm25 < threshold:
            status = "Danger"
        else:
            status = "Safe"
        print(f"{station_id}: {pm25} ==> {status}")
report_status(stations, 100)
