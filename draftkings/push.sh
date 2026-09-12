#!/bin/sh
# Push the current branch to origin. When GITHUB_TOKEN is set, authenticate with it through a
# git credential helper (the token never appears in a command line or in output). Otherwise plain push.
branch=$(git branch --show-current)
if [ -n "$GITHUB_TOKEN" ]; then
  echo "push.sh: GITHUB_TOKEN present, pushing $branch with token auth"
  git -c credential.helper= \
      -c credential.helper='!f(){ echo username=x-access-token; echo "password=$GITHUB_TOKEN"; }; f' \
      push origin "$branch" 2>&1 | sed "s#$GITHUB_TOKEN#REDACTED#g"
  exit "${PIPESTATUS:-$?}"
else
  echo "push.sh: GITHUB_TOKEN not set, plain push of $branch"
  git push origin "$branch"
fi
