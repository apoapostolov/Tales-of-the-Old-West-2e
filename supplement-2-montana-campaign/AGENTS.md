# Supplement 2 Agents Guide

This file defines how work inside `supplement-2-montana-campaign/` is organized.

## Purpose

This directory is building a full book-length sandbox supplement for _Tales of the Old West 2e_ set in Montana Territory in `1873`.

The supplement has two different kinds of files:

- final manuscript content
- research, planning, and production scaffolding

Do not mix them.

## Directory Rules

### `book-content/`

This folder is for final book manuscript text only.

Rules:

- chapter-facing prose goes here
- file names should be book-order numeric, for example `00-welcome-to-montana.md`
- prose should be publication-facing, not planning-facing
- no checklists, TODOs, or rough research notes in this folder
- any in-progress manuscript chapter that is meant to survive into the book belongs here

### `research/`

This folder is for research, audits, structure notes, historical analysis, web source ledgers, and scenario design notes.

Rules:

- planning documents stay here
- source collection stays here
- chapter analysis and product architecture stay here
- if a file explains how to write a chapter rather than being the chapter, it belongs here

### `villages/`

This folder is for settlement templates, settlement planning, and pre-manuscript town scaffolds.

Rules:

- templates and indices stay here
- rough town skeletons stay here until promoted to full manuscript
- once a settlement becomes finished book prose, move or rewrite it into `book-content/`

### `factions/`

This folder is for faction design, presence matrices, and faction planning notes.

### `outlaw-bands/`

This folder is for outlaw-band planning, ledgers, and development notes.

## Writing Standard

When writing manuscript prose for this supplement:

- follow the `western-writing` skill guidance
- keep chronology locked to `1873`
- distinguish verified history from plausible synthesis and fictionalized table content
- preserve the gritty, concrete, non-generic prose register used elsewhere in the repo
- avoid planning language in manuscript files

## Structural Standard

The Montana supplement should mirror the usability of the New Mexico campaign chapter, but at full-book scale.

Core principle:

- `book-content/` is the book
- everything else exists to support the book

## Immediate Conventions

- the current opening chapter is [book-content/00-welcome-to-montana.md](/mnt/c/git-public/Tales-of-the-Old-West-2e/supplement-2-montana-campaign/book-content/00-welcome-to-montana.md)
- the former root-level manuscript file should not be used as the primary book file any longer
- future final chapters should be added under `book-content/` in sequence
