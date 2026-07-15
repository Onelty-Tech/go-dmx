# Go DMX - DMX512 Lighting Control Library for Golang

A **DMX512 library for Go (Golang)** focused on controlling DMX interfaces and lighting fixtures.

This project provides a foundation for building **lighting controllers**, **show control software**, **automation systems**, or any application that needs to communicate with **DMX512-compatible devices**.

## Features

- DMX512 communication from Go.
- DMX port management.
- Basic lighting fixture control.
- Extensible architecture for fixture abstractions.
- Improved implementation based on an older abandoned DMX library.
- Open source and easy to modify.

## Project Status

> **Status:** Archived / Maintenance only.

The project is no longer under active development, but the core library is functional.

Current state:

- ✅ DMX port communication works.
- ✅ Fixture control API is usable.
- ✅ Core DMX functions have been improved.
- 🚧 Chase recording/playback system was started but never completed.
- 🚧 An experimental desktop controller is included but unfinished.

## Why this project?

Originally, this repository was created as a continuation of an abandoned Go DMX library that I found years ago.

Instead of letting the work disappear, I decided to improve it, expand its capabilities, and eventually release the source code so others can benefit from it.

## Who is it for?

This library may be useful if you're building:

- DMX lighting controllers
- Theater lighting software
- Stage automation
- Show control systems
- Home automation using DMX
- Interactive installations
- Custom lighting fixtures
- Embedded Go applications that output DMX

## Production Use

The library is suitable if you simply need to send DMX data to compatible devices.

For advanced lighting features (scenes, chases, effects, cue lists, automation, etc.), you should expect to extend or maintain the existing code.

## Contributions

Although the project is archived, pull requests, bug fixes, and improvements are welcome.
