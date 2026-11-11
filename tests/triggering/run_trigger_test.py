#!/usr/bin/env python3
"""Trigger-firing test runner for the under50 skill.

Method: "A Session-Start Hook Raised Claude Code Skill Firing From 15% to 62%"
(Towards Data Science, 2026-11-10). One `claude -p` call per run in a throwaway
git repo holding only the skill; score the agent's FIRST tool call: a run fires
when the first call loads the skill. Stdlib only.

Usage:
  python3 run_trigger_test.py --model sonnet --runs 3
  python3 run_trigger_test.py --model haiku --model sonnet --model opus --runs 3 \
      --skill-path /path/to/other/SKILL.md   # e.g. previous description, to compare

Requires: Claude Code CLI (`claude`) on PATH, with usage billing. In the
original experiment a run cost about 2 cents; 144 runs (16 prompts x 3 runs
x 3 models) took 3-4 minutes with four in parallel and cost about $3.
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time

# Env vars a parent Claude Code session sets; the original runner stripped nine.
def stripped_env():
    drop_prefixes = ("CLAUDE_CODE", "CLAUDECODE")
    drop_exact = {"CLAUDE_EFFORT", "CLAUDE_CODE_SESSION_ID"}
    return {k: v for k, v in os.environ.items()
            if k not in drop_exact and not k.startswith(drop_prefixes)}


def first_action(prompt, model, workspace):
    """Return the skill or tool the agent calls first, or None for a text-only answer."""
    cmd = ["claude", "-p", "--model", model, "--max-turns", "1",
           "--setting-sources", "project", "--strict-mcp-config",
           "--no-session-persistence",
           "--output-format", "stream-json", "--verbose", prompt]
    env = stripped_env()
    proc = subprocess.Popen(cmd, cwd=workspace, env=env, stdin=subprocess.DEVNULL,
                            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
    try:
        for line in proc.stdout:
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            if event.get("type") == "result":
                if event.get("subtype") != "success":
                    raise RuntimeError("run failed")  # the runner retries it
                return None  # text-only reply
            if event.get("type") == "assistant":
                for block in event["message"]["content"]:
                    if block["type"] == "tool_use":
                        tool = block["name"]
                        return block["input"].get("skill") if tool == "Skill" else tool
        raise RuntimeError("no tool call or result")  # the runner retries it
    finally:
        proc.kill()  # stop before the tool runs


def build_workspace(skill_path, skill_name):
    """Throwaway git repo holding only the skill under .claude/skills/."""
    ws = tempfile.mkdtemp(prefix="trigger-test-")
    subprocess.run(["git", "init", "-q"], cwd=ws, check=True)
    dest = os.path.join(ws, ".claude", "skills", skill_name)
    os.makedirs(dest)
    shutil.copy(skill_path, os.path.join(dest, "SKILL.md"))
    return ws


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", action="append", default=None,
                    help="Model to test (repeatable). Default: sonnet.")
    ap.add_argument("--runs", type=int, default=3, help="Repetitions per prompt per model.")
    ap.add_argument("--skill-path", default=os.path.join(os.path.dirname(__file__), "..", "..", "SKILL.md"),
                    help="SKILL.md under test (point at an older copy to compare descriptions).")
    ap.add_argument("--skill-name", default="under50")
    ap.add_argument("--prompts", default=os.path.join(os.path.dirname(__file__), "prompts.json"))
    ap.add_argument("--out", default="trigger_results.jsonl")
    ap.add_argument("--retries", type=int, default=2)
    args = ap.parse_args()

    models = args.model or ["sonnet"]
    spec = json.load(open(args.prompts))
    ws = build_workspace(os.path.abspath(args.skill_path), args.skill_name)
    print("workspace:", ws)

    results = []
    with open(args.out, "a") as fh:
        for model in models:
            for cls, prompts in spec["classes"].items():
                for prompt in prompts:
                    for rep in range(1, args.runs + 1):
                        action, err = None, None
                        for attempt in range(args.retries + 1):
                            try:
                                action = first_action(prompt, model, ws)
                                break
                            except RuntimeError as e:
                                err = str(e)
                                time.sleep(2)
                        rec = {"model": model, "class": cls, "prompt": prompt,
                               "rep": rep, "first_action": action, "error": err}
                        results.append(rec)
                        fh.write(json.dumps(rec) + "\n")
                        fh.flush()
                        fired = action is not None and args.skill_name in str(action)
                        print(f"{model:8s} {cls:10s} rep{rep} -> {action!r}{' FIRED' if fired else ''}{' ERR:' + err if err else ''}")

    print("\n== fire rate (first tool call loads the skill) ==")
    for model in models:
        for cls in spec["classes"]:
            sub = [r for r in results if r["model"] == model and r["class"] == cls]
            fired = sum(1 for r in sub if r["first_action"] and args.skill_name in str(r["first_action"]))
            print(f"{model:8s} {cls:10s} {fired}/{len(sub)}")


if __name__ == "__main__":
    sys.exit(main())
