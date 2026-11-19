# Second brain kit: the SECOND method

The starter kit of the masterclass. One zip file, `second-brain-kit.zip`, holds a small team of
AI agents that works on plain files on your own computer. Unzip it, double-click one file, and
you talk to the team.

Created by **Hanane Dupouy**: https://www.linkedin.com/in/hanane-dupouy/

## What it is for

A second brain is a team of 16 AI agents that knows who you are, listens, remembers, proposes,
writes in your voice and learns from results. **You decide.** No agent publishes, posts or sends
anything: you do.

**The goal is action, not storage.** Capturing, organizing and storing notes is only the start.
You build a second brain to act on what you capture and create every day:

- **Productivity:** the team reads, summarizes, checks and plans, so you spend your time deciding
  instead of searching.
- **Creativity:** what you read and what you already know meet in one memory, and new ideas come
  out of them.
- **New content:** your notes become pieces written in your voice, backed by your sources, ready
  for you to review and publish.

A note that is never used is a cost. This brain is built to turn notes into work that goes out.

The team follows the six steps of the SECOND method. Each step answers one question and has its
own folder of memory.

| Step | The question it answers | The agents |
|---|---|---|
| **S** Self | Who am I, how do I speak, what do I refuse? | Sofia, Sacha, Serena, Sosie |
| **E** Ears | What should reach me? | Emma, Carl |
| **C** Condense | What is worth keeping, and what does it really say? | Chloe, Cato |
| **O** Orient | What do I do next? | Olivia |
| **N** Narrate | How do I say it, in my voice, with proof? | Naomi, Nora, Noah |
| **D** Debrief | What worked, and what do I change? | Dexter, Diane, Diego |

Debrief feeds Self: what you learn goes back into who you are and how you write. Alfred, the
Chief of Staff, routes the work. You talk to him only: he calls the right agent, and he stops
each time a decision is yours.

Four of the agents are reviewers (Sosie, Cato, Nora, Diego). Nobody reviews their own work.

The agents are generic. They say "piece". What a piece is (a post, a status report, a
newsletter) comes from the brain you build. Change the brain and the same team does another job.

## See it before you install it

Two pages show the whole system, with no install:

- **The SECOND Method**, the visual page: the loop of the six steps, the files and agents of each
  step, the journey of one source from capture to a piece, the house rules, what to bring and the
  order to build in.
  https://claude.ai/artifact/Bfg2gmLmCMeR69v9wMqUhY
- **The SECOND Team**: every step and every agent, with what it reads, the exact files it writes,
  who checks it and what it never does. All 31 skills, with a search, and the scripts.
  https://claude.ai/artifact/8nrCyP5SMcPjgcHVQvh1ZK

## What you need

- **Claude Code**, installed and signed in: https://claude.com/claude-code. It needs a Claude
  account that includes Claude Code (a paid plan, or an API account). The kit was tested with
  Claude Code 2.1.323.
- **Python 3**: https://www.python.org. On Windows, tick "Add python.exe to PATH" during the
  install. Nothing else to install: the scripts use the standard library only.
- **A browser**, for the screen. It runs on your computer only, at http://127.0.0.1:8770.
- **About one hour** for the first step (Self), then 15 to 45 minutes for each later step.
- **Your own material**, for the first steps:
  - who you are: your CV or LinkedIn profile, a short bio, 5 to 10 pieces you wrote and like.
  - what you know (optional): your courses, slides, a book chapter, your notes.

No coding needed. You never type a command yourself: Alfred runs them for you.

## Launch it

1. **Download the zip.** In this repository, click `second-brain-kit.zip`, then the download
   button.
