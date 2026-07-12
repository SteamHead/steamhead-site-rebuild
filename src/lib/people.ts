import type { CollectionEntry } from 'astro:content';

/* A profile gets its own page only when it has written body content;
   frontmatter-only profiles appear as cards on /about-us/ without a link. */
export function personHasPage(person: CollectionEntry<'people'>): boolean {
  return !person.data.draft && (person.body ?? '').trim().length > 0;
}

/* Patterns a person can be mentioned by in blog posts.
   'Benjamin "James" Simpson' matches both "Benjamin Simpson" and
   "James Simpson"; every other name matches as written. */
function namePatterns(name: string): string[] {
  const nick = name.match(/^(\S+)\s+"([^"]+)"\s+(.+)$/);
  if (nick) return [`${nick[1]} ${nick[3]}`, `${nick[2]} ${nick[3]}`];
  return [name];
}

const escape = (s: string) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

export function mentionRegex(name: string): RegExp {
  const pats = namePatterns(name).map(escape);
  return new RegExp(`\\b(?:${pats.join('|')})\\b`, 'i');
}

/* Blog posts that mention the person by name, newest first.
   Computed at build time — regenerates on every deploy. */
export function blogMentions(
  name: string,
  posts: CollectionEntry<'blog'>[],
): CollectionEntry<'blog'>[] {
  const rx = mentionRegex(name);
  return posts
    .filter(
      p =>
        !p.data.draft &&
        (rx.test(p.data.title) ||
          rx.test(p.data.description ?? '') ||
          rx.test(p.body ?? '')),
    )
    .sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());
}
