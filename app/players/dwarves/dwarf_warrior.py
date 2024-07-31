from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(
            self,
            nickname: str,
            hummer_level: int,
            favourite_dish: str
    ) -> None:
        super().__init__(nickname, favourite_dish)
        self._hummer_level = hummer_level

    def player_info(self) -> str:
        return (
            f"Dwarf warrior "
            f"{self.nickname}. "
            f"{self.nickname} "
            f"has a hummer of the "
            f"{self._hummer_level} level"
        )

    def get_rating(self) -> int:
        return self._hummer_level + 4
