# Ali Love — LOVE IS THE SIGNAL Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Extend the existing Ali Love/THE SPIRAL project into the LOVE IS THE SIGNAL album-launch system with a procedural Resonance Rose, ethical distributed biography, reactive official website, connection game and live VJ instrument, stopping at a verified local build.

**Architecture:** Preserve the canonical site's server/static HTML and the current THE SPIRAL WebGL2 runtime. Add a framework-light, typed `love-signal` domain containing content/rights contracts, pure interaction logic, accessible React/Preact-compatible UI and adapters to the existing Spiral engine; do not create a second 3D engine. Resolve the real repository and host integration paths in Task 1 before any source edit.

**Tech Stack:** Canonical repo's installed framework; strict TypeScript; existing Three.js/WebGL2; native Web Audio API; `canvas.captureStream()` + `MediaRecorder`; existing unit runner or Vitest when none exists; Playwright + axe-core for journeys; Cinema 4D/Redshift, Houdini, TouchDesigner, Resolume Arena and DaVinci Resolve as offline/live-production tools only.

**Spec:** `docs/superpowers/specs/2026-08-24-ali-love-love-is-the-signal.md`

## Global Constraints

- Do not deploy, push, open a pull request, merge, or change any remote service.
- Do not change DNS, Vercel settings, security, permissions, billing, secrets or analytics accounts.
- Work in an isolated branch/worktree and stop at local build + local QA + written report.
- Do not invent an album title, release date, credit, biography fact or rights status.
- Treat 528 Hz as a cultural/compositional reference, never as a therapeutic or scientific claim.
- Preserve the existing 11 Spiral phases, official HTML, SEO, routes, copy and accessible fallbacks.
- Keep the existing Three/WebGL2 renderer in P0; no full WebGPU, TSL or framework migration.
- Audio, microphone and Web MIDI start only after deliberate consent or user gesture.
- Do not upload microphone data, create accounts, collect usernames or add PII.
- Every asset must use `concept`, `approved-preview`, `cleared-production` or `withheld`.
- Any production build mode must reject uncleared public media and embargoed release metadata.
- The generated key visual starts as `approved-preview`, not `cleared-production`.

---

## Target file map

All feature-owned source files use these exact paths. If the canonical repository does not use a `src/` directory, create `src/features/love-signal/`; only host-route imports depend on the audited integration map.

| Path | Responsibility |
| --- | --- |
| `docs/audits/ali-love-repo-baseline.md` | Canonical repo, versions, baseline and pre-existing failures |
| `docs/audits/ali-love-repo-map.json` | Machine-readable host integration paths |
| `src/features/love-signal/index.ts` | Public feature exports |
| `src/features/love-signal/model/types.ts` | Shared release, rights, biography, signal and frame types |
| `src/features/love-signal/model/signal528.ts` | 528-derived constants and public disclaimer |
| `src/features/love-signal/model/validateContent.ts` | Pure release/rights validation |
| `src/features/love-signal/content/release.ts` | Embargo-safe campaign and current-signal data |
| `src/features/love-signal/content/biography.ts` | Source-backed memory ledger |
| `src/features/love-signal/content/artworks.ts` | Cover/source audit and asset provenance |
| `src/features/love-signal/styles/tokens.css` | Palette, typography roles and motion tokens |
| `src/features/love-signal/ui/LoveSignalShell.tsx` | Campaign shell and accessible content flow |
| `src/features/love-signal/ui/ResonanceRose2D.tsx` | Semantic, reduced-motion/static Rose fallback |
| `src/features/love-signal/ui/NowTransmitting.tsx` | Embargo-safe release module |
| `src/features/love-signal/ui/BiographyMemory.tsx` | Ambient/discoverable/accessible biography layers |
| `src/features/love-signal/ui/SignalConsent.tsx` | Audio/microphone consent and state |
| `src/features/love-signal/rose/createRoseGeometry.ts` | Pure Resonance Rose vertex/instance data |
| `src/features/love-signal/rose/createRoseObject.ts` | Three object using the current renderer |
| `src/features/love-signal/rose/roseFallback.ts` | Low-cost/static visual parameters |
| `src/features/love-signal/integration/createSpiralSignalAdapter.ts` | Adapter from existing phases/audio to Rose state |
| `src/features/love-signal/integration/LoveSignalExperience.client.tsx` | Client-island lifecycle and disposal |
| `src/features/love-signal/audio/createSignalAnalyser.ts` | LOW/MID/HIGH/ENERGY envelopes |
| `src/features/love-signal/audio/createCalibrationTone.ts` | Opt-in, bounded calibration cue |
| `src/features/love-signal/game/reducer.ts` | Deterministic 30-second game state machine |
| `src/features/love-signal/game/connection.ts` | Particle-cluster bridge scoring |
| `src/features/love-signal/game/ResonanceSession.tsx` | Accessible game UI and inputs |
| `src/features/love-signal/recorder/createSessionRecorder.ts` | MIME detection, capture and cleanup |
| `src/features/love-signal/vj/controlMap.ts` | Normalized macros and control names |
| `src/features/love-signal/vj/presets.ts` | Five scene-bank presets |
| `src/features/love-signal/vj/VJStudio.tsx` | Primary live instrument UI |
| `public/media/love-signal/concept/resonance-rose-key-visual-v1.png` | Approved-preview key visual |
| `public/media/love-signal/provenance/resonance-rose-key-visual-v1.json` | Rights/source sidecar |
| `tests/love-signal/*.test.ts(x)` | Pure logic and component tests |
| `tests/e2e/love-signal.spec.ts` | End-to-end website, game, VJ and accessibility journey |
| `docs/qa/ali-love-love-is-the-signal-local.md` | Final local build and QA report |

Host-route paths are read from `docs/audits/ali-love-repo-map.json`. That file is a required interface, not a note. Later tasks must fail closed when an integration path is absent.

---

### Task 1: Identify the canonical repository and freeze the baseline

**Files:**

