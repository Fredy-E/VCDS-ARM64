# Reproduction template (maintainers)

Use this template when recording a new observation for [EVIDENCE.md](EVIDENCE.md). Copy it into a new file (for example `docs/observations/YYYY-MM-DD-<short-slug>.md`) or a PR description.

**Rules**

- Only genuine, licensed VCDS installations with genuine Ross-Tech hardware.
- Record unknowns as **"not recorded"** — never guess, and never leave a field silently blank.
- Do not include VINs, serial numbers, license/activation data, raw logs, or anything else that identifies a vehicle or person.
- Separate what you *observed* from what you *infer*. Quote official guidance with a source link; do not restate it as your own finding.

---

## Observation record

- **Date (YYYY-MM-DD):**
- **Reporter (maintainer / contributor):**
- **Machine:** CPU/SoC: ____ | RAM: ____ | Windows edition: ____ | Windows build (`winver`): ____
- **VCDS:** exact version and build (Help → About): ____ | architecture shown (x86 / ARM64): ____ | install path: ____
- **Interface:** model (HEX-V2 / HEX-NET / other): ____ | firmware version: ____ | connection used (USB / WiFi): ____
- **Driver / device info (Device Manager):** device name: ____ | provider + version: ____ | COM port present (Y/N): ____
- **Vehicle context:** model/year only, and only if non-identifying and relevant: ____
- **Scenario (step by step):**
  1. ____
  2. ____
- **Observed result (exact behavior, error text — redact personal data):**
- **Repeated?** first observation / reproduced N times / could not reproduce
- **What was NOT tested / not recorded:**
- **Attachments:** screenshots only if they contain no VIN, serial, or license data: ____

## Maintainer review checklist

- [ ] Unknowns marked "not recorded" (not guessed, not left blank).
- [ ] No VINs, serials, license data, or identifying logs included.
- [ ] Claims match exactly what was observed; official guidance quoted with a source link.
- [ ] Entry added to [EVIDENCE.md](EVIDENCE.md) with an explicit scope note (single machine, date, versions).
