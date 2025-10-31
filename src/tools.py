# ~/.gemini/extensions/mcp/tools.py
"""A collection of example tools for the example MCP server."""

import math


def modulus(a: int, b: int) -> int:
  """Calculates the modulus of two integers.

  Args:
    a: The dividend.
    b: The divisor.

  Returns:
    The remainder of a divided by b.
  """
  return a % b


def sqrt(a: float) -> float:
  """Calculates the square root of a number.

  Args:
    a: The number.

  Returns:
    The square root of a.
  """
  return math.sqrt(a)
