# Battlegrounds Public

[简体中文](README.md) | **English**

An unofficial core implementation and adaptation of battlegrounds gameplay. The current source version is **14.5.0**, marking the closure of the 14.0 development stage. This repository has independent Git history created from a reviewed file allowlist and is intended for code reading, rules research, and further development.

**This is a core source archive, not a directly runnable complete game.** All visual files and their import metadata are omitted, including default placeholder images, project-authored UI artwork, and keyword-effect textures. Source code may still reference these missing files. This repository does not promise a download-and-play experience and does not include an engine binary or executable release.

For runnable source and a Windows download, see [battlegrounds-open](https://github.com/ctyyytc/battlegrounds-open) and its [v14.5.0 release](https://github.com/ctyyytc/battlegrounds-open/releases/tag/v14.5.0).

## Contents

| Directory | Purpose |
| --- | --- |
| `battlegrounds/domain/` | Rules, state, random streams, saving/loading, and resource loading |
| `battlegrounds/ui/`, `battlegrounds/app/` | UI and application-entry source; visual dependencies must be prepared separately |
| `battlegrounds/content/` | Functional definitions, compatibility IDs, and default placeholder data |
| `battlegrounds/resource_contract/` | Neutral interfaces for external text/images, base numeric fields, and image keys |
| `battlegrounds/tools/` | Offline content-pack templates, validation, and local subset-copy tools |
| `battlegrounds/examples/` | An empty content-pack example without original game artwork or text |

The source project uses Godot 4.x. Its application name and user-data directory, `battlegrounds-o`, are retained for local data isolation. Project files live under `battlegrounds/`. See [LICENSE](LICENSE) for the software license and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for dependency and asset boundaries.

## External content interface

Run these offline tools from the repository root with Python 3.10 or later. They use only the standard library and do not download content:

```sh
python battlegrounds/tools/resource_pack.py template --output my-pack
python battlegrounds/tools/resource_pack.py check --pack my-pack/pack.json
```

The template contains default placeholder values and empty display fields; it does not restore original artwork, descriptions, or a pack of original base values. Users must supply external resources they have the appropriate rights to use. Importing a content pack does not supply all built-in visual dependencies omitted from this archive. Creating a runnable project requires preparing those resources and validating the result separately. See [RESOURCE_PACKS.md](battlegrounds/RESOURCE_PACKS.md) for the interface.

## Behavior and validation boundaries

The source includes starting with a full legal hero list or three candidates, shared settings, reminders for available trinket choices, saving after the start-of-round choice chain completes, a rolling undo history of the last three complete recruitment actions, and related rules fixes. Settings preserve the existing pause state. Undo has no usage-count limit but remains subject to round and phase boundaries.

The complete original project at a fixed 14.5.0 source identity passed eight groups of 522 selected independent checks, including representative hero-power additions and cross-process save/load checks. Those results apply to that original fixed source and named scope; they do not certify this public subset as runnable. This subset was checked for file identity, publication scope, and offline tools. Godot startup, full natural matches, all content combinations, and a complete resource-pack installation/uninstallation UI matrix were not run against this subset.

## Unofficial project and license

This is an unofficial recreation and adaptation of gameplay associated with Hearthstone Battlegrounds, shared free of charge by the maintainer without monetization. It is not affiliated with, partnered with, or endorsed by Blizzard Entertainment. Compatibility IDs are used only for functional associations.

The repository does not contain original artwork, original card descriptions, private resource packs, or historical source materials, and provides no download links or automatic acquisition tool for them. Internal workflow records, pre-existing private Git history, player saves, screenshots, raw test states, and development plugins are excluded.

The maintainer selected **MIT**: modification, redistribution, and commercial use are permitted under its terms, with the copyright and license notices retained. The maintainer's decision to share the project free of charge adds no downstream restriction on commercial use. MIT does not grant rights to third-party images, text, trademarks, or separately obtained assets.

## Contact

Maintainer email: [2571114956@qq.com](mailto:2571114956@qq.com).
