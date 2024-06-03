class KriptoValuta:
    def __init__(
        self,
        ime,
        vrijednost,
        trend_24h,
        trend_24h_vrijednost,
        trend_7d,
        trend_7d_vrijednost,
    ) -> None:
        self.ime = ime
        self.vrijednost = vrijednost
        self.trend_24h = trend_24h
        self.trend_24h_vrijednost = trend_24h_vrijednost
        self.trend_7d = trend_7d
        self.trend_7d_vrijednost = trend_7d_vrijednost

    def __str__(self) -> str:
        return f"{self.ime}, {self.vrijednost}, 24H: {self.trend_24h_vrijednost} ({self.trend_24h}), 7D: {self.trend_7d_vrijednost} ({self.trend_7d})"
