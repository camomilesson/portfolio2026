import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { glob } from 'astro/loaders';
const projects = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/projects' }),
  schema: z.object({
    title: z.string(), summary: z.string(), category: z.string(),
    technologies: z.array(z.string()), featured: z.boolean().default(false),
    order: z.number(), source: z.url(), live: z.url().optional(), liveLabel: z.string().default("Visit website"),
    accent: z.enum(['green', 'ochre', 'blue', 'rose', 'purple']),
    visual: z.string(), image: z.string().optional(), imageAlt: z.string().optional(),
    imageKind: z.enum(['artwork', 'screenshot']).default('artwork'),
    screenshots: z.array(z.object({
      src: z.string(), alt: z.string(), title: z.string(), caption: z.string(),
      width: z.number(), height: z.number(),
    })).default([]),
    draft: z.boolean().default(false),
  }),
});
export const collections = { projects };
