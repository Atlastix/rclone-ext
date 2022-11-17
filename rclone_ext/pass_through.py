"""Passthrough shim for Rclone extension."""
import sys

import structlog
from meltano.edk.logging import pass_through_logging_config
from rclone_ext.extension import Rclone


def pass_through_cli() -> None:
    """Pass through CLI entry point."""
    pass_through_logging_config()
    ext = Rclone()
    ext.pass_through_invoker(
        structlog.getLogger("rclone_invoker"),
        *sys.argv[1:] if len(sys.argv) > 1 else []
    )
