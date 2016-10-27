#!/usr/bin/env python

import sys
import json
import requests
import hashlib


def hashToNumber(txhash, total):
    result = long(txhash, 16) % total
    return result


def getBlocktxs(blockhash, number, total, startnum):
    url = "https://blockexplorer.com/api/block/" + blockhash
    params = dict()

    resp = requests.get(url=url, params=params, timeout=5)
    data = json.loads(resp.text)
    if "tx" in data:
        if len(data["tx"]) >= number:
            print ("%d Transactions for %d results." % (len(data["tx"]), number))
            for i in range(number):
                txhash=data["tx"][i]
                hashwithtotal = txhash + str(total)
                resulthash = hashlib.sha1(hashwithtotal).hexdigest()
                r = hashToNumber(resulthash , total) + startnum
                print ("result %d is %d" % (i, r))
        else:
            print ("only %d Transactions for %d results." % (len(data["tx"]), number))

    else:
        print "invalid block data"


def main():
    if len(sys.argv) == 5:
        blockhash = sys.argv[1]
        number = sys.argv[2]
        total= sys.argv[3]
        startnum = sys.argv[4]
        getBlocktxs(blockhash, int(number), int(total), int(startnum))
    else:
        print "usage: ./lotteryResult.py blockhash number total startnum"


if __name__ == '__main__':
    main()
