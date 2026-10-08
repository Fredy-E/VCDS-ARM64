# Troubleshooting — VCDS on Windows 11 ARM64

Each item is labeled **Local observation** (from the original maintainer's single machine — see [EVIDENCE.md](EVIDENCE.md)) or **General guidance** (quoted from official Ross-Tech / Microsoft documentation).

## Interface is not detected after configuring a COM port

**Local observation (single machine):** setting a COM port in VCDS configuration broke interface detection on the maintainer's machine; the USB-mode path was the one that worked.

**General guidance (why this is plausible):** a current interface such as the HEX-V2 "enumerates as an HID device and does not require a special driver" and is not a COM-port device at all ([Ross-Tech HEX-V2 page](https://www.ross-tech.com/vcds/hex-v2.php)). A COM-port selection has no role in that model.

**Action:** leave COM-port selection alone; use the USB interface path. Then in VCDS: [Options] → [Test] "to confirm that the program can use the port and find the interface" → [Save] ([Ross-Tech download instructions](https://www.ross-tech.com/vcds/download/current.php)). If detection still fails, treat it as a product issue and use Ross-Tech's official channels: [support policy](https://www.ross-tech.com/vag-com/support.php) and [forum](https://forums.ross-tech.com/).

## A legacy interface (HEX-USB, HEX-USB+CAN, Micro-CAN, older) does not work

**General guidance:** three official reasons stack up here.

- Windows on ARM "is only supported with the HEX-NET and HEX-V2" ([FAQ 1.4](https://www.ross-tech.com/vag-com/faq_1.php)) — legacy interfaces are not a supported configuration on this platform.
- Legacy interfaces depend on their own kernel-mode USB drivers, and Microsoft states that "emulation only supports user mode code and doesn't support drivers. Any kernel mode components must be compiled as Arm64" ([Microsoft: How emulation works on Arm](https://learn.microsoft.com/en-us/windows/arm/apps-on-arm-x86-emulation)). A non-ARM64 kernel driver cannot run, emulation or not.
- Ross-Tech additionally notes: "As of April, 2026 updates to Windows 11 may prevent the USB drivers for legacy interfaces from loading per The Windows Driver Policy" ([download page](https://www.ross-tech.com/vcds/download/current.php); policy background: [Microsoft — The Windows Driver Policy](https://support.microsoft.com/en-us/windows/the-windows-driver-policy-ecd2a78c-750c-415d-93f2-e37302ce0443)), and recommends legacy users "stick with a PC using an older OS or taking advantage of our trade-in program".

**Action:** use a current interface (HEX-V2 or HEX-NET) with the current release, or use legacy hardware on a non-ARM PC. Do not attempt driver workarounds.

## HEX-NET WiFi problems on ARM

**General guidance:** "Computers with ARM CPUs may not work well with some HEX-NET interfaces via WiFi. This occurs primarily with the original HEX-NET in black shells and serial numbers starting with 'HN1'. If you encounter this problem, please use the supplied USB cable as a temporary work-around" ([Ross-Tech download page](https://www.ross-tech.com/vcds/download/current.php)).

**Action:** use USB mode.

## Performance or emulation quirks

**General guidance:** on Windows 11 on Arm, x86/x64 apps run under emulation (Prism since Windows 11 24H2), and Microsoft documents optional per-app emulation compatibility settings ([Microsoft: Adjust emulation settings on Arm](https://learn.microsoft.com/en-us/windows/arm/apps-on-arm-program-compat-troubleshooter)). For VCDS, use the current official release from Ross-Tech — which ships native ARM64 builds for HEX-NET/HEX-V2 since Release 22.3 ([download page](https://www.ross-tech.com/vcds/download/current.php)) — rather than pinning old builds.

## What this repository cannot help with

- License, activation, or "unlock" problems — those are handled only by Ross-Tech, with genuine hardware. Nothing here bypasses or modifies any protection mechanism.
- Third-party interfaces or modified software.
- Vehicle repair decisions.

Community interoperability notes; not affiliated with, endorsed by, or sponsored by Ross-Tech. "VCDS" is a trademark of Ross-Tech, LLC.