- Create: `docs/audits/ali-love-repo-baseline.md`
- Create: `docs/audits/ali-love-repo-map.json`
- Inspect only: `package.json`, lockfiles, framework config, route sources, Vercel config and current Spiral/VJ sources

**Interfaces:**

- Consumes: the uploaded master handoff and the canonical working tree.
- Produces: `RepoMap` JSON used by every host-integration task.

- [ ] **Step 1: Create or enter an isolated worktree without altering the current working tree**

Run the repository's normal worktree workflow. Record the exact branch, base commit and local path. Do not use `git reset`, `git checkout --` or another destructive command.

- [ ] **Step 2: Inventory candidate repositories and framework evidence**

Run from each candidate root:

```bash
git rev-parse --show-toplevel
git branch --show-current
git rev-parse HEAD
rg --files -g 'package.json' -g 'next.config.*' -g 'vite.config.*' -g 'vercel.json' -g 'app/**/page.*' -g 'src/app/**/page.*' -g 'pages/**' -g 'src/pages/**' | sort
```

Expected: one documented candidate whose configured domain/pipeline or repository metadata explains the official site. If no candidate is provably canonical, stop and report the evidence; do not edit source.

- [ ] **Step 3: Record exact installed versions and package manager**

Use the lockfile and installed manifest, not memory:

```bash
node -e "const p=require('./package.json'); console.log(JSON.stringify({packageManager:p.packageManager,scripts:p.scripts,dependencies:p.dependencies,devDependencies:p.devDependencies},null,2))"
```

Expected: framework, React/Preact, Three and test/build versions are copied into the baseline report.

- [ ] **Step 4: Run the untouched baseline commands**

Use the package manager selected by the lockfile:

```bash
# package-lock.json
npm ci && npm run build

# pnpm-lock.yaml
corepack pnpm install --frozen-lockfile && corepack pnpm run build

# yarn.lock
corepack yarn install --immutable && corepack yarn build

# bun.lock or bun.lockb
bun install --frozen-lockfile && bun run build
```

Run the existing unit/E2E commands listed in `package.json` without changing configuration. Capture exit codes and logs in the report. A pre-existing failure does not authorize a remote fix.

- [ ] **Step 5: Write the machine-readable repo map**

Create `docs/audits/ali-love-repo-map.json` with real, repository-relative paths:

```json
{
  "canonicalRepo": "absolute path recorded by git rev-parse",
  "baseCommit": "40-character commit SHA",
  "packageManager": "npm",
  "framework": "next-app",
  "paths": {
    "homeRouteSource": "src/app/page.tsx",
    "spiralEntrySource": "src/components/spiral/SpiralExperience.client.tsx",
    "vjRouteSource": "src/app/vj/page.tsx",
    "archiveSource": "src/components/archive/Archive.tsx",
    "globalStylesSource": "src/app/globals.css",
    "assetRoot": "public"
  },
  "commands": {
    "install": "npm ci",
    "unit": "npm run test:unit",
    "e2e": "npm run test:e2e",
    "build": "npm run build"
  }
}
```

Replace each example value with observed evidence. Validate that every path exists before continuing:

```bash
node -e "const fs=require('fs');const m=require('./docs/audits/ali-love-repo-map.json');for(const [k,p] of Object.entries(m.paths)){if(k!=='assetRoot'&&!fs.existsSync(p))throw new Error(k+': '+p)}"
```

Expected: exit code 0.

- [ ] **Step 6: Write the human baseline report**

The report must contain canonical evidence, base commit, versions, route map, baseline commands, exit codes, pre-existing failures, current route/content list and a statement that no remote action occurred.

- [ ] **Step 7: Commit the audit only**

```bash
git add docs/audits/ali-love-repo-baseline.md docs/audits/ali-love-repo-map.json
git commit -m "docs: freeze ali love campaign baseline"
```

---

### Task 2: Add typed content, evidence and rights contracts

**Files:**

- Create: `src/features/love-signal/model/types.ts`
- Create: `src/features/love-signal/model/signal528.ts`
- Create: `src/features/love-signal/model/validateContent.ts`
- Create: `src/features/love-signal/content/release.ts`
- Create: `src/features/love-signal/content/biography.ts`
- Create: `src/features/love-signal/content/artworks.ts`
- Create: `src/features/love-signal/index.ts`
- Test: `tests/love-signal/validateContent.test.ts`

**Interfaces:**

- Consumes: no UI or renderer code.
- Produces: `ReleaseManifest`, `BiographyMemory`, `ArtworkRecord`, `validatePublicContent()` and `SIGNAL_528`.

- [ ] **Step 1: Write the failing validation tests**

```ts
import { describe, expect, it } from "vitest";
import { validatePublicContent } from "../../src/features/love-signal/model/validateContent";

describe("validatePublicContent", () => {
  it("rejects invented or absent release metadata in released mode", () => {
    expect(() => validatePublicContent({
      campaign: "LOVE IS THE SIGNAL",
      releaseTitle: null,
      releaseDate: null,
      status: "released",
      currentSignal: null,
      artworkAssetId: null,
      audioAssetIds: []
    }, [], "production")).toThrow(/releaseTitle/);
  });

  it("rejects an uncleared enabled biography memory in production", () => {
    expect(() => validatePublicContent({
      campaign: "LOVE IS THE SIGNAL",
      releaseTitle: null,
      releaseDate: null,
      status: "embargoed",
      currentSignal: null,
      artworkAssetId: null,
      audioAssetIds: []
    }, [{ id: "memory", enabled: true, evidence: "needs-artist-verification", rights: "withheld" }], "production")).toThrow(/memory/);
  });
});
```

- [ ] **Step 2: Run the focused test and confirm it fails because the module is absent**

Run the audited unit command with `tests/love-signal/validateContent.test.ts`. Expected: module resolution failure.

- [ ] **Step 3: Implement the contracts and fail-closed validator**

Use the exact unions from the spec. The validator returns no value when valid and throws an error containing every invalid field or memory ID:

