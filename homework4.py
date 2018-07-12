import CONF
import json
import psutil
import time


class SimpleMonitor(object):
    count = 0

    def __init__(self):
        self.clock = time.strftime("%H:%M:%S")
        self.cpu = str(psutil.cpu_percent())
        self.vmm = str(psutil.virtual_memory().percent)
        self.swm = str(psutil.swap_memory().percent)
        self.ior = str(psutil.disk_io_counters().read_count)
        self.iow = str(psutil.disk_io_counters().write_count)
        self.nbs = str(psutil.net_io_counters().bytes_sent)
        self.nbw = str(psutil.net_io_counters().bytes_recv)
        SimpleMonitor.count += 1

    def outflow(self):
        if CONF.out == "txt":
            self.zapistxt()
        else:
            self.zapisjsn()

    def zapisjsn(self):
        dyson = {'SNAPSHOT': SimpleMonitor.count, 'TIME': self.clock,
                 'CPU load': self.cpu, 'Memory usage': self.vmm,
                 'VMemory usage': self.swm, 'Disk Read Count': self.ior,
                 'Disk Write Count': self.iow, 'Byte sent': self.nbs,
                 'Byte receive': self.nbw}
        outing = "[%s]" % json.dumps(dyson)
        with open('log.json', "a") as logfile:
            logfile.write(outing)
        with open('log.json', 'r') as temp:
            testfile = temp.read()
        with open('log.json', 'w') as temp1:
            temp1.write(testfile.replace("][", ", "))

    def zapistxt(self):
        outing = 'SNAPSHOT: {num}\nTime: {T}\nCPU load: {cp}\n' \
                 'Memory usage: {mu}\nVMemory usage: {vu}\n' \
                 'Disk Read Count: {dr}\nDisk Write Count: {dw}\n' \
                 'Byte sent: {bs}\nByte receive: {br}\n' \
                 '\n'.format(num=SimpleMonitor.count, T=self.clock,
                             cp=self.cpu, mu=self.vmm, vu=self.swm,
                             dr=self.ior, dw=self.iow, bs=self.nbs,
                             br=self.nbw)
        with open('log.txt', "a") as logfile:
            logfile.write(outing)


while True:
    ckl = SimpleMonitor()
    ckl.outflow()
    time.sleep(CONF.interval)
