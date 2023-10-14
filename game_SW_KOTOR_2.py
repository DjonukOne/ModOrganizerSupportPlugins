# -*- encoding: utf-8 -*-

from PyQt5.QtCore import QFileInfo

import mobase

from ..basic_game import BasicGame


class StarWarsKOTOR2ModDataChecker(mobase.ModDataChecker):
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


class StarWarsKOTOR2Game(BasicGame):
    Name = "Star Wars KOTOR 2 Support Plugin"
    Author = "DjonukOne"
    Version = "0.1"

    GameName = "Star Wars: Knights of the Old Republic 2"
    GameShortName = "kotor2"
    GameNexusName = "kotor2"
    GameNexusId = 198
    GameSteamId = 208580
   # GameGogId = 1453375253
    GameBinary = "swkotor2.exe"
    GameDataPath = "%GAME_PATH%"
    GameDocumentsDirectory = "%Game_PATH"
    GameSavesDirectory = "saves"

    def init(self, organizer: mobase.IOrganizer):
        super().init(organizer)
        self._featureMap[mobase.ModDataChecker] = StarWarsKOTOR2ModDataChecker()
        return True

    def executables(self):
        return [
            mobase.ExecutableInfo(
                "SW Kotor 2", QFileInfo(self.gameDirectory(), "swkotor2.exe")
            ),
            mobase.ExecutableInfo(
                "Launcher", QFileInfo(self.gameDirectory(), "launcher.exe")
            ),
            mobase.ExecutableInfo(
                "SW Config", QFileInfo(self.gameDirectory(), "swconfig.exe")
            ),
        ]
        