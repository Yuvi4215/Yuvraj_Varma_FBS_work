### bus route and total fare calculation based on location and distance


def getTotalFare(loc, dist, rate):
    distance, flag = 0, True
    size = len(loc)
    start = input("Enter Source Location : ")
    end = input("Enter Destination Location : ")
    if start in loc and end in loc:
        for index in range(0, size):
            if loc[index] == start:
                j = index
                while flag:
                    if loc[j] == end:
                        flag = False
                    else:
                        # print(dist[j])
                        distance += dist[j]
                        j += 1
                    if j == size:
                        j = 0
    return distance * rate


loc = ["s1", "s2", "s3", "s4", "s5", "s6"]
print("Stations : ['s1','s2','s3','s4','s5','s6']")
dist = [1000, 2400, 3800, 1500, 2800, 4900]
rate = float(input("Enter the rate(rupess/meter) : "))
# getTotalFare(loc,dist,rate)
total_fare = getTotalFare(loc, dist, rate)
print(
    f"""
------------------------------------------------      
Total Fare : {total_fare:.2f} ₹
------------------------------------------------"""
)
