#!/bin/bash
git add .
commitMessage="$*"
git commit -m "$commitMessage"
git push
