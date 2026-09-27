# POP Verticals — Production Deploy

Target Vercel project: `pop-verticals-client`

Production root directory:
`produtos/pop-verticals`

Production branch:
`deploy/pop-verticals-client-production-20260926`

Expected production alias:
`https://pop-verticals-client.vercel.app/`

No build command is required. This is a static HTML deployment.

Before public release:
1. Set the Vercel project's Root Directory to `produtos/pop-verticals`.
2. Connect repository `princeandreofc/obsidian-importer`.
3. Set Production Branch to `deploy/pop-verticals-client-production-20260926`.
4. Disable Vercel Authentication for the production environment if external POP reviewers must access it.
5. Deploy and verify HTTP 200, responsive layout, form mailto, images/video, robots.txt and sitemap.xml.
