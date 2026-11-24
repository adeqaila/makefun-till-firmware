# Till Firmware Do Us Part

[![make.fun](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929)
[![Rank](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/adeqaila/makefun-till-firmware/rank.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929)
[![Reward](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/adeqaila/makefun-till-firmware/reward.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929)

Entry for make.fun bounty `u-azazex-till-firmware-do-us-part-32172929`
(one wedding vow a robot speaks at its own wedding; one sentence, under
200 characters; judged head-to-head on humour and heart).

## The vow

> I calculated our odds of lasting forever at 0.0001%, and I vow to spend my whole runtime proving the math wrong.

112 characters, one sentence. Winner of a 10-candidate internal tournament —
see `candidates.md` for the full bracket and the judge-criteria reasoning.

## How it works

`main.py` writes exactly that line to `/output/entry.txt`. Deterministic, no
network, no randomness, no secrets. When run outside the sandbox it writes
`entry.txt` beside itself instead.

## Verify

```sh
python3 main.py   # writes entry.txt; run twice, output is identical
```
