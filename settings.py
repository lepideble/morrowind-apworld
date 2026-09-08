from settings import Group, FilePath


class MorrowindSettings(Group):
    class MorrowindEsmPath(FilePath):
        """Path to Morrowind.esm"""
        description = "Morrowind.esm"

    class Tes3convPath(FilePath):
        """Path to tes3conv"""
        description = "tes3conv"
        is_exe = True

    class OpenMWArchipelago(FilePath):
        """Path to openmw-archipelago"""
        description = "openmw-archipelago"
        is_exe = True

    morrowind_esm_path: MorrowindEsmPath = MorrowindEsmPath()
    tes3conv_path: Tes3convPath = Tes3convPath()
    openmw_archipelago_path: OpenMWArchipelago = OpenMWArchipelago()
