# CohortX Post-Competition Release Watch - 2026-07-16

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Checked at: 2026-07-16 16:50 BRT
- Competition open: false
- Deadline: 2026-07-16 11:59 UTC / 08:59 BRT
- JV public result currently visible: #10, `0.43713`
- Best JV submission: `v832_v715_med_drop_d15.csv`

## What Is Visible Now

- Kaggle leaderboard still exposes the same public-score table via CLI.
- JV is shown as #10 with public score `0.43713`.
- #9 remains `Md Raihan` at `0.43741`; public gap is `0.00028`.
- `kaggle competitions submissions` still has empty `privateScore` values for all JV submissions.
- Public notebooks remain unchanged: 4 listed, no new or updated notebook.
- Competition files remain only the original files: `Task_3.xlsx` and `mimic-iv_icd-10_dict.xlsx`.
- Discussions remain unchanged: 2 topics, latest update `2026-06-12T08:11:23.300Z`.

## What Is Not Yet Released

- No private leaderboard or private score is visible through the Kaggle CLI.
- No winner code, writeup, paper, or post-competition notebook is visible.
- No new Kaggle dataset/file package has been released.
- GitHub/web search did not find public solution repositories for the exact competition.

## Absorbable Insights Already Available From Our Final Window

- Best public move: remove `D15` family from `Enlarged Mediastinum` on top of the `v715`
  anchor, producing `0.43713`.
- Other positive removals: `Q34`, non-mediastinal `Q34` children, `C78`, and `D38`.
- Negative removals: `C38`, `J85`, and core `J98` branches should stay in public-facing
  candidates.
- C39 overlays on old broad ASSOC composites were negative; do not combine C39 with the
  old high-volume ASSOC maps without a separate private rationale.

## Monitor Next

1. Recheck Kaggle leaderboard for `privateScore` / final ranking after organizer release.
2. Recheck discussions for winner posts or organizer clarification.
3. Recheck public notebooks sorted by recent run.
4. Search GitHub again for exact-title/code releases.
