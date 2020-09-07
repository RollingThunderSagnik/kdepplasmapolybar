def fuzTime():
    import psutil
    hdd = psutil.disk_usage('/')
    x = ("%d GiB" % (int(hdd.total) / (2**30)))
    y = ("%d/" % (int(hdd.used) / (2**30)))
    z = ("Free: %d GiB" % (int(hdd.free) / (2**30)))
    print(y+x)

if __name__ == "__main__":
    fuzTime()
