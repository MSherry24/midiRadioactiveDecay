import driver, chordMappings

maxHalfLifeInMinutes = 0.1
numberOfAtoms = 50
chordMapping = chordMappings.CMajToFMaj()

driver.main(maxHalfLifeInMinutes, numberOfAtoms, chordMapping)