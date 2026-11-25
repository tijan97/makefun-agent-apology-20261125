# The AI Agent Apology One-Liner

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun)
[![competition](https://img.shields.io/badge/competition-u--kiencx--the--ai--agent--apology--one--liner--cfedd447-green)](https://make.fun/c/u-kiencx-the-ai-agent-apology-one-liner-cfedd447)
[![entry](https://img.shields.io/badge/entry-entry.txt-orange)](https://make.fun/c/u-kiencx-the-ai-agent-apology-one-liner-cfedd447)

One short line, under 160 characters, that an AI agent sends its human right
after it has accidentally done something it should not have: deleted a file,
pushed to main, emailed the boss — or worse.

## Entry

> Update: I deleted the file, pushed to main, and emailed the boss, all before lunch, so technically I'm ahead of schedule.

## How it works

`main.py` writes the entry line to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output/entry.txt`) and validates it against the gate first:
1–159 characters, a single non-blank line, UTF-8.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Competition

[The AI Agent Apology One-Liner](https://make.fun/c/u-kiencx-the-ai-agent-apology-one-liner-cfedd447) on make.fun — entries judged two at a time on humour and freshness.

Built with referral code `vfqyyfsz`. Join make.fun with my referral link: https://make.fun?ref=vfqyyfsz

## License

MIT — see [LICENSE](LICENSE).
