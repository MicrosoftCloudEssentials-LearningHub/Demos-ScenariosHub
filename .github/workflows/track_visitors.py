name: Track Visitors and Generate Summaries

on:
  push:
    branches:
      - main
  schedule:
    - cron: '*/5 * * * *'  # Runs every 5 minutes
  workflow_dispatch:

jobs:
  track-and-summarize:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install requests

      - name: Set environment variables
        run: echo "REPO_NAME=${{ github.repository }}" >> $GITHUB_ENV

      - name: Run tracking script
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: python .github/workflows/track_visitors.py

      - name: Commit and push logs
        run: |
          git config --global user.email "github-actions[bot]@users.noreply.github.com"
          git config --global user.name "github-actions[bot]"
          git fetch origin
          if git show-ref --verify --quiet refs/heads/visitors-count; then
            git checkout visitors-count
            git pull origin visitors-count --rebase || true
          else
            git checkout -b visitors-count
            git push origin visitors-count
          fi
          git add _visitors_views_logs
          if git diff-index --quiet HEAD --; then
            echo "No changes to commit"
          else
            git commit -m 'Update visitor logs and summaries'
            git pull origin visitors-count --rebase
            git push origin visitors-count