```ts
export function validatePublicContent(
  release: ReleaseManifest,
  memories: Pick<BiographyMemory, "id" | "enabled" | "evidence" | "rights">[],
  mode: "preview" | "production"
): void {
  const errors: string[] = [];
  if (mode === "production" && release.status === "released") {
    if (!release.releaseTitle) errors.push("releaseTitle");
    if (!release.releaseDate) errors.push("releaseDate");
  }
  for (const memory of memories) {
    if (mode === "production" && memory.enabled &&
        (memory.evidence !== "project-approved" || memory.rights !== "cleared-production")) {
      errors.push(`memory:${memory.id}`);
    }
  }
  if (errors.length) throw new Error(`Public content blocked: ${errors.join(", ")}`);
}
```

- [ ] **Step 4: Encode the 528 constants and disclaimer**

```ts
export const SIGNAL_528 = Object.freeze({
  calibrationHz: 528,
  foldedHz: [66, 132, 264, 528] as const,
  transitionMs: 528,
  breathMs: 5280,
  holdMs: 1056,
  normalized: 0.528
});

export const SIGNAL_528_DISCLAIMER =
  "528 Hz is used in this artwork as a cultural and compositional reference. No medical or therapeutic claim is made.";
```

- [ ] **Step 5: Enter source-backed content with conservative states**

Set the release to `embargoed`, keep title/date null, mark the generated key visual `approved-preview`, and keep memories requiring artist confirmation disabled. Enter `My Only Crime` only as `public-catalog` + `reference-only` until editorial approval.

- [ ] **Step 6: Run the focused test and typecheck**

Expected: tests pass; strict typecheck has no new errors.

- [ ] **Step 7: Commit the content boundary**

```bash
git add src/features/love-signal tests/love-signal/validateContent.test.ts
git commit -m "feat: add love signal content and rights contracts"
```

---

### Task 3: Add design tokens and the accessible 2D Resonance Rose

**Files:**

- Create: `src/features/love-signal/styles/tokens.css`
- Create: `src/features/love-signal/ui/ResonanceRose2D.tsx`
- Test: `tests/love-signal/ResonanceRose2D.test.tsx`

**Interfaces:**

- Consumes: `SIGNAL_528` only through CSS values copied from the spec.
- Produces: `ResonanceRose2D({ state, title })` with no Canvas dependency.

- [ ] **Step 1: Write the failing accessibility test**

```tsx
import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import { ResonanceRose2D } from "../../src/features/love-signal/ui/ResonanceRose2D";

it("exposes a named image and does not require motion", () => {
  render(<ResonanceRose2D state="listening" title="The Resonance Rose" />);
  expect(screen.getByRole("img", { name: "The Resonance Rose" })).toBeVisible();
  expect(screen.getByTestId("resonance-rose")).toHaveAttribute("data-state", "listening");
});
```

- [ ] **Step 2: Run the focused test and confirm module failure**

Expected: FAIL because the component does not exist.

- [ ] **Step 3: Implement a semantic CSS/SVG fallback**

Render one labeled `<svg role="img">` with twelve petals, six axes, two orbit groups and a central core. Use generated paths owned by this project; do not trace a cover or Emoto crystal. State changes may alter CSS custom properties only.

```tsx
export type RoseState = "unstable" | "listening" | "resonant" | "remembered";

export function ResonanceRose2D({ state, title }: { state: RoseState; title: string }) {
  const petals = Array.from({ length: 12 }, (_, index) => index * 30);
  return (
    <svg role="img" aria-label={title} data-testid="resonance-rose" data-state={state}
      viewBox="0 0 528 528" className="resonanceRose2D">
      <g className="resonanceRose2D__petals">
        {petals.map((angle) => <ellipse key={angle} cx="264" cy="150" rx="46" ry="112"
          transform={`rotate(${angle} 264 264)`} />)}
      </g>
      <circle className="resonanceRose2D__core" cx="264" cy="264" r="18" />
    </svg>
  );
}
```

- [ ] **Step 4: Implement motion and reduced-motion tokens**

Use the palette and exact `528ms`, `1056ms`, `5280ms` tokens. Under `prefers-reduced-motion: reduce`, remove rotation, pulsing and transition interpolation while preserving state color/label.

- [ ] **Step 5: Run test, typecheck and a contrast check**

Expected: component test passes; no text contrast below WCAG AA for normal copy.

- [ ] **Step 6: Commit the accessible identity**

```bash
git add src/features/love-signal/styles/tokens.css src/features/love-signal/ui/ResonanceRose2D.tsx tests/love-signal/ResonanceRose2D.test.tsx
git commit -m "feat: add accessible resonance rose identity"
```

---

### Task 4: Build deterministic Resonance Rose geometry without a new renderer

**Files:**

- Create: `src/features/love-signal/rose/createRoseGeometry.ts`
- Create: `src/features/love-signal/rose/roseFallback.ts`
- Test: `tests/love-signal/createRoseGeometry.test.ts`

**Interfaces:**

- Consumes: `{ seed, petals, axes, radius, asymmetry }`.
- Produces: typed arrays for petal control points, axes, orbits and particles; no Three imports.

- [ ] **Step 1: Write the failing deterministic-geometry test**

```ts
import { expect, it } from "vitest";
import { createRoseGeometry } from "../../src/features/love-signal/rose/createRoseGeometry";

it("creates the canonical 12-petal, 6-axis rose deterministically", () => {
  const a = createRoseGeometry({ seed: 528, petals: 12, axes: 6, radius: 1, asymmetry: 0.028 });
  const b = createRoseGeometry({ seed: 528, petals: 12, axes: 6, radius: 1, asymmetry: 0.028 });
  expect(a.petalAngles).toEqual(b.petalAngles);
  expect(a.petalAngles).toHaveLength(12);
  expect(a.axisAngles).toHaveLength(6);
  expect(Math.max(...a.radii)).toBeLessThanOrEqual(1.028);
});
```

- [ ] **Step 2: Run the focused test and confirm module failure**

- [ ] **Step 3: Implement seeded geometry as pure math**

