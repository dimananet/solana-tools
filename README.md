# solana-tools

## find-stakes

Usage:
```
solana stakes | ./find-stakes.py "Stake Authority=GcibmF4zgb6Vr4bpZZYHGDPZNWiLnBDUHdpJZTsTDvwe" "Withdraw Authority=H2qwtMNNFh6euD3ym4HLgpkbNY6vMdf5aX5bazkU4y8b"
```

You can add as many filters as you need.

Sample for unstaking stakes:
```
solana stakes | ./find-stakes.py "Stake Authority=GcibmF4zgb6Vr4bpZZYHGDPZNWiLnBDUHdpJZTsTDvwe" "Withdraw Authority=H2qwtMNNFh6euD3ym4HLgpkbNY6vMdf5aX5bazkU4y8b" | while read in; do solana deactivate-stake "$in"; done
```
