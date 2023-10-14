# -*- encoding: utf-8 -*-

from PyQt5.QtCore import QFileInfo

import mobase

from ..basic_game import BasicGame


class StarWarsKOTOR1ModDataChecker(mobase.ModDataChecker):
    def __init__(self):
        super().__init__()

    def dataLooksValid(
        self, tree: mobase.IFileTree
    ) -> mobase.ModDataChecker.CheckReturn:

        for e in tree:
            if e.isDir() and e.exists(  # type: ignore
                "manifest.json", mobase.IFileTree.FILE
            ):
                return mobase.ModDataChecker.VALID

        return mobase.ModDataChecker.INVALID


class StarWarsKOTOR1Game(BasicGame):
    Name = "Star Wars KOTOR 1 Support Plugin"
    Author = "DjonukOne"
    Version = "0.1"

    GameName = "Star Wars: Knights of the Old Republic"
    GameShortName = "kotor"
    GameNexusName = "kotor"
    GameNexusId = 234
    GameSteamId = 32370
   # GameGogId = 1453375253
    GameBinary = "swkotor.exe"
    GameDataPath = "%GAME_PATH%"
    GameDocumentsDirectory = "%Game_PATH"
    GameSavesDirectory = "saves"

    def init(self, organizer: mobase.IOrganizer):
        super().init(organizer)
        self._featureMap[mobase.ModDataChecker] = StarWarsKOTOR1ModDataChecker()
        return True

    def executables(self):
        return [
            mobase.ExecutableInfo(
                "SW Kotor", QFileInfo(self.gameDirectory(), "swkotor.exe")
            ),
            mobase.ExecutableInfo(
                "Launcher", QFileInfo(self.gameDirectory(), "launcher.exe")
            ),
            mobase.ExecutableInfo(
                "SW Config", QFileInfo(self.gameDirectory(), "swconfig.exe")
            ),
        ]
        