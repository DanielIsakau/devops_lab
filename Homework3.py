import CONF
import json
import psutil
import time

plus = 1


def count():
    global plus
    res = plus
    plus += 1
    return res


def outflow():
    clock = time.strftime("%H:%M:%S")
    cpu = str(psutil.cpu_percent())
    vmm = str(psutil.virtual_memory().percent)
    swm = str(psutil.swap_memory().percent)
    ior = str(psutil.disk_io_counters().read_count)
    iow = str(psutil.disk_io_counters().write_count)
    nbs = str(psutil.net_io_counters().bytes_sent)
    nbw = str(psutil.net_io_counters().bytes_recv)
    if CONF.out == "txt":
        outing = 'SNAPSHOT: {num}\nTime: {T}\nCPU load: {cp}\n' \
                 'Memory usage: {mu}\nVMemory usage: {vu}\nDisk Read' \
                 'Count: {dr}\nDisk Write Count: {dw}\nByte sent: {bs}\n' \
                 'Byte receive: {br}\n\n'.format(num=count(), T=clock,
                                                 cp=cpu, mu=vmm, vu=swm,
                                                 dr=ior, dw=iow, bs=nbs,
                                                 br=nbw)
        with open('log.txt', "a") as logfile:
            logfile.write(outing)
    else:
        dyson = {'SNAPSHOT': count(), 'TIME': clock, 'CPU load': cpu,
                 'Memory usage': vmm, 'VMemory usage': swm,
                 'Disk Read Count': ior, 'Disk Write Count': iow,
                 'Byte sent': nbs, 'Byte receive': nbw}
        outing = "[%s]" % json.dumps(dyson)
        with open('log.json', "a") as logfile:
            logfile.write(outing)
        with open('log.json', 'r') as temp:
            testfile = temp.read()
        with open('log.json', 'w') as temp1:
            temp1.write(testfile.replace("][", ", "))


while True:
    outflow()
    time.sleep(CONF.interval)
