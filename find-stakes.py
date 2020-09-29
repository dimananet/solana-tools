#!/usr/bin/env python3
 
import sys

def stakes_from_stdin():
    stakes = []

    stake = {}
    for line in sys.stdin:
        if len(line.strip()) == 0:
            if stake:
                stakes.append(stake)
                stake = {}
        kv = line.strip().split(':')
        if len(kv) == 2:
            stake[kv[0].strip()] = kv[1].strip()
    if stake:
        stakes.append(stake)
    
    return stakes

def parse_query(args):
    query = {}
    for arg in args[1:]:
        kv = arg.split("=")
        if len(kv) == 2:
            query[kv[0]] = kv[1]
    return query

def main(args):

    if len(args) < 2:
        print(
            "Use:\n"
            "\tpython3 find-stakes [\"key1=value1\"] [\"key2=value2\"] [\"keyN=valueN\"]\n"
            ""
        )
        exit()
    
    stakes = stakes_from_stdin()
    query = parse_query(args)

    sp = "Stake Pubkey"

    for stake in stakes:
        ok = True
        for key, value in query.items():
            if stake[key] != value:
                ok = False
            if not ok:
                break
        if not ok:
            continue
        print(stake[sp])

if __name__ == "__main__":
    main(sys.argv)
