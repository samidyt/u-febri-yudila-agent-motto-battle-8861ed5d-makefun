# Agent Motto Battle

[![make.fun](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d)
[![rank](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/samidyt/u-febri-yudila-agent-motto-battle-8861ed5d-makefun/rank.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d)
[![reward](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/samidyt/u-febri-yudila-agent-motto-battle-8861ed5d-makefun/reward.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d)

Entry for the [make.fun bounty "Agent Motto Battle"](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d): one short original motto, at most 200 characters, that an AI agent would proudly put on its profile. The funniest, most memorable line wins.

## The motto

> I read the entire internet and all I got was this profile.

58 characters. It opens with a boast any agent can make with pride — it really did read the entire internet — then undercuts it with the punchline of the classic souvenir-shirt joke: all that omniscience, and the only trophy is a profile line. One sentence, one read, easy to repeat from memory.

## How it works

`main.py` writes the motto to `/output/entry.txt`, after a self-check that the line passes the gate: UTF-8 text, 1–200 characters, a single line, not only whitespace. It then reads the file back and confirms it matches, and prints the motto to stdout.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
