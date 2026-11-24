// news-image-20261123 entry (Node 22, standard library only).
// The poster is entry.png beside this file; the program copies it to the
// output directory the grader provides. It creates the output directory
// first so the copy never fails on a fresh container.
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
const src = new URL('./entry.png', import.meta.url);
if (!existsSync(src)) throw new Error('entry.png missing from repository');
copyFileSync(src, join(outDir, 'entry.png'));
