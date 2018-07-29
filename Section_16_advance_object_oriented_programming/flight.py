"""
Flight Leg:

GLA -> LHR -> CAN
2 segments (GLA -> LHR, LHR -> CAN)
"""

from typing import List


class Segment:
    def __init__(self, departure, destination):
        self.departure = departure
        self.destination = destination


class Flight:
    def __init__(self, segments: List[Segment]):
        self.segments = segments

    def __repr__(self):
        """

        :return: string in the format of GLA -> LHR -> CAN
        """
        stops = [self.segments[0].departure, self.segments[0].destination]
        for seg in self.segments[1:]:
            stops.append(seg.destination)
        return ' -> '.join(stops)


    @property
    def departure_point(self):
        return self.segments[0].departure

    @departure_point.setter
    def departure_point(self, val):
        self.segments[0].departure = val


flight = Flight([Segment('GLA', 'LHR'), Segment('LHR', 'VIE')])
print(flight.departure_point)

flight.departure_point = 'EDI'
print(flight.departure_point)

print(flight)






