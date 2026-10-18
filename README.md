# Dhyey Radadia portfolio — GitHub Pages

This is a standalone public export of the existing portfolio. It retains its design, content, photographs, gallery controls, contact links, and PDF/Word résumé downloads. No build tools or backend are required.

## What is included

- `site/`: the exact public website assets, plus `.nojekyll` and a `/resume/` compatibility page.
- `.github/workflows/pages.yml`: deploys only `site/` on pushes to `main`, or by manual run.
- `scripts/check_site.py`: checks links, anchors, required files, symlinks, and common credential patterns.
- `.gitignore`: excludes local configuration and common credential files.

The original Sites `.git` history, `.openai` configuration, scripts with local paths, activity source records, medical documents, QA files, and deployment archives were not copied. There are no API keys or credentials required. The workflow uses GitHub's automatic, short-lived token and OIDC permissions. Do not create a personal access token secret for this workflow.

Your existing public content, including your contact details, photos, background, and downloadable résumé, is intentionally retained. Google Fonts still loads from Google, just as on the existing site.

## Publish at dhyeyradadia.github.io

The GitHub account must be named `dhyeyradadia` to get this exact free address. A different username produces a different username.github.io address.

1. Sign in to that GitHub account.
2. Create a **public** repository named **dhyeyradadia.github.io**. For the commands below, leave it empty: do not initialize a README, license, or gitignore on GitHub.
3. Open a terminal in this exported folder (not the original `dhyey-portfolio` folder):

```sh
cd "/Users/dhyeyradadia/Documents/Codex/2026-09-30/give-me-some-ideas-on-who/dhyeyradadia.github.io"
git init -b main
git add .gitignore README.md .github/workflows/pages.yml scripts/check_site.py site/
git diff --cached --stat
git commit -m "Prepare portfolio for GitHub Pages"
git remote add origin https://github.com/dhyeyradadia/dhyeyradadia.github.io.git
git push -u origin main
```

Use GitHub's browser/credential-manager sign-in or GitHub CLI authentication if prompted. Never put tokens in a remote URL or commit them in files. If Git asks for author information, set your chosen Git author name and email in this repository first.

4. In the repository, go to **Settings → Pages → Build and deployment → Source → GitHub Actions**. Leave **Custom domain blank**. No purchased domain, DNS setup, or CNAME file is needed for github.io.
5. Open **Actions → Deploy portfolio to GitHub Pages → Run workflow → main**. This also retries the initial push if it ran before Pages was enabled.
6. When the deployment succeeds, visit **https://dhyeyradadia.github.io/**. GitHub may take a few minutes to serve it.

If the repository already contains work, clone it and copy these export files into that checkout instead; review the changes and push normally. Do not force-push or overwrite existing work.

## Check and preview locally

```sh
python3 scripts/check_site.py
python3 -m http.server 8080 --directory site
```

Open http://localhost:8080/ and http://localhost:8080/resume/. Stop the server with Ctrl+C. The `/resume/` copy uses a relative base URL so links and downloads still resolve at the root. `/resume.html` remains supported too. GitHub redirects `/resume` to `/resume/` when serving the directory.

## Later updates

Edit the files in `site/`, run the checker, and commit/push to `main`. If you edit `site/resume.html`, regenerate the directory copy:

```sh
python3 -c 'from pathlib import Path; p=Path("site/resume.html"); Path("site/resume/index.html").write_text(p.read_text().replace("<head>", "<head><base href=\"../\">", 1))'
```

Do not replace this repository with the entire old project directory or its Git history. Only copy intentionally public assets. A workflow checks for common mistakes, but cannot guarantee detection of every possible secret.

## Verification and status

The export is prepared locally; no GitHub repository has been created or pushed, and no GitHub Pages deployment has been run by the assistant. The existing Sites website remains unchanged. The first deployment requires the repository and Pages setting above.

Official documentation:
- https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site
- https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
