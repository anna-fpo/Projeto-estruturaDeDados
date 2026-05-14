class Node:
    def __init__(self, track):
        self.track = track
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cursor = None
        self.size = 0

    def add(self, track):
        new_node = Node(track)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.cursor = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.size += 1


    def current(self):
        if self.cursor:
            return self.cursor.track
        return None

    def move_next(self):
        if self.cursor and self.cursor.next:
            self.cursor = self.cursor.next

        return self.current()

    def move_prev(self):
        if self.cursor and self.cursor.prev:
            self.cursor = self.cursor.prev

        return self.current()

    def __len__(self):
        return self.size

    def __iter__(self):
        """Implementa um iterador para a playlist, percorrendo do início ao fim."""
        atual = self.head
        while atual is not None:
            yield atual.track
            atual = atual.next

    def remove_at(self, pos):
        """Remove a track que se encontra na posição pos da lista (baseado em 1)."""
        # 1. Validação da posição
        if pos < 1 or pos > self.size:
            return None  # Posição inválida

        # Caminhar até o nó na posição desejada
        atual = self.head
        for _ in range(pos - 1):
            atual = atual.next

        # Se o nó a ser removido for o que o cursor está apontando,
        # movemos o cursor para o próximo (ou None se for o último)
        if self.cursor == atual:
            self.cursor = atual.next

        # 2. Remover o primeiro elemento (head)
        if atual == self.head:
            self.head = atual.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None  # A lista ficou vazia
        # 3. Remover o último elemento (tail)
        elif atual == self.tail:
            self.tail = atual.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None  # A lista ficou vazia
        # 4. Remover um elemento do meio
        else:
            atual.prev.next = atual.next
            atual.next.prev = atual.prev
        # Decrementa o tamanho da lista e retorna a faixa removida
        self.size -= 1
        return atual.track

