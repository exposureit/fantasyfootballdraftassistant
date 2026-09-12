#!/bin/sh
# Push the current branch to origin. Uses GITHUB_TOKEN when present (routine sessions
# have no repo push credentials of their own). Never prints the token.
set -e
branch=$(git branch --show-current)
if [ -n "$GITHUB_TOKEN" ]; then
  auth=$(printf 'x-access-token:%s' "$GITHUB_TOKEN" | base64 | tr -d '\n')
  git -c "http.https://github.com/.extraheader=AUTHORIZATION: basic $auth" push origin "$branch" 2>&1 | sed "s#$GITHUB_TOKEN#REDACTED#g"
else
  git push origin "$branch"
fi