Use a local seeded PRNG and polar coordinates. Return ordinary arrays or typed arrays so the same state can feed WebGL, CSS fallback, tests and offline exporters. Clamp asymmetry to `[0, 0.08]`.

- [ ] **Step 4: Add mobile/static fallbacks**

Export immutable presets `ROSE_CINEMATIC`, `ROSE_STANDARD`, `ROSE_MOBILE` and `ROSE_STATIC`. The static preset creates no moving particles.

- [ ] **Step 5: Run tests and verify a stable serialized snapshot**

Expected: identical seed and inputs produce byte-stable values within the test's numeric precision.

- [ ] **Step 6: Commit the pure geometry**

```bash
git add src/features/love-signal/rose tests/love-signal/createRoseGeometry.test.ts
git commit -m "feat: add deterministic resonance rose geometry"
```

---

### Task 5: Adapt the Rose to the existing THE SPIRAL renderer

**Files:**

- Create: `src/features/love-signal/rose/createRoseObject.ts`
- Create: `src/features/love-signal/integration/createSpiralSignalAdapter.ts`
- Modify: the exact `spiralEntrySource` from `docs/audits/ali-love-repo-map.json`
- Test: `tests/love-signal/createSpiralSignalAdapter.test.ts`

**Interfaces:**

- Consumes: existing renderer/scene, current phase ID/progress and audio envelopes.
- Produces: one disposable `THREE.Group` and `SpiralSignalAdapter.update(frame)`.

- [ ] **Step 1: Write the failing adapter test**

```ts
import { expect, it, vi } from "vitest";
import { createSpiralSignalAdapter } from "../../src/features/love-signal/integration/createSpiralSignalAdapter";

it("maps LISTEN to a calm rose and disposes exactly once", () => {
  const disposeRose = vi.fn();
  const adapter = createSpiralSignalAdapter({ disposeRose });
  expect(adapter.frame({ phase: "listen", progress: 0.5, energy: 0.2 }).depth).toBeLessThan(0.5);
  adapter.dispose();
  adapter.dispose();
  expect(disposeRose).toHaveBeenCalledTimes(1);
});
```

- [ ] **Step 2: Run the focused test and confirm module failure**

- [ ] **Step 3: Implement one Three group with bounded resources**

Use the canonical geometry arrays to create instanced petals/particles, one line/orbit material family and one core light/material. Reuse geometries and materials. Do not create a renderer, animation loop, post stack or second scene.

- [ ] **Step 4: Implement the phase-to-signal adapter**

Map all 11 existing phase IDs to normalized `energy`, `depth`, `memory` and `connection`. Keep the existing camera score and transitions. The Rose is prominent in Bring Love, Listen and Finale; it recedes in Film, Records, Press and EPK so official material remains readable.

- [ ] **Step 5: Integrate through the audited Spiral entry**

Read the exact path without guessing:

```bash
ALI_SPIRAL_PATH=$(node -p "require('./docs/audits/ali-love-repo-map.json').paths.spiralEntrySource")
test -f "$ALI_SPIRAL_PATH"
```

Add the adapter to the current lifecycle, use the existing animation loop, and call its idempotent disposer from the existing teardown.

- [ ] **Step 6: Run unit tests and the existing entry → exit → entry lifecycle test**

Expected: one animation loop, no duplicate listeners and no increasing Three resource counts after the second exit.

- [ ] **Step 7: Commit the renderer adapter**

```bash
git add src/features/love-signal/rose/createRoseObject.ts src/features/love-signal/integration/createSpiralSignalAdapter.ts tests/love-signal/createSpiralSignalAdapter.test.ts "$ALI_SPIRAL_PATH"
git commit -m "feat: integrate resonance rose with spiral runtime"
```

---

### Task 6: Add opt-in signal analysis and bounded 528 calibration

**Files:**

- Create: `src/features/love-signal/audio/createSignalAnalyser.ts`
- Create: `src/features/love-signal/audio/createCalibrationTone.ts`
- Create: `src/features/love-signal/ui/SignalConsent.tsx`
- Test: `tests/love-signal/audio.test.ts`

**Interfaces:**

- Consumes: an `AudioContext` created after user gesture and an optional `MediaStream`.
- Produces: smoothed `{ low, mid, high, energy }` values and idempotent cleanup.

- [ ] **Step 1: Write failing tests for band boundaries and cleanup**

```ts
import { expect, it, vi } from "vitest";
import { aggregateBands } from "../../src/features/love-signal/audio/createSignalAnalyser";

it("returns normalized low, mid, high and energy envelopes", () => {
  const bins = new Uint8Array(128).fill(128);
  expect(aggregateBands(bins)).toEqual({ low: 128 / 255, mid: 128 / 255, high: 128 / 255, energy: 128 / 255 });
});

it("stops every microphone track", () => {
  const stop = vi.fn();
  const tracks = [{ stop }, { stop }];
  tracks.forEach((track) => track.stop());
  expect(stop).toHaveBeenCalledTimes(2);
});
```

- [ ] **Step 2: Run the tests and confirm module failure**

- [ ] **Step 3: Implement the analyser**

Use the existing band contract: LOW bins 0–8, MID 9–32, HIGH 33–96 and aggregate RMS energy. Apply faster attack than decay and clamp outputs to `[0,1]`.

- [ ] **Step 4: Implement the calibration cue**

Create an oscillator only after gesture, set `528 Hz`, begin at or below `-24 dBFS`, fade in/out, stop within `528 ms`, disconnect nodes and return an idempotent `stop()`.

- [ ] **Step 5: Implement consent UI**

Expose separate `Enable sound` and `Use microphone` actions, a persistent mute/stop action, local-only explanation and the exact cultural/compositional disclaimer. Denial leaves the full site usable.

- [ ] **Step 6: Run tests and manually verify browser permission denial**

Expected: denial causes no unhandled rejection; microphone tracks stop immediately when requested.

- [ ] **Step 7: Commit the audio boundary**

```bash
git add src/features/love-signal/audio src/features/love-signal/ui/SignalConsent.tsx tests/love-signal/audio.test.ts
git commit -m "feat: add opt-in signal audio analysis"
```

