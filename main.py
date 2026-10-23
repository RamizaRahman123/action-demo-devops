"""Simple demo module for GitHub Actions."""


def greet(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b


def main() -> None:
    """Run the demo."""
    print(greet("DevOps"))
    print(f"2 + 3 = {add(2, 3)}")


if __name__ == "__main__":
    main()
