# SPDX-License-Identifier: AGPL-3.0-only
# Copyright 2026-present the TuneLabs AI Inc. team. All rights reserved. See /studio/LICENSE.AGPL-3.0

import os as _os
import sys as _sys

import typer
from importlib.metadata import version as package_version, PackageNotFoundError


from tunelabs_cli.commands.train import train
from tunelabs_cli.commands.inference import inference
from tunelabs_cli.commands.chat import chat
from tunelabs_cli.commands.connect import connect_app
from tunelabs_cli.commands.export import export, list_checkpoints
from tunelabs_cli.commands.studio import (
    run as studio_run,
    studio_app,
    _expand_attached_np_short,
)


# Canonicalise `-np<N>` only under the `tunelabs` console-script;
# third-party scripts that import tunelabs_cli keep their argv intact.
_entry_base = _os.path.basename(_sys.argv[0]).lower() if _sys.argv else ""
if _entry_base in {"tunelabs", "tunelabs.exe"}:
    _expand_attached_np_short()
del _entry_base


def show_version(value: bool):
    if value:
        try:
            version = package_version("tunelabs")
        except PackageNotFoundError:
            version = "unknown"
        typer.echo(f"tunelabs {version}")
        raise typer.Exit()


app = typer.Typer(
    help = "Command-line interface for TuneLabs training, inference, and export.",
    context_settings = {"help_option_names": ["-h", "--help"]},
)


@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        "-V",
        callback = show_version,
        is_eager = True,
        help = "Show version and exit.",
    ),
):
    if (
        _sys.platform == "win32"
    ):  # this block catches tunelabs running inside of System32 or any subdirs, this WILL cause errors if not prevented.
        _cwd = _os.path.normcase(_os.path.normpath(_os.getcwd()))
        _system32 = _os.path.normcase(
            _os.path.normpath(_os.path.join(_os.environ.get("WINDIR", r"C:\Windows"), "System32"))
        )
        if _cwd == _system32 or _cwd.startswith(_system32 + _os.sep):
            typer.secho(
                "Refusing to run TuneLabs inside System32 as it will lead to Errors.\n"
                "cd to a normal working directory and try again.",
                fg = "red",
                err = True,
            )
            raise typer.Exit(code = 1)


app.command()(train)
app.command()(inference)
app.command()(chat)
app.command()(export)
app.command("list-checkpoints")(list_checkpoints)
app.add_typer(studio_app, name = "studio", help = "TuneLabs Studio commands.")
app.add_typer(
    connect_app,
    name = "connect",
    help = "Connect a coding agent (Claude Code, Codex) to Studio.",
)

# Top-level `tunelabs run` aliases `tunelabs studio run`; same context
# so unknown flags still pass through to llama-server.
app.command(
    "run",
    context_settings = {
        "allow_extra_args": True,
        "ignore_unknown_options": True,
    },
    help = "Alias for `tunelabs studio run`.",
)(studio_run)
