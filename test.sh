#!/bin/sh

MOD_BRANCH="main"

git checkout --orphan latest_branch
git add -A
git commit -m "Initial commit"
git branch -D "$MOD_BRANCH"
git branch -m latest_branch "$MOD_BRANCH"
git push -u origin "$MOD_BRANCH" -f