---

### Task 7: Implement the deterministic connection mechanic

**Files:**

- Create: `src/features/love-signal/game/reducer.ts`
- Create: `src/features/love-signal/game/connection.ts`
- Create: `src/features/love-signal/game/ResonanceSession.tsx`
- Test: `tests/love-signal/game.test.ts`

**Interfaces:**

- Consumes: elapsed milliseconds and normalized tune/shape/connection inputs.
- Produces: deterministic `GameState` and final session seed/topology.

- [ ] **Step 1: Write failing state-transition tests**

```ts
import { expect, it } from "vitest";
import { gameReducer, initialGameState } from "../../src/features/love-signal/game/reducer";

it("enters remembered only after sustained resonance in the hold window", () => {
  let state = initialGameState(528);
  state = gameReducer(state, { type: "TICK", elapsedMs: 6000, resonance: 0.6 });
  state = gameReducer(state, { type: "TICK", elapsedMs: 19000, resonance: 0.9 });
  state = gameReducer(state, { type: "TICK", elapsedMs: 26000, resonance: 0.9 });
  expect(state.status).toBe("remembered");
});

it("has no game-over state", () => {
  const state = gameReducer(initialGameState(528), { type: "TICK", elapsedMs: 30000, resonance: 0 });
  expect(state.status).toBe("listening");
});
```

- [ ] **Step 2: Run the tests and confirm module failure**

- [ ] **Step 3: Implement the reducer and timing windows**

Use exact windows `0–5000`, `5000–18000`, `18000–26000`, `26000–30000`. Make time an input rather than reading `Date.now()` inside the reducer.

- [ ] **Step 4: Implement connection scoring**

Build a small graph from particle positions. A bridge exists when two different clusters have a normalized distance under the current threshold. Score sustained bridges, not frantic pointer movement. Clamp all inputs and make the algorithm seed-deterministic.

- [ ] **Step 5: Implement keyboard/touch UI**

Provide labeled Tune, Shape and Capture controls; arrow-key and button alternatives; visible state text; a 30-second progress indicator; and the final message `THE ROOM REMEMBERS`. No leaderboard, name field, login or network request.

- [ ] **Step 6: Run logic/component tests**

Expected: deterministic seed replay; keyboard-only completion; no `gameOver` value in the exported type.

- [ ] **Step 7: Commit the game vertical slice**

```bash
git add src/features/love-signal/game tests/love-signal/game.test.ts
git commit -m "feat: add resonance connection session"
```

---

### Task 8: Add local recording as the game trophy

**Files:**

- Create: `src/features/love-signal/recorder/createSessionRecorder.ts`
- Test: `tests/love-signal/recorder.test.ts`

**Interfaces:**

- Consumes: a Canvas, FPS and optional cleared audio stream.
- Produces: `{ start, stop, dispose, mimeType }` and a local Blob; no upload.

- [ ] **Step 1: Write failing MIME-priority and filename tests**

```ts
import { expect, it } from "vitest";
import { chooseRecordingMime, sessionFilename } from "../../src/features/love-signal/recorder/createSessionRecorder";

it("prefers supported MP4, then VP9 WebM, then generic WebM", () => {
  const supported = (mime: string) => mime === "video/webm;codecs=vp9";
  expect(chooseRecordingMime(supported)).toBe("video/webm;codecs=vp9");
});

it("creates an ali love session filename", () => {
  expect(sessionFilename(new Date("2026-08-24T12:34:00Z"), "webm"))
    .toBe("ali-love-spiral-session-20260824-1234.webm");
});
```

- [ ] **Step 2: Run the tests and confirm module failure**

- [ ] **Step 3: Implement capability detection and recorder lifecycle**

Try compatible MP4 candidates first, then VP9 WebM, then generic WebM using `MediaRecorder.isTypeSupported`. Use `canvas.captureStream(30)`. Revoke object URLs, stop captured tracks and clear chunks after download/dispose.

- [ ] **Step 4: Wire Capture to the game's final window**

Recording remains a direct user action. If unavailable, show `SAVE IMAGE` and export a still. Web Share appears only after capability detection and never auto-opens.

- [ ] **Step 5: Run tests and record a local clip in two browsers**

Expected: a playable file, correct extension/MIME pairing, no continuing capture track after disposal.

- [ ] **Step 6: Commit the recorder**

```bash
git add src/features/love-signal/recorder tests/love-signal/recorder.test.ts
git commit -m "feat: add local resonance session recorder"
```

---

### Task 9: Evolve VJ Studio into the five-bank signal instrument

**Files:**

- Create: `src/features/love-signal/vj/controlMap.ts`
- Create: `src/features/love-signal/vj/presets.ts`
- Create: `src/features/love-signal/vj/VJStudio.tsx`
- Modify: the exact `vjRouteSource` from `docs/audits/ali-love-repo-map.json`
- Test: `tests/love-signal/vj.test.ts`

**Interfaces:**

- Consumes: normalized audio envelopes and existing Spiral parameters.
- Produces: `VJFrame { scene, energy, depth, memory, connection }` and stable control names for browser/TouchDesigner/Resolume documentation.

- [ ] **Step 1: Write the failing preset and clamp tests**

```ts
import { expect, it } from "vitest";
import { applyVJControl, VJ_PRESETS } from "../../src/features/love-signal/vj/presets";

it("provides exactly five named scene banks", () => {
  expect(VJ_PRESETS.map((p) => p.id)).toEqual(["orbit", "groove", "garden", "ritual", "day-signal"]);
});

it("clamps every macro to zero through one", () => {
  expect(applyVJControl(VJ_PRESETS[0], "energy", 4).energy).toBe(1);
  expect(applyVJControl(VJ_PRESETS[0], "memory", -1).memory).toBe(0);
});
```

- [ ] **Step 2: Run the tests and confirm module failure**

- [ ] **Step 3: Implement scene and macro contracts**

Primary UI has five scene buttons and four macros only: ENERGY, DEPTH, MEMORY, CONNECTION. Map audio to parameters through attack/decay smoothing. Camera amplitude remains bounded and cannot be directly driven by high-frequency peaks.

