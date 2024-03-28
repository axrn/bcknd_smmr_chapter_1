__all__ = ("seconds_to_str",)


def seconds_to_str(seconds: int) -> str:
    """Реализует текстовое представление времени.

    Example:
        >> seconds_to_str(20)
        20s
        >> seconds_to_str(60)
        01m00s
        >> seconds_to_str(65)
        01m05s
        >> seconds_to_str(3700)
        01h01m40s
        >> seconds_to_str(93600)
        01d02h00m00s
    """
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    rest_seconds = seconds % 60

    if seconds < 60:
        return f"{rest_seconds:02}s"
    if seconds < 3600:
        return f"{minutes:02}m{rest_seconds:02}s"
    if seconds < 86400:
        return f"{hours:02}h{minutes:02}m{rest_seconds:02}s"

    return f"{days:02}d{hours:02}h{minutes:02}m{rest_seconds:02}s"
