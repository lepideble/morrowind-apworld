from ...locations import LocationData
from ...quests import ThePathOfTheIncarnate


name = 'Cavern of the Incarnate'


locations = {
    'Pick Moon and Star': LocationData(
        events=[ThePathOfTheIncarnate.Completed],
    ),
}
