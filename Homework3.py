import psutil
import json
import CONF
import time

plus = 1
def count():
    global plus
    res = plus
    plus += 1
    return res


def outtxt():
    cpu = str(psutil.cpu_percent(interval=0.5))
    vmm = str(psutil.virtual_memory().percent)
    swm = str(psutil.swap_memory().percent)
    ior = str(psutil.disk_io_counters().read_count)
    iow = str(psutil.disk_io_counters().write_count)
    nbs = str(psutil.net_io_counters().bytes_sent)
    nbw = str(psutil.net_io_counters().bytes_recv)
    outinfo = ("SNAPSHOT " + str(count()) + "\n" + time.strftime("%H:%M:%S") +
               "\n" + "CPU load " + cpu + "\n" + "Memory usage " + vmm +
               "\n" + "VMemory usage " + swm + "\n" + "Disk Read Count "
               + ior + "\n" + "Disk Write Count " + iow + "\n" +
               "Byte sent " + nbs + "\n" + "Byte receive" + nbw + "\n\n")
    with open('log.txt', "a") as logfile:
        logfile.write(outinfo)


def outjson():
    cpu = str(psutil.cpu_percent(interval=0.5))
    vmm = str(psutil.virtual_memory().percent)
    swm = str(psutil.swap_memory().percent)
    ior = str(psutil.disk_io_counters().read_count)
    iow = str(psutil.disk_io_counters().write_count)
    nbs = str(psutil.net_io_counters().bytes_sent)
    nbw = str(psutil.net_io_counters().bytes_recv)
    djson = dict()
    djson["SNAPSHOT"] = count()
    djson["TIME"] = time.strftime("%H:%M:%S")
    djson["CPU load"] = cpu
    djson["Memory usage"] = vmm
    djson["VMemory usage"] = swm
    djson["Disk Read Count"] = ior
    djson["Disk Write Count"] = iow
    djson["Byte sent "] = nbs
    djson["Byte receive"] = nbw
    outinfo = "[" + json.dumps(djson) + "]"
    with open('log.json', "a") as logfile:
        logfile.write(outinfo)
    replace()


def replace():
    file = open('log.json', 'r')
    text = file.read()
    file.close()
    file = open('log.json', 'w')
    file.write(text.replace("][", " ,"))
    file.close()


def writelog():
    while True:
        if CONF.out == "txt":
            outtxt()
            time.sleep(CONF.interval)
        else:
            outjson()
            time.sleep(CONF.interval)


writelog()
