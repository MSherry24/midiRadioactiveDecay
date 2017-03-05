import math, numpy

class AtomFactory:
	def __init__(self, maxHalfLife):
		self.maxHalfLife = maxHalfLife
		self.scaledHalfLives = self.getHalfLifeMap()

	def createAtom(self):
		return Atom(self.maxHalfLife, self.scaledHalfLives)

	def getHalfLifeMap(self):
		return {
			'U235': self.scaleHalfLife(713000000 * 365 * 24 * 60 * 60),
			'Th231': self.scaleHalfLife(25.6 * 365 * 24 * 60 * 60),
			'Pa231': self.scaleHalfLife(32480 * 365 * 24 * 60 * 60),
			'Ac227': self.scaleHalfLife(21.2 * 365 * 24 * 60 * 60),
			'Fr223': self.scaleHalfLife(22 * 60),
			'Th227': self.scaleHalfLife(18 * 24 * 60 * 60),
			'Ra223': self.scaleHalfLife(11.7 * 24 * 60 * 60),
			'Rn219': self.scaleHalfLife(4),
			'Po215': self.scaleHalfLife(0.0018),
			'At215': self.scaleHalfLife(0.00001), 
			'Pb211': self.scaleHalfLife(31.6 * 60),
			'Bi211': self.scaleHalfLife(21.5 * 60),
			'Po211': self.scaleHalfLife(25), 
			'Tl207': self.scaleHalfLife(4.78 * 60),
			'Pb207': self.scaleHalfLife(9999999999999999999999999)
		}

	def scaleHalfLife(self, time):
		normalizedTime = time * 1000000
		maxHalfLifeScaledMinutes = self.maxHalfLife
		maxHalfLifeRealTimePower = 13
		maxHalfLifeScaledSeconds = maxHalfLifeScaledMinutes * 60
		scale = maxHalfLifeScaledSeconds * math.log(normalizedTime) / maxHalfLifeRealTimePower
		return scale

class Atom:

	def __init__(self, maxHalfLife, scaledHalfLives):
		self.maxHalfLife = maxHalfLife
		self.scaledHalfLives = scaledHalfLives
		self.element = 'U235'
		self.decayTime = self.getDecayTime()
		self.decayIndex = 0

	def getDecayTime(self):
		return numpy.random.exponential(scale=self.getHalfLife())

	def getHalfLife(self):
		return self.scaledHalfLives[self.element]

	def nextElementInSequence(self) :
		sequence = self.getDecaySequence()
		nextElement = sequence[self.decayIndex]
		if (isinstance(nextElement, list)):
			nextElement = nextElement[numpy.random.binomial(1,0.5)]
		return nextElement

	def decay(self):
		prevElement = self.element
		self.decayIndex += 1;
		self.element = self.nextElementInSequence()
		self.decayTime = self.getDecayTime()

	def getDecaySequence(self):
		return [
		'U235', 
		'Th231',
		'Pa231',
		'Ac227',
		['Fr223','Th227'],
		'Ra223',
		'Rn219',
		'Po215',
		['At215', 'Pb211'],
		'Bi211',
		['Po211', 'Tl207'],
		'Pb207'
		]



