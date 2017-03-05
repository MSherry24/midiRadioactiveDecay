import Player, numpy


class EventFactory:

	def __init__(self, elementToChordMap):
		self.elementToChordMap = elementToChordMap
		self.idCounter = -1

	def createEvent(self, atom):
		self.idCounter += 1
		return Event(self.idCounter, atom, self.elementToChordMap)

class Event:

	def __init__(self, pid, atom, elementToChordMap):
		self.pid = pid
		self.Atom = atom
		self.eventTime = self.getEventTime(0)
		self.elementToChordMap = elementToChordMap
		self.octave = numpy.random.randint(low=-5, high=5)
		self.channel = self.Atom.decayIndex
		self.midiMessage = self.getMessage()

	def __lt__(self, other):
	    selfPriority = self.eventTime
	    otherPriority = other.eventTime
	    return selfPriority < otherPriority

	def getMessage(self):
		note = self.getNote()
		return Player.getMidoMessage(note, self.octave, self.channel)

	def getEventTime(self, currentTime):
		return self.Atom.decayTime + currentTime

	def generateNextEvent(self, currentTime):
		self.Atom.decay()
		self.channel = self.Atom.decayIndex
		self.midiMessage = self.getMessage()
		self.eventTime = self.getEventTime(currentTime)

	def getNote(self):
		chord = self.elementToChordMap[self.Atom.element]
		index = numpy.random.randint(low=0, high=len(chord) - 1)
		return chord[index]




