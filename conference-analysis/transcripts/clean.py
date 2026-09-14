#!/usr/bin/env python3
"""Clean YouTube auto-caption VTT files: strip timestamps, dedupe rolling captions."""
import re, sys, glob, os

def clean_vtt(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    lines_out = []
    for block in text.split("\n\n"):
        blines = block.strip().splitlines()
        # keep only cue body lines (after the timestamp line)
        for i, l in enumerate(blines):
            if "-->" in l:
                body = blines[i + 1:]
                # rolling captions: the last line of the body is the newest segment
                if body:
                    seg = body[-1]
                    seg = re.sub(r"<[^>]+>", "", seg).strip()
                    if seg and (not lines_out or lines_out[-1] != seg):
                        lines_out.append(seg)
                break
    return " ".join(lines_out)

for vtt in glob.glob("*.en.vtt"):
    base = os.path.basename(vtt)[:-len(".en.vtt")]
    out = os.path.join("txt", base + ".txt")
    with open(out, "w", encoding="utf-8") as f:
        f.write(clean_vtt(vtt) + "\n")
    print(f"ok: {base[:60]}")