# CMS Setup Guide

This site uses **Sveltia CMS** — a browser-based content editor accessible at `/admin/`.
Staff can edit page content and write blog posts without touching any code.

The CMS authenticates through GitHub so edits commit directly to the repo,
which triggers Cloudflare Pages to rebuild the site automatically.

---

## One-time setup (do this before going live)

### Step 1 — Deploy the Sveltia Auth Worker to Cloudflare

The CMS needs a small OAuth handler so staff can log in with GitHub.
Sveltia provides a pre-built Cloudflare Worker for this.

1. Go to: https://github.com/sveltia/sveltia-cms-auth
2. Click **"Deploy to Cloudflare Workers"** (there's a button in the README)
3. Follow the prompts — you'll need to be logged into Cloudflare
4. Note the Worker URL it gives you (e.g. `https://sveltia-cms-auth.YOUR_NAME.workers.dev`)

### Step 2 — Create a GitHub OAuth App

1. Go to: https://github.com/settings/developers → **OAuth Apps → New OAuth App**
2. Fill in:
   - **Application name:** SteamHead CMS
   - **Homepage URL:** `https://your-site.pages.dev` (your Cloudflare Pages URL)
   - **Authorization callback URL:** `https://sveltia-cms-auth.YOUR_NAME.workers.dev/callback`
3. Click **Register application**
4. Copy the **Client ID**
5. Click **Generate a new client secret** and copy it

### Step 3 — Add secrets to the Cloudflare Worker

1. In the Cloudflare dashboard, go to **Workers & Pages → sveltia-cms-auth**
2. Go to **Settings → Variables**
3. Add two secret variables:
   - `GITHUB_CLIENT_ID` → paste your Client ID
   - `GITHUB_CLIENT_SECRET` → paste your Client Secret

### Step 4 — Update config.yml

Open `public/admin/config.yml` and replace the placeholder:

```yaml
# Change this line:
base_url: https://YOUR_AUTH_WORKER.workers.dev

# To your actual worker URL:
base_url: https://sveltia-cms-auth.YOUR_NAME.workers.dev
```

---

## How to use the CMS

Once deployed, staff visit: `https://your-site.pages.dev/admin/`

- **Blog Posts** — create, edit, delete posts in the "Great Things Blog"
- **Pages** — edit the copy on each of the 6 main pages
- **Site Settings** — update the mission statement, social links, contact URLs

Changes are saved as commits to the GitHub repo. Cloudflare Pages automatically
rebuilds the site within ~1 minute of each save.

---

## Local development (no OAuth needed)

To run the CMS locally without OAuth, add this to the top of `public/admin/config.yml`:

```yaml
local_backend: true
```

Then in a second terminal, run:

```bash
npx netlify-cms-proxy-server
```

The CMS will be available at `http://localhost:4321/admin/` and will read/write
files on disk directly.

**Remove `local_backend: true` before deploying.**