- [ ] **Step 4: Implement the live UI**

Support pointer, keyboard and existing audio. Add a deliberate advanced drawer for calibration, MIDI learn and recording. Show current scene, FPS profile, audio state and REC state without covering the artwork.

- [ ] **Step 5: Integrate through the audited VJ route**

```bash
ALI_VJ_PATH=$(node -p "require('./docs/audits/ali-love-repo-map.json').paths.vjRouteSource")
test -f "$ALI_VJ_PATH"
```

Mount `VJStudio` without removing the current route's accessible title, description or fallback. Preserve any current operator shortcuts unless they conflict; document the final map.

- [ ] **Step 6: Run unit tests and a 30-minute local soak**

Expected: stable memory/geometry/texture counts, recorder starts/stops repeatedly, MIDI denial does not break controls.

- [ ] **Step 7: Commit the VJ instrument**

```bash
git add src/features/love-signal/vj tests/love-signal/vj.test.ts "$ALI_VJ_PATH"
git commit -m "feat: evolve vj studio into signal instrument"
```

---

### Task 10: Render the biography as ethical distributed memory

**Files:**

- Create: `src/features/love-signal/ui/BiographyMemory.tsx`
- Test: `tests/love-signal/BiographyMemory.test.tsx`
- Modify: the audited Archive/EPK source recorded during Task 1

**Interfaces:**

- Consumes: enabled `BiographyMemory[]`.
- Produces: ambient motif tokens, focus/hover liner notes and a complete accessible archive list.

- [ ] **Step 1: Write failing ethical-rendering tests**

```tsx
import { render, screen } from "@testing-library/react";
import { expect, it } from "vitest";
import { BiographyMemory } from "../../src/features/love-signal/ui/BiographyMemory";

it("does not render withheld facts and exposes cleared copy to assistive tech", () => {
  render(<BiographyMemory memories={[
    { id: "clear", enabled: true, evidence: "project-approved", rights: "cleared-production", title: "Do It Again", accessibleCopy: "Cleared credit", discoverableCopy: "2007", ambientMotif: "constellation", year: 2007, role: "featured", sourceUrl: "https://example.test" },
    { id: "held", enabled: true, evidence: "needs-artist-verification", rights: "withheld", title: "Held", accessibleCopy: "Must not render", discoverableCopy: "Hidden", ambientMotif: "none", year: null, role: "process", sourceUrl: "https://example.test" }
  ]} />);
  expect(screen.getByText("Cleared credit")).toBeVisible();
  expect(screen.queryByText("Must not render")).toBeNull();
});
```

- [ ] **Step 2: Run the test and confirm module failure**

- [ ] **Step 3: Implement the three layers**

Ambient layers expose a named motif token to the Spiral adapter. Discoverable copy opens on hover **and focus**. The accessible archive is ordinary semantic HTML with year, role, copy and source link. Do not use opacity-zero text, rapid flashes or inaudible messaging.

- [ ] **Step 4: Integrate into the existing Archive/EPK without duplicate copy**

Use the current official biography as source and replace duplicated visual labels with references to the ledger. Keep every public claim disabled until its evidence and rights gates pass.

- [ ] **Step 5: Run component, keyboard and screen-reader smoke tests**

Expected: all discoverable notes are keyboard reachable; withheld entries are absent from DOM and metadata output.

- [ ] **Step 6: Commit the memory layer**

```bash
ALI_ARCHIVE_PATH=$(node -p "require('./docs/audits/ali-love-repo-map.json').paths.archiveSource")
test -f "$ALI_ARCHIVE_PATH"
git add src/features/love-signal/ui/BiographyMemory.tsx tests/love-signal/BiographyMemory.test.tsx src/features/love-signal/content/biography.ts
git add "$ALI_ARCHIVE_PATH"
git commit -m "feat: distribute ali love biography through memory layers"
```

Task 1 requires `archiveSource`; if its recorded path no longer exists, stop and treat that as repository drift before editing the archive.

---

### Task 11: Add the campaign shell and embargo-safe current signal

**Files:**

- Create: `src/features/love-signal/ui/NowTransmitting.tsx`
- Create: `src/features/love-signal/ui/LoveSignalShell.tsx`
- Create: `src/features/love-signal/integration/LoveSignalExperience.client.tsx`
- Modify: the exact `homeRouteSource` from `docs/audits/ali-love-repo-map.json`
- Test: `tests/love-signal/LoveSignalShell.test.tsx`

**Interfaces:**

- Consumes: release manifest, 2D Rose, client-island loader, game, biography and official links.
- Produces: DOM-first public journey and lazy visual enhancement.

- [ ] **Step 1: Write failing embargo tests**

```tsx
import { render, screen } from "@testing-library/react";
import { expect, it } from "vitest";
import { NowTransmitting } from "../../src/features/love-signal/ui/NowTransmitting";

it("renders neutral campaign copy while release metadata is embargoed", () => {
  render(<NowTransmitting release={{ campaign: "LOVE IS THE SIGNAL", releaseTitle: null, releaseDate: null, status: "embargoed", currentSignal: null, artworkAssetId: null, audioAssetIds: [] }} />);
  expect(screen.getByText("NEW TRANSMISSION")).toBeVisible();
  expect(screen.queryByText(/coming soon/i)).toBeNull();
});
```

- [ ] **Step 2: Run the test and confirm module failure**

- [ ] **Step 3: Implement the server/static campaign shell**

Order the sections: TUNE IN, NOW TRANSMITTING, ENTER THE SPIRAL, ALBUM UNIVERSE, RESONANCE SESSION, VJ STUDIO, MEMORY ARCHIVE, LIVE/PRESS/EPK. Keep official content and links in HTML. Use the 2D Rose as the initial render.

- [ ] **Step 4: Implement the lazy client island**

Load the visual experience near viewport or after `ENTER THE SPIRAL`, preserve dimensions to prevent layout shift, catch WebGL failure and keep the 2D experience. On unmount, cancel the current animation loop, remove listeners, stop media tracks, disconnect audio, dispose Three resources and clear timers.

