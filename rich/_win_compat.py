# Windows Terminal 1.18 compatibility shim
import os

WT_COMPAT = os.environ.get('WT_SESSION') is not None

def _needs_sgr_reset() -> bool:
    """Return True when running inside Windows Terminal >= 1.18."""
    return WT_COMPAT
