# -*- encoding: utf-8 -*-

import mobase

from ..basic_features import BasicGameSaveGameInfo
from ..basic_game import BasicGame


class BaldursGate3Game(BasicGame):
    Name = "Baldurs Gate 3 Support Plugin"
    Author = "DjonukOne"
    Version = "1.0.0"

    GameName = "Baldurs Gate 3"
    GameShortName = "baldursgate3"
    GameNexusName = "baldursgate3"
    GameValidShortNames = ["baldursgate3"]
    GameNexusId = 347
    GameSteamId = [1086940]
    GameBinary = "bin/bg3.exe"
    GameDataPath = "Data"
    GameSaveExtension = "lsv"  
    GameDocumentsDirectory = (
        "%USERPROFILE%/AppData/Local/Larian Studios/Baldur's Gate 3"
    )
    GameSavesDirectory = (
        "%USERPROFILE%/AppData/Local/Larian Studios/Baldur's Gate 3/PlayerProfiles"
    )

    def init(self, organizer: mobase.IOrganizer):
        super().init(organizer)
        self._featureMap[mobase.SaveGameInfo] = BasicGameSaveGameInfo(
            lambda s: s.replace(".lsv", ".WebP")  
        )
        return True
