import Player

def CMajToFMaj():
	return {
		'U235' : Player.getChord('C'), 
		'Th231' : Player.getChord('D', 'm'),
		'Pa231' : Player.getChord('E', 'm'),
		'Ac227' : Player.getChord('F'),
		'Fr223' : Player.getChord('G'),
		'Th227' : Player.getChord('A', 'm'),
		'Ra223' : Player.getChord('F'),
		'Rn219' : Player.getChord('G#', 'm'),
		'Po215' : Player.getChord('A#', 'm'),
		'At215' : Player.getChord('Bb'),
		'Pb211' : Player.getChord('C'),
		'Bi211' : Player.getChord('G'),
		'Po211' : Player.getChord('F'),
		'Tl207' : Player.getChord('C'),
		'Pb207' : Player.getChord('C')
	}

def C13toC():
	return {
		'U235' : Player.getChord('C', '13'), 
		'Th231' : Player.getChord('C', '11'),
		'Pa231' : Player.getChord('C', '9'),
		'Ac227' : Player.getChord('C', '7'),
		'Fr223' : Player.getChord('C', 'm9'),
		'Th227' : Player.getChord('C', 'm7'),
		'Ra223' : Player.getChord('A', 'm7'),
		'Rn219' : Player.getChord('D', '7'),
		'Po215' : Player.getChord('F'),
		'At215' : Player.getChord('F', 'm'),
		'Pb211' : Player.getChord('C', 'sus4'),
		'Bi211' : Player.getChord('C', 'sus2'),
		'Po211' : Player.getChord('C'),
		'Tl207' : Player.getChord('C'),
		'Pb207' : Player.getChord('C')
	}