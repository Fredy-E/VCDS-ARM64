<h1 align="center">VCDS ARM64</h1>

<p align="center">
  <strong>Compatibility notes for running <a href="https://www.ross-tech.com/vcds/">Ross-Tech VCDS</a> on Windows 11 on ARM64</strong> (Snapdragon X / Windows on ARM).<br>
  Original material only — no Ross-Tech code, binaries, or firmware is included or redistributed.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/platform-Windows%2011%20ARM64-29354b?style=flat-square" alt="Windows 11 ARM64">
  <img src="https://img.shields.io/badge/material-original%20only-c7a366?style=flat-square" alt="Original material only">
  <img src="https://img.shields.io/badge/license-MIT-737373?style=flat-square" alt="License: MIT">
</p>

## Scope

- This repository contains only original, self-authored material.
- **No Ross-Tech code, binaries, or firmware** is included or redistributed.
- **Nothing here modifies or bypasses any license, activation, or protection mechanism.** You need your own licensed VCDS installation and a genuine Ross-Tech interface (e.g. HEX-V2).

## Verified notes (Windows 11 ARM64)

- VCDS 24.x (x86) runs on Windows 11 ARM64 in **USB interface mode** under the built-in x86 emulation.
- Setting a COM port in VCDS configuration breaks interface detection on this platform — the USB-mode path is the working one.

## Related

- [USBPcap-ARM64](https://github.com/Fredy-E/USBPcap-ARM64) — unofficial native ARM64 port of USBPcap: USB packet capture for Windows on ARM.

## Disclaimer

Community interoperability notes. Not affiliated with, endorsed by, or sponsored by Ross-Tech. "VCDS" is a trademark of Ross-Tech.

## Contact

Questions about this project: **fff.eid607@gmail.com**