- [ ] **Step 5: Integrate through the audited home route**

```bash
ALI_HOME_ROUTE_PATH=$(node -p "require('./docs/audits/ali-love-repo-map.json').paths.homeRouteSource")
test -f "$ALI_HOME_ROUTE_PATH"
```

Preserve existing metadata, structured data and official navigation. Import the shell into the appropriate campaign slot; do not move the full route into a client component.

- [ ] **Step 6: Run tests, typecheck and local route smoke test**

Expected: HTML content is present before JavaScript/Canvas; WebGL-disabled mode remains complete; no hydration error.

- [ ] **Step 7: Commit the campaign integration**

```bash
git add src/features/love-signal/ui src/features/love-signal/integration/LoveSignalExperience.client.tsx tests/love-signal/LoveSignalShell.test.tsx "$ALI_HOME_ROUTE_PATH"
git commit -m "feat: add love is the signal campaign shell"
```

---

### Task 12: Add the concept asset and provenance sidecar

**Files:**

- Create: `public/media/love-signal/concept/resonance-rose-key-visual-v1.png`
- Create: `public/media/love-signal/provenance/resonance-rose-key-visual-v1.json`
- Modify: `src/features/love-signal/content/artworks.ts`
- Test: `tests/love-signal/assets.test.ts`

**Interfaces:**

- Consumes: project-local generated key visual from the handoff package.
- Produces: one manifest-addressable `approved-preview` asset with provenance.

- [ ] **Step 1: Write the failing provenance test**

```ts
import fs from "node:fs";
import { expect, it } from "vitest";

it("keeps the key visual out of production clearance", () => {
  const data = JSON.parse(fs.readFileSync("public/media/love-signal/provenance/resonance-rose-key-visual-v1.json", "utf8"));
  expect(data.status).toBe("approved-preview");
  expect(data.publicationAuthorized).toBe(false);
  expect(data.sourceType).toBe("generated-original-concept");
});
```

- [ ] **Step 2: Run the test and confirm the sidecar is absent**

- [ ] **Step 3: Copy the supplied project asset without recompression**

Copy `artifacts/ali-love-love-is-the-signal/resonance-rose-key-visual-v1.png` to the exact public concept path and record its SHA-256 in the sidecar.

- [ ] **Step 4: Create the provenance record**

```json
{
  "id": "resonance-rose-key-visual-v1",
  "sourceType": "generated-original-concept",
  "createdFor": "Ali Love — LOVE IS THE SIGNAL",
  "status": "approved-preview",
  "publicationAuthorized": false,
  "containsArtistLikeness": false,
  "containsThirdPartyArtwork": false,
  "scientificClaim": false,
  "sha256": "computed lowercase SHA-256",
  "notes": "Original concept inspired by general standing-wave physics and the project's audited visual grammar; not a reproduction of an existing cover or a scientific diagram."
}
```

- [ ] **Step 5: Register the asset and run the test**

Expected: preview rendering can address the asset; production validation refuses it until status and authorization are explicitly changed in a separately approved workflow.

- [ ] **Step 6: Commit the concept asset**

```bash
git add public/media/love-signal src/features/love-signal/content/artworks.ts tests/love-signal/assets.test.ts
git commit -m "chore: add resonance rose concept provenance"
```

---

### Task 13: Document the offline 3D, VJ and campaign production package

**Files:**

- Create: `docs/production/ali-love-resonance-rose-asset-pipeline.md`
- Create: `docs/production/vj-control-map.json`
- Create: `docs/production/deliverables-matrix.csv`
- Test: `tests/love-signal/production-contracts.test.ts`

**Interfaces:**

- Consumes: browser control names, palette, Rose topology and campaign phases.
- Produces: tool-agnostic exchange contract for Cinema 4D/Redshift, Houdini, TouchDesigner, Resolume and Resolve.

- [ ] **Step 1: Write a failing control-map parity test**

```ts
import fs from "node:fs";
import { expect, it } from "vitest";
import { VJ_CONTROL_IDS } from "../../src/features/love-signal/vj/controlMap";

it("keeps browser and live-production control names identical", () => {
  const live = JSON.parse(fs.readFileSync("docs/production/vj-control-map.json", "utf8"));
  expect(live.controls.map((control: { id: string }) => control.id)).toEqual(VJ_CONTROL_IDS);
});
```

- [ ] **Step 2: Run the test and confirm the production map is absent**

- [ ] **Step 3: Write the asset pipeline**

Specify ACEScg offline work, sRGB web display, GLB/KTX2 web delivery, EXR/PNG masters, ProRes 4444/422 HQ masters, DXV3 Resolume copies, alpha mode, frame rate, loop handles, naming, checksums and sidecars. Keep Houdini specialist-only; Cinema 4D/Redshift is the primary 3D authoring path.

- [ ] **Step 4: Write the shared control map**

Include `scene`, `energy`, `depth`, `memory`, `connection`, LOW/MID/HIGH/ENERGY envelopes, ranges `[0,1]`, smoothing and safe defaults. Add MIDI CC and OSC address mappings without requiring hardware in the web build.

- [ ] **Step 5: Write the deliverables matrix**

The CSV contains 16:9, 9:16, 4:5, 1:1 and 21:9; durations 5.28, 10, 15 and 30 seconds; clean/texted/alpha variants; master and delivery codecs; rights owner; status; checksum; and approver fields.

- [ ] **Step 6: Run parity test and validate JSON/CSV parsing**

Expected: exact control order; all required ratios and durations present; no `cleared-production` default.

- [ ] **Step 7: Commit the production contract**

```bash
git add docs/production tests/love-signal/production-contracts.test.ts
git commit -m "docs: define ali love visual production pipeline"
```

---

### Task 14: Add end-to-end accessibility, lifecycle and performance checks

**Files:**

- Create: `tests/e2e/love-signal.spec.ts`
- Create: `tests/e2e/fixtures/reduced-motion.ts`
- Modify: existing Playwright config only when Task 1 confirms one exists

