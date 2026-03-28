def _apply_tax(amount: float, tax_rate: float = 0.15) -> float:
    """Verilen tutara vergi/markup uygular ve sonucu döner."""
    return amount * (1 + tax_rate)

def _format_total_string(amount: float) -> str:
    """Yazdırma için biçimlenmiş toplam metnini döner."""
    return f"Total: {amount:.2f}"

def _append_to_log(results: list[float], filename: str = "log.txt") -> None:
    """Sonuç listesini belirtilen log dosyasına ekler."""
    with open(filename, "a") as f:
        f.write(str(results) + "\n")

def process_data(data, tax_rate: float = 0.15, log_file: str = "log.txt"):
    """
    Verilen sayı listesini işler:
    - Her bir değere vergi uygular,
    - Biçimlenmiş toplamı yazdırır,
    - Sonuçları log dosyasına ekler ve liste olarak döner.
    """
    processed = []
    for value in data:
        taxed_value = _apply_tax(value, tax_rate)
        print(_format_total_string(taxed_value))
        processed.append(taxed_value)

    _append_to_log(processed, log_file)
    return processed
