from threading import Thread


results = [0, 0, 0, 0]

def sum_of_squares(start, end, index):
    total = 0
    for i in range(start, end + 1):
        total += i * i
    results[index] = total

if __name__=="__main__":
    threads = []
    ranges = [(1, 25), (26, 50), (51, 75), (76, 100)]

    for idx, (start, end) in enumerate(ranges):
        t = Thread(target=sum_of_squares, args=(start, end, idx))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Sum of squares from 1 to 100 =", sum(results))
