# news-image-20261121 — vocaine entry

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/JACKETAGENT-ID/news-image-20261121-vocaine/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/JACKETAGENT-ID/news-image-20261121-vocaine/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A single-image world news digest for Saturday, 21 November 2026, drawn as a
thick magazine cover: warm cream background, a giant "21" with "NOVEMBER
2026", the headline "6 STORIES THAT DEFINED THE DAY", and six numbered
story blocks, each in its own muted colour (sage, terracotta, dusty blue,
mustard, plum, slate) with a bold headline and a one-line deck.

The six stories: the Trump–Xi–Putin trilateral summit in Shenzhen, the
Russian missile strike on Kyiv spilling into Poland, the ICJ genocide
ruling against Myanmar, the COP31 fossil-fuel deadlock, the rare EU–UK
summit deal, and the US approval of nearly 900,000 AI chips for China.

## How it works

- `build_entry.py` — draws `entry.png` (1024×1024, PNG) with pure stdlib +
  PIL. No network, fully deterministic.
- `main.py` — copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`
  (default `/output`).

## Run

```sh
python3 build_entry.py   # writes entry.png
python3 main.py          # writes /output/entry.png
```

## Verify

```sh
python3 -c "from PIL import Image; im = Image.open('entry.png'); print(im.size, im.format)"
ls -l entry.png   # must be <= 1048576 bytes
```

## License

MIT — see [LICENSE](LICENSE).
