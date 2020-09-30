# solana-tools

## find-stakes

Usage:
```
solana stakes | ./find-stakes.py "key[=value]" ["key2[=value2]"] ... ["keyN[=valueN]"]
```

You can add as many filters as you need.

Unstake all stakes:
```
solana stakes \
 | ./find-stakes.py \
 "Stake Authority=GcibmF4zgb6Vr4bpZZYHGDPZNWiLnBDUHdpJZTsTDvwe" \
 "Withdraw Authority=H2qwtMNNFh6euD3ym4HLgpkbNY6vMdf5aX5bazkU4y8b" \
 | while read in; do solana deactivate-stake "$in"; done
```

Merge undelegated stakes:
```
solana stakes \
 | ./find-stakes.py \
 "Stake Authority=GcibmF4zgb6Vr4bpZZYHGDPZNWiLnBDUHdpJZTsTDvwe" \
 "Withdraw Authority=H2qwtMNNFh6euD3ym4HLgpkbNY6vMdf5aX5bazkU4y8b" \
 "Stake account is undelegated" \
 | while read in; do solana merge-stake C79F5mPVyfkaznEsHDGMGmYqEbquFDFFefjAEYJJPdv8 "$in"; done
```
