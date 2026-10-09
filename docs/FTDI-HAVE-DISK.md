# FTDI USB driver install (Have Disk method)

> **Scope.** Installing FTDI's own USB serial drivers on Windows 11 ARM64
> for FTDI-based legacy cables (e.g. HEX-USB). No driver files are hosted
> here — download them from FTDI directly. No bypass, patching, modified
> drivers, or disabled protections are involved.

## What you need

- A genuine Ross-Tech interface and your own licensed VCDS installation.
- Windows 11 on ARM64 (e.g. Snapdragon X).
- FTDI's official CDM driver package for ARM64, from
  <https://ftdichip.com/drivers/vcp-drivers/> (verify the URL before
  downloading; never use a random re-upload).
- The cable plugged in so Device Manager shows the device (typically with a
  warning icon until the driver is installed).

## Steps

1. Extract FTDI's official package to a local folder. Note the folder path —
   you will point Device Manager at it twice.
2. Open Device Manager and find the cable device (e.g. "Ross-Tech HEX-USB"
   with a yellow warning icon).
3. Right-click it → **Update driver** → **Browse my computer for drivers** →
   **Let me pick from a list of available drivers**.
4. Click **Have Disk…**, browse to the extracted folder, and select
   `FTDIBUS.inf` → OK. Choose **USB Serial Converter** → Install.
5. Back in Device Manager, find the new **USB Serial Converter** device.
6. Repeat steps 3–4 on it, this time selecting `FTDIPORT.inf` → OK. Choose
   **USB Serial Port (COMn)** → Install. Note the assigned COM port number.
7. Confirm in VCDS under Options / port settings that the interface is found.

## Checks

- Device Manager shows **USB Serial Converter** and **USB Serial Port
  (COMn)**, both status OK.
- In PowerShell, `[System.IO.Ports.SerialPort]::GetPortNames()` lists the
  port.
- VCDS detects the interface. (On this project's test machine the working
  VCDS path is USB interface mode — see [docs/EVIDENCE.md](EVIDENCE.md).)

## Warnings — read before clicking through anything

- **Only install the official FTDI package.** If Windows warns the driver
  does not match the hardware, stop and re-check that you downloaded the
  correct ARM64 package from FTDI. Do not install driver files from
  untrusted sources.
- **Do not disable driver signature enforcement, Secure Boot, or Test Mode
  workarounds** to force a driver to load. If a driver will not load with
  those protections on, that is a signal to stop, not to lower them.
- **Never use modified `.inf`/`.sys` files.** Editing FTDI's files breaks
  their signature and turns a routine install into untrusted-driver
  territory.
- Windows Update can replace a manually installed driver. If the cable stops
  being detected after an update, redo these steps with the official
  package.
- This covers the USB serial transport only. It does not change VCDS
  licensing, and nothing here bypasses, patches, or alters any license,
  activation, or interface check.

## Why this page is safe

- Contains no binaries, no `.sys`/`.inf`/`.dll` files, no download mirrors.
- Points only at the vendor's official source.
- Instructs no protection to be disabled and no file to be modified.
