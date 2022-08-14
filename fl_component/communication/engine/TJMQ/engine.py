import base64
from collections import Iterable
from functools import cached_property, partial
from pickle import dumps as p_dumps, loads as p_loads

from ...party import Party
from TJMQ.tj_mq.client import Client


class Engine():
	def __init__(
		self,
		session_id: str,
		local_party: Party,
		extra_info: dict,
		ip: str,
		port: int,
		from_queue: bool,
	):
		self._session_id = session_id
		self._local_party = local_party
		self._extra_info = extra_info
		self._ip = ip
		self._port = port
		self._from_queue = from_queue
		self.queue_map = {}

	@cached_property
	def client(self):
		return Client(ip=self._ip, port=self._port, from_queue=self._from_queue)

	def encode(self, data):
		return base64.b64encode(p_dumps(data))

	def decode(self, raw):
		return p_loads(base64.b64decode(raw))

	def get_queue(self, partya, partyb, tag):
		return f'{self._session_id}-{partya.id}-{partya.role}-{partyb.id}-{partyb.role}-{tag}'

	def __pull_party(self, party, tag):
		q = self.get_queue(party, self._local_party, tag)
		while 1:
			count = int(self.client.pop(q).decode())
			if not count:
				break
			for i in range(count): yield self.decode(self.client.pop(q))

	def pull(self, parties, tag: str):
		is_streams = [
			self.client.pop(self.get_queue(p, self._local_party, tag))
			for p in parties
		]
		stream = is_streams[0]
		assert all([i == stream for i in is_streams]), 'error stream'
		if stream == b'true':
			return [
	    		self.__pull_party(p, tag)
	    		for p in parties
    		]
			return
		return [
    		self.decode(self.client.pop(self.get_queue(p, self._local_party, tag)))
    		for p in parties
    	]

	def __push_party(self, queue, items):
		self.client.push(queue, f'{len(items)}'.encode())
		for i in items: self.client.push(queue, self.encode(i))

	def push(self, data, parties, tag: str, stream=False):
		if stream:
			assert isinstance(data, Iterable), 'data required Iterable, when mode is stream'
			funcs = []
			for p in parties:
				q = self.get_queue(self._local_party, p, tag)
				self.client.push(q, b'true')
				funcs.append(partial(self.__push_party, 	q))
			for i in data:
				for f in funcs:
					f([i])
			for p in parties:
				q = self.get_queue(self._local_party, p, tag)
				self.client.push(q, b'0')
			return
		for p in parties:
			q = self.get_queue(self._local_party, p, tag)
			self.client.push(q, b'false')
			self.client.push(q, self.encode(data))
