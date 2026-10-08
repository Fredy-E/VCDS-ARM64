<h1 align="center">VCDS ARM64</h1>

<p align="center">
  <strong>Compatibility notes for running <a href="https://www.ross-tech.com/vcds/">Ross-Tech VCDS</a> on Windows 11 on ARM64</strong> (Snapdragon X / Windows on ARM).<br>
  Documentation only — no Ross-Tech code, binaries, firmware, or drivers are included or redistributed.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/platform-Windows%2011%20ARM64-29354b?style=flat-square" alt="Windows 11 ARM64">
  <img src="https://img.shields.io/badge/material-original%20only-c7a366?style=flat-square" alt="Original material only">
  <img src="https://img.shields.io/badge/license-MIT-737373?style=flat-square" alt="License: MIT">
</p>

## Scope

- **Documentation only.** Original, self-authored material (MIT — see [LICENSE](LICENSE)). No Ross-Tech code, binaries, firmware, installers, or drivers are included or redistributed.
- **Genuine, licensed setups only.** You need your own licensed VCDS installation and a genuine Ross-Tech interface (current generation: HEX-V2 or HEX-NET). Nothing here modifies or bypasses any license, activation, or protection mechanism.
- **Honest evidence.** Every claim is either a single-machine observation or quoted official guidance, labeled and linked. Unknowns are marked "not recorded" rather than guessed.

## Documentation

| Document | Contents |
| --- | --- |
| [docs/SETUP.md](docs/SETUP.md) | Getting a genuine, licensed setup working in USB mode on Windows 11 ARM64 |
| [docs/EVIDENCE.md](docs/EVIDENCE.md) | What has actually been observed; versioned table of not-recorded fields; quoted official guidance |
| [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) | COM-port detection issue, legacy interfaces on ARM, HEX-NET WiFi caveat |
| [docs/REPRODUCTION-TEMPLATE.md](docs/REPRODUCTION-TEMPLATE.md) | Maintainer template for recording new observations |
| [docs/releases/v0.1.0.md](docs/releases/v0.1.0.md) | Documentation-only release draft (not published) |

Doc link checks: `python3 tools/check_docs.py` — dependency-free (Python stdlib only); also run by the docs-only CI workflow.

## Observed notes (single machine — not a compatibility matrix)

- VCDS 24.x (x86) runs on Windows 11 ARM64 in **USB interface mode** under the built-in x86 emulation.
- Setting a COM port in VCDS configuration breaks interface detection on this platform — the USB-mode path is the working one.

Exact Windows build, interface model, firmware, and driver versions were not recorded. Full scope and the versioned table: [docs/EVIDENCE.md](docs/EVIDENCE.md).

## Related

- [USBPcap-ARM64](https://github.com/Fredy-E/USBPcap-ARM64) — unofficial native ARM64 port of USBPcap: USB packet capture for Windows on ARM.

## Disclaimer

Community interoperability notes. Not affiliated with, endorsed by, or sponsored by Ross-Tech. "VCDS" is a trademark of Ross-Tech, LLC.

## Contact

Questions about this project: **fff.eid607@gmail.com**
