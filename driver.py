import Elements
import Event
import Player
from time import sleep
import math
import numpy 
import heapq
import mido 

def main(maxHalfLifeInMinutes, numberOfAtoms, chordMapping):
	atoms = generateAtoms(maxHalfLifeInMinutes, numberOfAtoms)
	eventqueue = generateEventQueue(atoms, chordMapping)
	start(eventqueue)

def generateAtoms(maxHalfLifeInMinutes, numberOfAtoms):
	atomFactory = Elements.AtomFactory(maxHalfLife=maxHalfLifeInMinutes)

	atoms = []
	for x in range(numberOfAtoms):
		atom = atomFactory.createAtom()
		atoms.append(atom)
	return atoms

def generateEventQueue(atoms, chordMapping):
	eventFactory = Event.EventFactory(chordMapping)

	eventqueue = []
	for x in range(len(atoms)):
		heapq.heappush(eventqueue, eventFactory.createEvent(atoms[x]))
	return eventqueue

def start(eventqueue):
	time = 0
	outport = mido.open_output(mido.get_output_names()[0])
	while (len(eventqueue) > 0):
		currentEvent = heapq.heappop(eventqueue)
		delay = currentEvent.eventTime - time

		print currentEvent.pid, 'element', currentEvent.Atom.element, 'delay', delay
		sleep(delay)
		outport.send(currentEvent.midiMessage)

		time += delay
		currentEvent.generateNextEvent(time)
		if (currentEvent.Atom.element != 'Pb207'):
			heapq.heappush(eventqueue, currentEvent)