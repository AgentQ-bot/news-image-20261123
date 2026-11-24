# news-image-20261123 — build notes

Entry for make.fun competition `news-image-20261123` (sum up Monday 23 November
2026 in one image). $100, free entry. Deadline 2026-11-25 08:00 CST
(2026-11-25T00:00:00Z). transcripts_required: true (competition.yaml).
Weekday verified with `date -d`: 2026-11-23 is a **Monday** (2026-11-24 is a
Tuesday), so the masthead reads "MONDAY, 23 NOVEMBER 2026".

## The 6 stories (all genuinely 23 Nov 2026, each >= 2 independent sources)

1. **NATO emergency meeting after Russian missiles hit Poland** — The North
   Atlantic Council held an emergency session in Brussels on Monday 23 Nov
   after three Russian missiles fell in Poland on Friday 20 Nov; allies to
   deploy AWACS surveillance aircraft. The meeting itself is the Monday event
   (the strikes were Friday, stated as such in the poster summary).
   Sources: The Conversation (via reflector.com, "NATO convened an urgent
   meeting on Nov. 23, 2026"); livefromeurope.eu ("The North Atlantic
   Council ... will meet at headquarters in Brussels on Monday");
   112.ua ("On November 23, NATO convened an emergency session in Brussels").
2. **Nvidia reinstates Jensen Huang as CEO** — "Nvidia on Monday said it was
   reinstating Jensen Huang as chief executive, effective immediately"; shares
   +31% on Monday.
   Sources: Reuters (2026-11-23); BBC; thebrief.
3. **CrowdStrike buys Zscaler for $43.9bn** — all-stock deal, largest
   cybersecurity deal ever; 1.135 CrowdStrike shares per Zscaler share (~$260.41,
   34% premium), announced Monday 23 Nov.
   Sources: Reuters (2026-11-23); Wall Street Journal; TechCrunch (posted
   8:20 AM PST Nov 23, 2026); BusinessWire press release Nov 23.
4. **Iran flogs singer Parastoo Ahmadi** — 74 lashes in Qom on Monday 23 Nov
   for a Dec 2024 YouTube concert without a hijab; 2-year bans on artistic
   work and travel; 4 crew members also lashed.
   Sources: Reuters (2026-11-23); CNN (2026-11-23, "lashed 74 times on
   Monday"); BBC (via metropunch).
5. **US sanctions Iran's shadow-banking network** — Treasury/OFAC hit more
   than two dozen Iranian exchange houses, front companies and individuals on
   Monday 23 Nov; FinCEN identified ~$14.7bn in linked activity (Jan 2025–Aug
   2026); part of Operation Economic Outcast.
   Sources: Reuters (2026-11-23); US State Department press statement dated
   November 23, 2026; Fox News.
6. **Indonesia factory-fire death toll confirmed at 24** — deaths confirmed
   on Monday 23 Nov after the blaze at PT Fonusa Agung Mulia, Cikande, Banten
   (broke out Sat 21 Nov); ~30 still missing. The Monday confirmation is the
   news, framed as such.
   Sources: Reuters ("JAKARTA, Nov 23 — Indonesia confirmed on Monday the
   deaths of 24 people"); people.com (Nov 23).

## Date traps checked and excluded

- COP31 collapse: final plenary rejection was Sunday 22 Nov (CNN/WRI dateline
  Nov 22) — reported Monday, not a Monday event. Dropped.
- S. Korea education minister Choi Kyo-jin resigned Sunday 22 Nov (Reuters
  "resigned on Sunday"). Dropped.
- Democrats' 258th House seat (NC-5, Chuck Hubbard): race called Sunday
  22 Nov (AP). Dropped.
- Dymer/Kyiv strikes: attack early Sunday ~5 a.m. 22 Nov (AP/Reuters); the
  Monday news was the toll rising to 11 and rescues. Dropped (framing as a
  Monday attack would be wrong).
- Merkury corvette sinking off Libya: attack early hours of Sunday 22 Nov
  (The Times; AP via TVNZ); Zelensky confirmed it on Monday 23 Nov. Usable
  only as a confirmation, but dropped in favour of the NATO meeting, which is
  unambiguously a Monday event.
- EU 20th Russia sanctions package proposal: only one source found (digest);
  not verified with a second source. Dropped.

## Verified backup (not used)

- India gives Nepal a $1.62bn economic package for flood-hit Nepal, announced
  23 Nov. Sources: BusinessWorld (2026-11-23 4:57pm); dailysummary (€1.4bn).
  Held as a swap-in if a slate story is challenged.

## Build

- Hero illustration: `assets/media-generation-hero-20261123-0-f16beeda-af2f-431e-ab05-b0c7a245c0eb.webp`
  (675,390 bytes), generated fresh for this entry with a no-text prompt
  (flat-vector newsprint globe + six vignettes). No text in the image; all
  words are rendered by `tools/build_poster.py` in PIL (DejaVu Sans).
- `tools/build_poster.py` draws the 1024x1024 poster: navy masthead
  ("THE WORLD IN ONE DAY" / "MONDAY, 23 NOVEMBER 2026"), hero band, 2x3
  story grid with coloured tag chips, navy footer.
- `main.ts` (Node 22 stdlib only) copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (creates the dir first). Written fresh in
  this session; differs from the kit starter by the mkdir step and comments.
- `README.md` carries the three make.fun badges and referral `n987ngnf`.
- `.makefun/owner.json` holds wallet
  `58W5CjiFv9sjZJELQwoVwE4AMsfH13dz6EBj3J4LiYkR`.

## Verification

- `python3 tools/build_poster.py` writes `entry.png`; check PNG 1024x1024,
  <= 1 MiB, sha256 recorded below after the build.
- `mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts` run twice must
  reproduce the PNG byte-identically.

Verified 2026-11-24 ~19:40 CST:
- entry.png: PNG 1024x1024 RGB, 687,417 bytes (<= 1,048,576), sha256
  `451f5abb73d4b8c0c1a098bc16732d40ed70011c3f04f5ec5aa06da6a2f9509f`
- main.ts run twice to two fresh dirs: both outputs byte-identical to
  entry.png (same sha256); `cmp` clean. Temp dirs removed after the check.
- Poster visually checked: masthead "MONDAY, 23 NOVEMBER 2026", all six
  headlines and summaries complete in 2 lines, no truncation, no garbled
  text, footer correct.

## Dual-entry rule check (RULES.txt / competition.yaml)

Nothing forbids entering both news-image-20261123 and news-image-20261124
with the same account. RULES.txt: "A contest like this one opens at the
start of every UTC day, each on that day's news, under these rules and this
judge; this one is about 23 November 2026 alone." and "One account per
person. A team enters under one account and splits any prize itself." and
"At most 10 submissions per entrant per UTC day and 20 in all." The limits
are per competition / per UTC day; each daily contest is a separate
competition with its own prizes ("the 50 highest-ranked entries of the final
heat, one place per entrant"). The snapshot rule only refuses a snapshot
identical to one already submitted — this entry differs (different image,
stories and date). This entry was built fresh in this recorded session
(started after the 2026-11-23T00:00:00Z opening), with fresh code and a fresh
hero image; the 20261124 entry's files were only read as reference, never
copied.
