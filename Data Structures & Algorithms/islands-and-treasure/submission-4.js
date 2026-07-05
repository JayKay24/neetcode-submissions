class Solution {
  #dirs;
  #n;
  #m;

  constructor() {
      this.#m = 0;
      this.#n = 0;
      this.#dirs = [
        [-1, 0], 
        [0, 1], 
        [1, 0], 
        [0, -1]
      ];
  }
  /**
   * @param {number[][]} grid
   */
  islandsAndTreasure(grid) {
      [this.#m, this.#n] = [grid.length, grid[0]?.length ?? 0];

      for (let i = 0; i < this.#m; i++) {
          for (let j = 0; j < this.#n; j++) {
              if (this.#isWater(grid[i][j]) || this.#isTreasure(grid[i][j])) continue;
              const res = this.#bfs(grid, i, j);
              grid[i][j] = res === Infinity ? grid[i][j] : res;
          }
      }

      return grid;
  }

  #bfs(grid, r, c, visited = new Set()) {
    const q = new QueueDLL();
    q.enqueue(this.#getCoordStr(r, c));
    let steps = 0;

    while (!q.isEmpty()) {
      const size = q.size();

      for (let i = 0; i < size; i++) {
        const coord = q.dequeue();
        visited.add(coord);
        const [r, c] = this.#getCoordArr(coord);

        if (this.#isTreasure(grid[r][c])) return steps;

        for (const [dr, dc] of this.#dirs) {
          const [nr, nc] = [r + dr, c + dc];
          if (!this.#isInBounds(nr, nc) || visited.has(this.#getCoordStr(nr, nc)) || this.#isWater(grid[nr][nc])) continue;
          q.enqueue(this.#getCoordStr(nr, nc));
        }
      }

      steps++;
    }

    return Infinity;
  }

  #isInBounds(r, c) {
    return r >= 0 && r < this.#m && c >= 0 && c < this.#n;
  }

  #getCoordStr(r, c) {
    return `${r}-${c}`;
  }

  #getCoordArr(coordStr) {
    const [r, c] = coordStr.split('-').map((c) => Number(c));
    return [r, c];
  }

  #isWater(el) {
      return el === -1;
  }

  #isTreasure(el) {
      return el === 0;
  }
}

class QueueDLL {
  constructor(dll = new DoublyLinkedList()) {
    this.dll = dll;
  }

  enqueue(element = null) {
    this.dll.insertAtTail(element);
  }

  dequeue() {
    return this.dll.deleteAtHead();
  }

  peek() {
    return this.dll.head?.data;
  }

  isEmpty() {
    return this.dll.isEmpty();
  }

  size() {
    return this.dll.size;
  }
}

class DoublyLinkedListNode {
  constructor(value) {
    this.data = value;
    this.next = null;
    this.prev = null;
  }
}

class DoublyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  isEmpty() {
    return this.size === 0;
  }

  insertAtHead(value) {
    if (this.head === null) {
      this.head = new DoublyLinkedListNode(value);
      this.tail = this.head;
    } else {
      const temp = new DoublyLinkedListNode(value);
      this.head.prev = temp;
      temp.next = this.head;
      this.head = temp;
    }

    this.size++;
  }

  insertAtTail(value) {
    if (this.tail === null) {
      this.tail = new DoublyLinkedListNode(value);
      this.head = this.tail;
    } else {
      const temp = new DoublyLinkedListNode(value);
      temp.prev = this.tail;
      this.tail.next = temp;
      this.tail = temp;
    }

    this.size++;
  }

  deleteAtHead() {
    let toReturn = null;

    if (this.head !== null) {
      toReturn = this.head.data;

      if (this.head === this.tail) {
        this.head = null;
        this.tail = null;
      } else {
        this.head = this.head.next;
        this.head.prev = null;
      }

      this.size--;
    }

    return toReturn;
  }

  deleteAtTail() {
    let toReturn = null;

    if (this.tail !== null) {
      toReturn = this.tail.data;

      if (this.tail === this.head) {
        this.tail = null;
        this.head = null;
      } else {
        this.tail = this.tail.prev;
        this.tail.next = null;
      }

      this.size--;
    }

    return toReturn;
  }

  findStartingHead(value) {
    if(this.head.data === value) return true;
    let currentHead = this.head;
    while(currentHead.next) {
      if(currentHead.data === value) return true;
      currentHead = currentHead.next;
    }

    return false;
  }

  findStartingTail(value) {
    if(this.tail.data === value) return true;
    let currentTail = this.tail;
    while(currentTail.prev) {
      if(currentTail.data === value) return true;
      currentTail = currentTail.prev;
    }

    return false;
  }
}
