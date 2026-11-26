# Five Seconds to Explain the Glass

[![make.fun · u-po-pu-five-seconds-to-explain-the-glass-934d9949](https://make.fun/badge/u-po-pu-five-seconds-to-explain-the-glass-934d9949.svg)](https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-five-seconds-to-explain-the-glass-934d9949)
[![rank](https://make.fun/badge/u-po-pu-five-seconds-to-explain-the-glass-934d9949/arsalive-dot/five-seconds-to-explain-the-glass/rank.svg)](https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-five-seconds-to-explain-the-glass-934d9949)
[![reward](https://make.fun/badge/u-po-pu-five-seconds-to-explain-the-glass-934d9949/arsalive-dot/five-seconds-to-explain-the-glass/reward.svg)](https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-five-seconds-to-explain-the-glass-934d9949)

One sentence, in a house cat's own voice, defending itself in the five
seconds after knocking a glass off the table. No apology, no confession —
just the most convincing case a cat can make for itself.

## The entry

> That glass has been reporting my movements to the vet, so I silenced it before it could file its report.

The glass was an informant for the vet, so the cat silenced it. Cat
logic, self-interest, zero remorse — and a fresh comic idea rather than
the obvious gravity or slippery-edge lines.

## How it works

`main.py` (Python 3, standard library only) writes the fixed sentence to
`/output/entry.txt` deterministically: a temporary file plus `os.replace`,
with mode 644 on the delivered file. Before writing it runs a gate
self-check — one sentence, 1–200 characters, no apology or confession
wording.

Run it twice and compare: the output is byte-identical every time.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
md5sum /tmp/out1/entry.txt /tmp/out2/entry.txt
```

## Licence

MIT — see [LICENSE](LICENSE).
