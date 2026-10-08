# Setup — VCDS on Windows 11 ARM64

How to get a **genuine, licensed VCDS installation** talking to a car on Windows 11 on ARM64. This page mixes two kinds of information and labels them:

- **General guidance (official)** — quoted from Ross-Tech or Microsoft documentation, with sources.
- **Local observation (single machine)** — from the original maintainer's machine only; see [EVIDENCE.md](EVIDENCE.md) for the full scope and the "not recorded" fields.

## Requirements (genuine hardware and license only)

- **A genuine Ross-Tech interface.** Ross-Tech states that "Windows on ARM is only supported with the HEX-NET and HEX-V2" ([Ross-Tech FAQ 1.4](https://www.ross-tech.com/vag-com/faq_1.php)). Legacy interfaces (HEX-USB, HEX-USB+CAN, Micro-CAN, and older) are not a supported path on ARM64 — [TROUBLESHOOTING.md](TROUBLESHOOTING.md) explains why, with sources.
- **The official VCDS software**, from Ross-Tech's own download page. As of Release 22.3, Ross-Tech ships "native builds for machines with ARM CPUs running Windows 10 or 11 only with HEX-NET or HEX-V2 interfaces" ([Ross-Tech download page](https://www.ross-tech.com/vcds/download/current.php)).
- **A licensed installation.** Ross-Tech's current release "must be used with a licensed Ross-Tech interface" (same page). This project does not provide, link to, or describe any license, activation, or protection bypass — none is included here, and none will be.

> This repository is documentation only. It does not include, host, or modify any Ross-Tech software, binaries, firmware, or drivers.

## Steps

1. **Install VCDS from Ross-Tech's official download page.** Ross-Tech notes it is "essential NOT to install in the \Program Files\ tree on systems running Windows Vista or newer"; the documented default is `C:\Ross-Tech\VCDS\`.
2. **Connect a HEX-V2 or HEX-NET by USB.** (HEX-V2 is USB-only; HEX-NET also supports WiFi — but see the WiFi caveat on ARM in [TROUBLESHOOTING.md](TROUBLESHOOTING.md).)
3. **In VCDS: [Options] → select the interface → [Test] → [Save].** Ross-Tech's documented workflow: "Use [Test] to confirm that the program can use the port and find the interface. Then [Save]."
4. **Keep interface firmware current** while you have internet access. Ross-Tech notes internet is required to update firmware in HEX-NET/HEX-V2 interfaces.

## Local observation (single machine)

On the original maintainer's Windows 11 ARM64 machine, **VCDS 24.x (x86) runs in USB interface mode** under the built-in x86 emulation — that is the path that worked. **Setting a COM port in VCDS configuration broke interface detection** on that machine.

This is one machine's observation, not a compatibility matrix. Exact Windows build, interface model, firmware, and driver versions were not recorded — see the versioned table in [EVIDENCE.md](EVIDENCE.md).

## Do not

- **Do not use third-party interfaces with full VCDS.** Ross-Tech states the current release does not work with "any third-party interfaces or some of the older 'low-tech' interfaces we made and sold before 2004" ([download page](https://www.ross-tech.com/vcds/download/current.php)).
- **Do not attempt driver or license workarounds.** For product issues, use Ross-Tech's official channels: [support policy](https://www.ross-tech.com/vag-com/support.php) and [forum](https://forums.ross-tech.com/).
