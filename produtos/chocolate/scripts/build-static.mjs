import { mkdir, copyFile, rm } from 'node:fs/promises';
import { join } from 'node:path';

const root = process.cwd();
const out = join(root, 'dist');

await rm(out, { recursive: true, force: true });
await mkdir(join(out, 'dossie'), { recursive: true });
await mkdir(join(out, 'oficio'), { recursive: true });

await copyFile(join(root, 'index.html'), join(out, 'index.html'));
await copyFile(join(root, 'dossie.html'), join(out, 'dossie', 'index.html'));
await copyFile(join(root, 'oficio.html'), join(out, 'oficio', 'index.html'));

console.log('Static campaign generated in dist/');
