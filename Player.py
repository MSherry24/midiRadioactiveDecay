import mido

def getOutport():
	outport = mido.open_output(mido.get_output_names()[0])

def clearMidiChannels():
	outport = mido.open_output(mido.get_output_names()[0])
	for x in range(15):
		for y in range(127):
			m = mido.Message('note_off', note=y, channel=x)
			outport.send(m)

def getMidoMessage(note, octave, channel):
	noteValue = note + 12 * octave;
	noteValue = adjustOctaves(noteValue)
	return mido.Message('note_on', note=noteValue, channel=channel)

def getChord(root, type='M'):
	chordMap = getChordMap()
	noteMap = getNoteMap()
	triad = chordMap[root]
	chord = []
	for x in range(len(triad)):
		note = noteMap[triad[x]]
		chord.append(noteMap[triad[x]])
	chord = addChordExtensions(chord, type)
	return chord

def addChordExtensions(chord, type):
	if (type == 'M'):
		return chord
	if (type == 'm'):
		return minorChord(chord)
	if (type == '7'):
		return dominantSeventhChord(chord)
	if (type == 'm7'):
		return minorSeventhChord(chord)
	if (type == 'dim'):
		return diminishedChord(chord)
	if (type == 'dim7'):
		return diminishedSeventhChord(chord)
	if (type == 'sus2'):
		return sus2Chord(chord)
	if (type == 'sus4'):
		return sus2Chord(chord)
	if (type == '9'):
		return ninthChord(chord)
	if (type == 'm9'):
		return minorNinthChord(chord)
	if (type == '11'):
		return eleventhChord(chord)
	if (type == 'm11'):
		return minorEleventhChord(chord)
	if (type == '13'):
		return thirteenthChord(chord)
	if (type == 'm13'):
		return minorThirteenthChord(chord)
		

def minorChord(chord):
	chord[1] = chord[1] - 1
	return chord

def dominantSeventhChord(chord):
	fifth = chord[2]
	chord.append(fifth + 3)
	return chord

def minorSeventhChord(chord):
	chord = minorChord(chord)
	chord = dominantSeventhChord(chord) 
	return chord

def flatFifth(chord):
	chord[2] = chord[2] - 1
	return chord

def diminishedChord(chord):
	chord = minorChord(chord)
	chord = flatFifth(chord)
	return chord

def diminishedSeventhChord(chord):
	chord = minorSeventhChord(chord)
	chord = diminishedChord(chord)
	return chord

def sus2Chord(chord):
	second = chord[0] + 2
	return [chord[0], second, chord[1], chord[2]]

def sus4Chord(chord):
	fourth = chord[1] + 1
	return [chord[0], chord[1], fourth, chord[2]]

def ninthChord(chord):
	chord = dominantSeventhChord(chord)
	ninth = chord[0] + 14
	chord.append(ninth)
	return chord

def minorNinthChord(chord):
	chord = minorSeventhChord(chord)
	ninth = chord[0] + 14
	chord.append(ninth)
	return chord

def eleventhChord(chord):
	chord = ninthChord(chord)
	eleventh = chord[0] + 17
	chord.append(eleventh)
	return chord

def minorEleventhChord(chord):
	chord = minorNinthChord(chord)
	eleventh = chord[0] + 17
	chord.append(eleventh)
	return chord

def thirteenthChord(chord):
	chord = eleventhChord(chord)
	thirteenth = chord[0] + 21
	chord.append(thirteenth)
	return chord

def minorThirteenthChord(chord):
	chord = minorEleventhChord(chord)
	thirteenth = chord[0] + 21
	chord.append(thirteenth)
	return chord

def adjustOctaves(noteValue):
	if (noteValue < 0):
		while (noteValue < 0):
			noteValue += 12
	if (noteValue > 127):
		while (noteValue > 127):
			noteValue -= 12
	return noteValue

def getChordNoteArray(chord):
	return chordMap[chord]

def getChordMap():
	return chordMap

def getNoteMap():
	return noteMap

noteMap = {
	'C' : 60,
	'C#' : 61,
	'Db' : 61,
	'D' : 62,
	'D#' : 63,
	'Eb' : 63,
	'E' : 64,
	'F' : 65,
	'F#' : 66,
	'Gb' : 66,
	'G' : 67,
	'G#' : 68,
	'Ab' : 68,
	'A' : 69,
	'A#' : 70,
	'Bb' : 70,
	'B' : 71,
}

chordMap = {
	'C' : ['C', 'E', 'G'],
	'C#' : ['C#', 'F', 'G#'],
	'Db' : ['C#', 'F', 'G#'],
	'D' : ['D', 'F#', 'A'],
	'D#' : ['D#', 'G' 'A#'],
	'Eb' : ['D#', 'G', 'A#'],
	'E' : ['E', 'G#', 'B'],
	'F' : ['F', 'A', 'C'],
	'F#' : ['F#', 'A#', 'C#'],
	'Gb' : ['F#', 'A#', 'C#'],
	'G' : ['G', 'B', 'D'],
	'G#' : ['G#', 'C', 'D#'],
	'Ab' : ['G#', 'C', 'D#'],
	'A' : ['A', 'C#', 'E'],
	'A#' : ['A#', 'D', 'F'],
	'Bb' : ['A#', 'D', 'F'],
	'B' : ['B', 'D#', 'F#'],
}