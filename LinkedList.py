# 자료구조 링크드 리스트 공부 #

class Node:
	"""링크드 리스트의 노드 클래스"""
	def __init__(self, data):
		self.data = data # 노드가 저장하는 데이터
		self.next = None # 다음 노드에 저장될 레퍼런스

#데이터 2, 3, 5, 7, 11을 담는 노드
head_node = Node(2)
node_1 = Node(3)
node_2 = Node(5)
node_3 = Node(7)
tail_node = Node(11)
