import argparse
import calendar
import datetime
import getpass
import json
import requests


def get_opt():
    pr = argparse.ArgumentParser(description="GitHub PR")
    pr.add_argument("-v", dest="version", action="version",
                    version="%(prog)s beta")
    pr.add_argument("-n", dest="number", action="store_true",
                    default=False, help="Days are open")
    pr.add_argument("-c", dest="Odtime", action="store_true",
                    default=False, help="Opened/closed in a day")
    pr.add_argument("-o", dest="openus", action="store_true",
                    default=False, help="Who opened")
    pr.add_argument("-l", dest="labels", action="store_true",
                    default=False, help="Attached labels")
    pr.add_argument("-a", dest="adddel", action="store_true",
                    default=False, help="Added and deleted lines")
    pr.add_argument("-u", dest="user", type=str,
                    required=True, help="GitHub login")
    pr.add_argument("-r", dest="repo", type=str,
                    required=True, help="GitHub repo")
    args = pr.parse_args().__dict__
    args["login"] = input("Login: ")
    args["password"] = getpass.getpass()
    dic = requests.get("https://api.github.com/repos/%s/%s/pulls?page="
                       "1&per_page=100" % (args["user"], args["repo"]),
                       auth=(args["login"], args["password"])).json()
    tmp = json.dumps(dic)
    with open('log.json', "w") as logfile:
        logfile.write(tmp)
    return args, dic


def number(dic):
    t = datetime.datetime.now().date()
    for i in dic:
        title = i["title"]
        d = datetime.datetime.strptime(i["created_at"], "%Y-%m-%dT%H:%M:"
                                                        "%SZ").date()
        r = t - d
        print("PR {0} is opened {1} days".format(title, r.days))


def opened_dt(dic):
    for i in dic:
        title = i["title"]
        do = datetime.datetime.strptime(i["created_at"], "%Y-%m-%dT%H:%M:"
                                                         "%SZ")
        dt = datetime.datetime.strptime(i["created_at"], "%Y-%m-%dT%H:%M:"
                                                         "%SZ").time()
        dayo = calendar.day_name[do.weekday()]
        print("PR {0} was opened on {1}, {2}".format(title, dayo, dt))


def openperiod(dic):
    for i in dic:
        name = i["user"]["login"]
        title = i["title"]
        print("PR {0} was opened by user {1}".format(title, name))


def label(dic):
    for i in dic:
        labe = i["label"]
        title = i["title"]
        print("PR {0} label {1}".format(title, labe))


def lineadd_del(args, dic):
    for i in dic:
        num = str(i["number"])
        lin = requests.get("https://api.github.com/repos/%s/%s/pulls/"
                           "%s?page=1&per_page=100" %
                           (args["user"], args["repo"], num),
                           auth=(args["login"], args["password"])).json()
        print("Number of lines {0}: ADD {1} DEL {2}".format(i["title"],
                                                            lin["additions"],
                                                            lin["deletions"]))


def prog():
    arguments, result = get_opt()
    if arguments["number"]:
        number(result)
    elif arguments["Odtime"]:
        opened_dt(result)
    elif arguments["openus"]:
        openperiod(result)
    elif arguments["labels"]:
        label(result)
    elif arguments["adddel"]:
        lineadd_del(arguments, result)
    else:
        print("No arguments")


prog()
