import os.path
import re
from collections import Counter
from itertools import groupby

DATA = os.path.join(os.path.dirname(__file__), 'day20.txt')


class Particle(object):

    def __init__(self, pid, position, velocity, acceleration):
        self.pid = pid
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def move(self):
        self.velocity = (self.velocity[0] + self.acceleration[0],
                         self.velocity[1] + self.acceleration[1],
                         self.velocity[2] + self.acceleration[2])

        self.position = (self.position[0] + self.velocity[0],
                         self.position[1] + self.velocity[1],
                         self.position[2] + self.velocity[2])

    def distance_to_origin(self) -> int:
        return abs(self.position[0]) + abs(self.position[1]) + abs(self.position[2])


def __build_particles(data) -> list[Particle]:
    particles = []
    for i, line in enumerate(data.splitlines()):
        parts = re.findall(
            r'p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>', line)[0]
        parts = tuple((int(p)) for p in parts)
        position = (parts[0], parts[1], parts[2])
        velocity = (parts[3], parts[4], parts[5])
        acceleration = (parts[6], parts[7], parts[8])
        particles.append(Particle(i, position, velocity, acceleration))
    return particles


def find_particle_closest_to_origin_for_longest(data) -> int:
    particles = __build_particles(data)
    closest_particles = []

    # "magic number" programming
    # I assume that after 1000 moves
    # we will have found the particle
    # that will always be the closest.
    moves = 1000

    while moves != 0:
        distances = {}
        for p in particles:
            p.move()
            distances[p.pid] = p.distance_to_origin()
        closest_particles.append(min(distances, key=distances.get))
        moves -= 1

    return Counter(closest_particles).most_common(1)[0][0]


def find_number_of_particles_left(data) -> int:
    particles = __build_particles(data)
    collided = []

    # "magic number" programming
    # I assume that after 1000 moves
    # there will be no more collisions.
    moves = 1000

    while moves != 0:
        positions = {}
        for p in particles:
            if p.pid not in collided:
                p.move()
                positions[p.pid] = p.position
        g = groupby(sorted(positions, key=positions.get), key=positions.get)
        g = [list(x) for _, x in g]
        for group in g:
            if len(group) >= 2:
                for pid in group:
                    collided.append(pid)
        moves -= 1

    return len(particles) - len(collided)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_particle_closest_to_origin_for_longest(data)))
        print("Part 2: " + str(find_number_of_particles_left(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