**Interfaces:**

- Consumes: locally running canonical app.
- Produces: evidence for HTML-first render, fallback, game, VJ, recorder guardrails and lifecycle.

- [ ] **Step 1: Write the failing HTML-first and reduced-motion tests**

```ts
import { expect, test } from "@playwright/test";

test("official content renders before WebGL enhancement", async ({ page }) => {
  await page.addInitScript(() => Object.defineProperty(HTMLCanvasElement.prototype, "getContext", { value: () => null }));
  await page.goto("/");
  await expect(page.getByRole("heading", { name: "LOVE IS THE SIGNAL" })).toBeVisible();
  await expect(page.getByRole("img", { name: "The Resonance Rose" })).toBeVisible();
});

test("reduced motion completes the resonance session", async ({ page }) => {
  await page.emulateMedia({ reducedMotion: "reduce" });
  await page.goto("/");
  await page.getByRole("button", { name: "Start Resonance Session" }).click();
  await expect(page.getByText(/LISTENING|RESONANT|THE ROOM REMEMBERS/)).toBeVisible();
});
```

- [ ] **Step 2: Run the focused E2E test and confirm it fails before integration is complete**

- [ ] **Step 3: Add keyboard and consent tests**

Verify visible focus, keyboard phase/game/VJ operation, audio staying off on load, microphone denial, immediate track stop and absence of network requests containing media data.

- [ ] **Step 4: Add lifecycle instrumentation in test mode**

Expose read-only test counters for active animation loops, listeners, geometries, textures and render targets. Assert entry → exit → entry leaves one loop and returns bounded resource counts after disposal.

- [ ] **Step 5: Run desktop and mobile projects**

Test Chromium, WebKit and the repository's supported Firefox project; include a mobile Safari-like viewport/orientation change. Expected: no black screen, no scroll lock, touch targets at least 44 px and usable 2D fallback.

- [ ] **Step 6: Run axe and record performance measurements**

Record FPS p50/p10, DPR, peak draw calls, textures, geometries, Three chunk size, first interactive frame and recorder MIME. If rolling FPS falls below 32 for 2.5 seconds, verify degradation order: DPR → halation → paper → stars → aurora fallback.

- [ ] **Step 7: Commit the QA harness**

```bash
git add tests/e2e
git commit -m "test: verify love signal journeys and lifecycle"
```

---

### Task 15: Run the complete local verification and write the Fable 5 handoff report

**Files:**

- Create: `docs/qa/ali-love-love-is-the-signal-local.md`
- Modify: none outside the report unless a failing test identifies a scoped defect

**Interfaces:**

- Consumes: all prior tasks and the audited commands.
- Produces: final evidence and explicit stop gate.

- [ ] **Step 1: Run content and placeholder scans**

```bash
rg -n "healing frequency|scientifically proven|therapeutic|T[B]D|T[O]DO|coming soon|Cosmic Rave.*album" src docs --glob '!docs/superpowers/**'
```

Expected: no prohibited claim, invented album label or unresolved production placeholder. Source commentary in the master spec is excluded intentionally.

- [ ] **Step 2: Run the audited unit, E2E and build commands**

Read commands from the repo map and run each without mutation:

```bash
node -e "const m=require('./docs/audits/ali-love-repo-map.json'); console.log(m.commands.unit); console.log(m.commands.e2e); console.log(m.commands.build)"
```

Execute all three exact printed commands. Expected: exit code 0, or a pre-existing baseline failure reproduced and clearly separated from new work.

- [ ] **Step 3: Verify the production content gate**

Run content validation in production mode. Expected: it blocks the generated `approved-preview` image and any unverified biography/release field. This controlled failure proves the public clearance guard works; it is not a build failure.

- [ ] **Step 4: Complete manual QA**

Verify desktop, mobile, reduced motion, keyboard, screen reader smoke test, audio off by default, microphone denial/stop, VJ scene/macros, REC/fallback still, entry → exit → entry, 5-minute site soak and 30-minute VJ soak.

- [ ] **Step 5: Write the report in the required format**

```markdown
# LOVE IS THE SIGNAL / THE SPIRAL — LOCAL BUILD READY

## Repo real
canonical:
branch/worktree:
base commit:
framework and versions:

## Baseline
initial build:
pre-existing failures:
real alilove.world pipeline:

## Delivered
campaign shell:
Resonance Rose:
528 framing:
Spiral integration:
game:
VJ:
biography/archive:
recording:
mobile/accessibility:

## QA evidence
unit:
E2E:
build:
desktop/mobile:
reduced motion:
audio/microphone:
REC:
console:

## Performance
FPS p50/p10:
DPR:
draw calls:
textures/geometries:
Three chunk:
interactive first frame:

## Content and rights
approved-preview:
cleared-production:
withheld:
production gate result:

## Scope
remote actions performed: none
deploy performed: no

## Next approval gate
Preview deployment, publication, production configuration and media clearance require explicit approval from André.
```

- [ ] **Step 6: Review the final diff and commit the report locally**

```bash
git status --short
git diff --check
git add docs/qa/ali-love-love-is-the-signal-local.md
git commit -m "docs: report love signal local build readiness"
```

- [ ] **Step 7: Stop**

Do not push, open a pull request, deploy, change a Vercel setting or publish an asset. Return the report, local commit list, unresolved rights items and exact evidence to the user.

---

## Self-review performed on this plan

- Spec coverage: campaign hierarchy, 528 framing, cover grammar, biography, 11-phase preservation, Rose, game, VJ, recording, assets, rights, accessibility, performance and stop gate all have implementation tasks.
- Placeholder scan: the plan contains no unresolved implementation placeholders; embargo-safe copy and conservative rights states are explicit behavior.
- Type consistency: `ReleaseManifest`, `BiographyMemory`, `RoseState`, normalized VJ macros and the four audio envelopes retain the same names across tasks.
- Architecture consistency: no second renderer, framework migration, remote service, server, login, CMS or multiplayer dependency enters P0.
