class Node:
    def __init__(self, info = None):
        self.info = info
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def AtTheBegining(self, data):
        if self.head != None:
            NewNode = Node(data)
            NewNode.next = self.head
            self.head = NewNode
        else:
            NewNode = Node(data)
            NewNode.next = None
            self.head = NewNode
            self.tail = NewNode

    def AtTheEnd(self, data):
        if self.head == None:
            NewNode = Node(data)
            NewNode.next = None
            self.head = NewNode
            self.tail = NewNode
        else:
            NewNode = Node(data)
            NewNode.next = None
            self.tail.next = NewNode
            self.tail = NewNode

    def display(self):
        if self.head is None:
            print("Linked list ว่าง")
            return
        
        print("ข้อมูลทั้งหมด:", end=" ")
        current = self.head
        while current:
            print(current.info, end=" ")
            current = current.next
        print()
    
    def calculate_average(self):
        if self.head is None:
            return 0
        
        total = 0
        count = 0
        current = self.head
        
        while current:
            total += current.info
            count += 1
            current = current.next
            
        return total / count

# ส่วนการทำงานหลักของโปรแกรม
print("โปรดระบุทางเลือกในการดำเนินการ Singly Linked List")
print("B: เพิ่มข้อมูลที่จุดเริ่มต้นของSingly Linked List")
print("E: เพิ่มข้อมูลที่จุดสุดท้าย Singly Linked List ")
print("กดปุ่มอื่นเพื่อจบการทำงาน")
print("-" * 30)

list = SLinkedList()

while True:
    choice = input("เลือกการทำงาน (B/E): ").upper()
    
    if choice not in ['B', 'E']:
        break
        
    try:
        data = int(input("ป้อนข้อมูล: "))
        
        if choice == 'B':
            list.AtTheBegining(data)
            print(f"เพิ่มข้อมูล {data} ที่จุดเริ่มต้น")
        else:
            list.AtTheEnd(data)
            print(f"เพิ่มข้อมูล {data} ที่จุดสุดท้าย")
            
        list.display()
        print("-" * 30)
        
    except ValueError:
        print("กรุณาป้อนตัวเลขเท่านั้น")
        print("-" * 30)

print("\nสรุปข้อมูล:")
print("-" * 30)
list.display()

if list.head:
    print(f"ข้อมูลที่ตำแหน่ง head: {list.head.info}")
    print(f"ข้อมูลที่ตำแหน่ง tail: {list.tail.info}")
    print(f"ค่าเฉลี่ยของข้อมูล: {list.calculate_average():.2f}")
else:
    print("ไม่มีข้อมูลใน Linked List")
