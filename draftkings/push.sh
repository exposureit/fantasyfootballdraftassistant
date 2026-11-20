#!/bin/sh
# Push HEAD to the picks branch on origin (routine sessions may be sitting on an auto-created outcome
# branch, so we never rely on the current branch name). When GITHUB_TOKEN is set, authenticate with it
# through a git credential helper; the token never appears in a command line or in output.
target="${PICKS_BRANCH:-claude/draftkings-nfl-picks-4aiuoj}"
if [ -n "$GITHUB_TOKEN" ]; then
  echo "push.sh: GITHUB_TOKEN present, pushing HEAD to $target with token auth"
  git -c credential.helper= \
      -c credential.helper='!f(){ echo username=x-access-token; echo "password=$GITHUB_TOKEN"; }; f' \
      push origin "HEAD:$target" 2>&1 | sed "s#$GITHUB_TOKEN#REDACTED#g"
else
  echo "push.sh: GITHUB_TOKEN not set, plain push of HEAD to $target"
  git push origin "HEAD:$target"
fi
