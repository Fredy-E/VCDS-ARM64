# Evidence — what has been observed, and what has not

This page is the honesty ledger for this repository. Every statement here is either a **published local observation** from the original maintainer's machine or **general guidance quoted from official documentation** (Ross-Tech / Microsoft), with a source link. Nothing else is claimed.

## Published observations (single machine)

These two notes are the entire published evidence base for this repository:

1. **VCDS 24.x (x86) runs on Windows 11 ARM64 in USB interface mode** under the built-in x86 emulation.
2. **Setting a COM port in VCDS configuration breaks interface detection** on this platform; the USB-mode path is the working one.

They come from one machine (the original maintainer's) and are an anecdote — not a hardware validation matrix. No second machine, no other interface model, and no other VCDS build has been recorded.

## Versioned validation table

State of the published notes. Unknown fields are explicitly **not recorded** — no value has been invented or back-filled.

| Field | Recorded value | Basis |
| --- | --- | --- |
| VCDS version | 24.x (exact build **not recorded**) | local observation |
| Windows | Windows 11 on ARM64 (exact build/edition **not recorded**) | local observation |
| Interface mode | USB interface mode, under x86 emulation | local observation |
| COM-port behavior | Setting a COM port breaks interface detection | local observation |
| Interface model (HEX-V2 / HEX-NET / other) | **Not recorded** | — |
| Interface firmware version | **Not recorded** | — |
| Interface revision / serial batch | **Not recorded** (and deliberately not published) | — |
| Driver / INF version | **Not recorded** | — |
| Date of observation | **Not recorded** | — |
| CPU / SoC | **Not recorded** | — |
| Vehicle, VIN, module, or license details | **Not recorded** (and deliberately not published) | — |

"Not recorded" means exactly that: the information was never captured, and it is not being guessed at now.

## What official sources say (general guidance — not local verification)

- **Supported interfaces on ARM:** "Windows on ARM is only supported with the HEX-NET and HEX-V2" — [Ross-Tech FAQ 1.4](https://www.ross-tech.com/vag-com/faq_1.php).
- **Native ARM builds:** "As of Release 22.3, we have included native builds for machines with ARM CPUs running Windows 10 or 11 only with HEX-NET or HEX-V2 interfaces" — [Ross-Tech download page](https://www.ross-tech.com/vcds/download/current.php).
- **HEX-V2 driver model:** "The HEX-V2 enumerates as an HID device and does not require a special driver" — [Ross-Tech HEX-V2 page](https://www.ross-tech.com/vcds/hex-v2.php).
- **Legacy interface driver model:** the legacy HEX-USB "requires a special driver to be installed on your PC" — [Ross-Tech HEX-USB page](https://www.ross-tech.com/vag-com/old-interfaces/hex-usb.html).
- **Emulation does not run drivers:** "emulation only supports user mode code and doesn't support drivers. Any kernel mode components must be compiled as Arm64" — [Microsoft: How emulation works on Arm](https://learn.microsoft.com/en-us/windows/arm/apps-on-arm-x86-emulation).

**Scope statement:** none of the above is local verification that any specific interface + driver + firmware combination works on ARM64 beyond the single-machine notes above. If you need certainty for your setup, treat Ross-Tech's supported configuration as the baseline and verify on your own hardware.

## Adding evidence

New observations are welcome. Use [REPRODUCTION-TEMPLATE.md](REPRODUCTION-TEMPLATE.md), and record unknowns as "not recorded" rather than leaving them blank or guessing. Do not include VINs, serial numbers, license data, or raw logs containing personal data.
