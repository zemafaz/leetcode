from re import S
import unittest

class UndergroundSystem:
	def __init__(self):
		self.active = []
		self.record = {}

	def check_in(self, id: int, station_name: str, t: int) -> None:
		entry = {
			'id': id,
			'name': station_name,
			'time': t
		}
		self.active.append(entry)

	def check_out(self, id: int, station_name: str, t: int) -> None:
		entry = {}
		for i, e in enumerate(self.active):
			if (e['id'] == id):
				aux = self.active.pop(i)
				entry = {
					'station_ci': aux['name'],
					'time': t - aux['time']
				}

		if self.record.get(station_name):
			n_trips = self.record[station_name][entry['station_ci']]['n_trips'] + 1
			self.record[station_name][entry['station_ci']] ={
				'time': (n_trips - 1) / n_trips * self.record[station_name][entry['station_ci']]['time'] + 1 / n_trips * entry['time'],
				'n_trips': n_trips
			} 
		else:
			self.record[station_name] = {
				entry['station_ci']: {
					'time': entry['time'],
					'n_trips': 1
				}
			}
		
	def get_average_time(self, start_station: str, end_station: str) -> float:
		return self.record[end_station][start_station]['time']

class TestSolution(unittest.TestCase):
	ug_system = UndergroundSystem()

	def test_1(self):
		self.ug_system.check_in(45, "Leyton", 3)
		self.ug_system.check_in(32, "Paradise", 8)
		self.ug_system.check_in(27, "Leyton", 10)
		self.ug_system.check_out(45, "Waterloo", 15)
		self.ug_system.check_out(27, "Waterloo", 20)
		self.ug_system.check_out(32, "Cambridge", 22)
		avg = self.ug_system.get_average_time("Paradise", "Cambridge")
		self.assertEqual(avg, 14)
		avg = self.ug_system.get_average_time('Leyton', 'Waterloo')
		self.assertEqual(avg, 11)

		self.ug_system.check_in(10, "Leyton", 24)
		avg = self.ug_system.get_average_time('Leyton', 'Waterloo')
		self.assertEqual(avg, 11)
		self.ug_system.check_out(10, 'Waterloo', 38)
		avg = self.ug_system.get_average_time('Leyton', 'Waterloo')
		self.assertEqual(avg, 12)

if __name__ == '__main__':
	unittest.main()