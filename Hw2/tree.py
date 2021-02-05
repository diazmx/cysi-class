class Tree:
    def __init__(self, key, frec):
        self.key = key
        self.frec = frec
        self.left = None
        self.right = None


class Node:
    def __init__(self, tree):
        self.tree = tree
        self.next = None
        self.prev = None


class TreeList:
    def __init__(self):
        # limits
        thead = Tree('-1', -1)
        tlast = Tree('-2', -2)
        self.head = Node(thead)
        self.last = Node(tlast)
        self.head.next = self.last
        self.last.prev = self.head
        self.tam = 0
        self.f = open("out.txt", "w")

    def create(self, list_):
        """
        Create a first list
        """
        for key, frec in list_:
            self.add(str(key), frec)

    def add(self, key, frec):
        # Create a Tree and Node objects
        t = Tree(key, frec)
        n_node = Node(t)

        i_node = self.head
        while i_node.tree.frec != -2:
            if t.frec < i_node.tree.frec:  # Check the frecuency
                # Connections
                n_node.next = i_node
                n_node.prev = i_node.prev
                i_node.prev.next = n_node
                i_node.prev = n_node
                self.tam += 1
                return
            else:  # Just cycle
                i_node = i_node.next
        # If there are not nodes to compare
        n_node.next = i_node
        n_node.prev = i_node.prev
        i_node.prev.next = n_node
        i_node.prev = n_node
        self.tam += 1

    def new_add(self, node):
        i_node = self.head
        while i_node.tree.frec != -2:
            if node.tree.frec < i_node.tree.frec:  # Check the frecuency
                # Connections
                node.next = i_node
                node.prev = i_node.prev
                i_node.prev.next = node
                i_node.prev = node
                self.tam += 1
                return
            else:  # Just cycle
                i_node = i_node.next
        # If there are not nodes to compare
        node.next = i_node
        node.prev = i_node.prev
        i_node.prev.next = node
        i_node.prev = node
        self.tam += 1

    def print_list(self):
        i_node = self.head
        while i_node:
            print(i_node.tree.key, i_node.tree.frec, end=' -> ')
            i_node = i_node.next
        print()

    def step(self):
        """
        Construir arbol con dos simbolos menor frecuencia
        a raiz asignar la suma de las frecuencias
        """
        # Tomo los dos primeros nodos
        nfir = self.head.next
        nsec = nfir.next
        # Sumo sus frecuencias y apunto a los nuevos
        sum_frec = nfir.tree.frec + nsec.tree.frec
        tnode = Tree(None, sum_frec)
        tnode.left = nfir.tree
        tnode.right = nsec.tree
        # Elimino los nodos utilizados
        nthe = nsec.next
        self.head.next = nthe
        nthe.prev = self.head
        del nfir
        del nsec
        self.tam -= 2
        # Add new node to Treelist
        nnode = Node(tnode)
        self.new_add(nnode)

    def complete(self):
        while self.tam != 1:
            self.step()

    def print_tree(self, root, prefix):
        if root.left.key != None:
            self.f.write(str(root.left.key) + "\t" + prefix+"0"+"\n")
        if root.right.key != None:
            self.f.write(str(root.right.key) + "\t" + prefix+"1"+"\n")
        # self.print_tree(root.right)
        if root.left.left:
            self.print_tree(root.left, prefix+"0")
        if root.right.right:
            self.print_tree(root.right, prefix+"1")

    def close_file(self):
        self.f.close()
