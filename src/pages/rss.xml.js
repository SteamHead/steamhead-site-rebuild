/*
  rss.xml.js — the Great Things Blog feed, at /rss.xml.

  Exists for automation more than for human subscribers: RSS-to-email
  (Mailchimp), Zapier/IFTTT/Make recipes that announce new posts, and
  Slack/Discord feed bots. Search engines ignore it — discovery is the
  sitemap's job (see astro.config.mjs).

  Items carry full post HTML rather than just the description, because
  that is what makes RSS-to-email useful. The HTML comes from
  `entry.rendered.html`, which is the same output the site renders, so
  remarkYouTubeEmbed's video embeds and rehypeTaskListLabel's labels are
  already applied — no second Markdown parser to drift out of sync.
*/
import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

const SITE = 'https://steamhead.space';

// Feed readers and email templates resolve relative URLs against their own
// origin, not ours, so every in-post link and image has to be absolute.
// Matches src="/foo" and href="/foo" but not protocol-relative "//host".
function absolutise(html) {
  return html.replace(/(src|href)="\/(?!\/)/g, `$1="${SITE}/`);
}

export async function GET(context) {
  const posts = (await getCollection('blog', ({ data }) => !data.draft))
    .sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf())
    // The full archive is 160+ posts. Nothing downstream reads past the
    // recent window, and an unbounded full-content feed gets large fast.
    .slice(0, 30);

  return rss({
    title: 'SteamHead — Great Things Blog',
    description:
      "Stories, projects, and ideas from SteamHead's global community of makers and educators.",
    site: context.site ?? SITE,
    trailingSlash: true,
    items: posts.map(post => ({
      title: post.data.title,
      pubDate: post.data.date,
      description: post.data.description,
      link: `/blog/${post.id}/`,
      author: post.data.author,
      categories: [...post.data.categories, ...post.data.tags],
      content: post.rendered?.html ? absolutise(post.rendered.html) : undefined,
    })),
    customData: '<language>en-us</language>',
  });
}