2. **Unzip it** in a folder of its own, for example `C:\second-brain\` or `~/second-brain/`.
   Avoid a folder synced by OneDrive or Dropbox: the brain moves folders, and a sync can lock
   them. Inside, you find a folder named `second-brain-kit`. That is your brain. You can rename
   it.
3. **Double-click `Start my brain`**: `Start my brain.bat` on Windows, `Start my brain.command`
   on a Mac. It checks Python and Claude Code, opens the screen in your browser and starts Alfred.
4. **Say yes** when Claude Code asks whether you trust this folder. The permissions of the kit
   only apply after that.
5. **Type `continue`.** Alfred says where you are in the six steps and starts the next thing.

From then on, three things are enough:

1. Double-click `Start my brain`.
2. Type `continue` to Alfred.
3. Answer `approve`, or `change:` followed by what to change. In Alfred's window, or on the screen.

Everything is saved in the files. You can stop after any step and come back tomorrow.

**If the launcher is blocked:**
- Windows may show "Windows protected your PC": click "More info", then "Run anyway".
- macOS may refuse a file downloaded from the internet: right-click `Start my brain.command`,
  "Open", then "Open" again.
- From a terminal opened in the folder, the same two things:
  `python .claude/skills/mission-control/scripts/serve.py --open` (the screen), then
  `claude --agent alfred` (Alfred).

## Where to find the docs inside the zip

Once unzipped, everything is in the folder `second-brain-kit/`.

| File | Read it when |
|---|---|
| `docs/STEP-BY-STEP.md` | **Start here if you are not a coder.** From zero, every click: install, the two folders to fill, then each of the six steps with what you should see and what to answer |
| `docs/build-guide.html` | The same six steps, Self to Debrief, as a page to open in your browser, with the prompts to copy |
| `docs/START-YOUR-OWN.md` | You are at ease with a terminal: from the zip to a brain that is yours, starting with the example brain |
| `README.md` | The full map: the method, the folders, the routines, the screen, the brains, the tools |
| `CLAUDE.md` | The one-page constitution every agent reads: the method and the seven house rules |
| `my-documents/README.md` | What to drop in `my-documents/`: who you are. Read at Step S |
| `my-knowledge/README.md` | What to drop in `my-knowledge/`: what you know. Filed at Step E, with your yes |

The rest of the folder is the system itself:

```
.claude/agents/     the team, one file per agent
.claude/skills/     the know-how, 31 skills
ops/tools/          small Python scripts, no AI inside
brains/_template/   an empty brain, with one guiding line per file
brains/project-manager/  an example brain: a fictional project manager, meeting notes in, a status report out
```

## A good first hour

1. Try the example first (15 minutes). Say to Alfred: `Switch to the brain project-manager.`, then
   `Alfred, run the production line on the three meeting notes of week 46: one status report.`
   Watch the screen while the agents work, one after the other.
2. Then build your own. Fill `my-documents/`, type `/build-self`, and answer Sofia's questions.
   The Self step ends with a test: Sosie writes three short pieces as you, and says what your
   files failed to tell her.
3. Go on with `/build-ears`, `/build-condense`, `/build-orient`, `/build-narrate` and
   `/build-debrief`, in that order, or just type `continue`.

## Good to know

- **Your files stay on your computer.** The brain is plain markdown files in the folder. The
  agents run through Claude Code, with your own account.
- **Nothing is sent or published.** The team proposes, you decide and you post.
- **Your brain is yours.** The kit holds no real person's brain: only the empty template and the
  fictional example.
- **The network** is used by Claude Code, and by two tools you launch yourself: the daily radar
  (up to three sources you choose) and the download of one page or paper.

## Credit

**CREDIT TO HANANE DUPOUY.** The SECOND method, the team of agents and this kit were designed
and built by Hanane Dupouy.

LinkedIn: https://www.linkedin.com/in/hanane-dupouy/

If you use, share or adapt this kit, please keep this credit and link back to this page.

## Licence

This folder is licensed under **CC BY-NC 4.0** (Creative Commons Attribution-NonCommercial 4.0
International), not under the MIT licence of the rest of the repository. See `LICENSE` in this
folder.

- **You may** share, reuse and adapt the kit.
- **You must** credit Hanane Dupouy, link to the licence, and say if you changed something.
- **You may not** use it for commercial purposes. For a commercial use, ask the author first.
