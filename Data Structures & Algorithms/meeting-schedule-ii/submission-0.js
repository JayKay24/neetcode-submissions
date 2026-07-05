/**
 * Definition of Interval:
 * class Interval {
 *   constructor(start, end) {
 *     this.start = start;
 *     this.end = end;
 *   }
 * }
 */

class Solution {
    /**
     * @param {Interval[]} intervals
     * @returns {number}
     */
    minMeetingRooms(intervals) {
        intervals.sort((a, b) => a.start - b.start);

        const minHeap = new PriorityQueueCustom(true);
        
        for (const interval of intervals) {
            if (!minHeap.isEmpty() && this.isNotConflicting(minHeap.peek().key, interval)) {
                minHeap.dequeue();
            }
            minHeap.enqueue(new PqNode(interval.end, interval));
        }

        return minHeap.size();
    }

    isNotConflicting(a, b) {
        return a.end <= b.start;
    }
}

class PriorityQueueCustom {
  #data;
  #min;
  constructor(min = false) {
    this.#data = [];
    this.#min = min;
  }

  peek() {
    return this.#data[0];
  }

  lastNode() {
    return this.#data[this.#data.length - 1];
  }

  isEmpty() {
    return this.size() === 0;
  }

  size() {
    return this.#data.length;
  }

  clear() {
    this.#data = [];
  }

  enqueue(value) {
    this.#data.push(value);

    let newNodeIdx = this.#data.length - 1;
    if (this.#min) {
      this.#insertMinHeap(newNodeIdx);
    } else {
      this.#insertMaxHeap(newNodeIdx);
    }
  }

  dequeue() {
    const toReturn = this.peek();
    if (this.size() === 1) {
      this.#data.pop();
    } else if (this.size() > 1) {
      this.#data[0] = this.#data.pop();
      let trickleNodeIdx = 0;
      if (this.#min) {
        this.#deleteMinHeap(trickleNodeIdx);
      } else {
        this.#deleteMaxHeap(trickleNodeIdx);
      }
    }
    return toReturn;
  }

  remove(val) {
    let idx = this.#data.findIndex((value) => value.priority === val);
    if (idx !== -1) {
      this.#swap(idx, 0);
      this.dequeue();
    }
  }

  #leftChildIdx(idx) {
    return (idx * 2) + 1;
  }

  #rightChildIdx(idx) {
    return (idx * 2) + 2;
  }

  #parentIdx(idx) {
    return Math.floor((idx - 1) / 2);
  }

  #insertMaxHeap(newNodeIdx) {
    while (newNodeIdx > 0 && this.#data[newNodeIdx].priority > this.#data[this.#parentIdx(newNodeIdx)].priority) {
      this.#swap(this.#parentIdx(newNodeIdx), newNodeIdx);
      newNodeIdx = this.#parentIdx(newNodeIdx);
    }
  }

  #insertMinHeap(newNodeIdx) {
    while (newNodeIdx > 0 && this.#data[newNodeIdx].priority < this.#data[this.#parentIdx(newNodeIdx)].priority) {
      this.#swap(this.#parentIdx(newNodeIdx), newNodeIdx);
      newNodeIdx = this.#parentIdx(newNodeIdx);
    }
  }

  #hasGreaterChild(idx) {
    return (this.#data[this.#leftChildIdx(idx)] !== undefined && this.#data[this.#leftChildIdx(idx)].priority > this.#data[idx].priority) ||
      (this.#data[this.#rightChildIdx(idx)] !== undefined && this.#data[this.#rightChildIdx(idx)].priority > this.#data[idx].priority);
  }

  #hasLesserChild(idx) {
    return (this.#data[this.#leftChildIdx(idx)] !== undefined && this.#data[this.#leftChildIdx(idx)].priority < this.#data[idx].priority) ||
      (this.#data[this.#rightChildIdx(idx)] !== undefined && this.#data[this.#rightChildIdx(idx)].priority < this.#data[idx].priority);
  }

  #calculateLargerChildIdx(idx) {
    if (this.#data[this.#rightChildIdx(idx)] === undefined) {
      return this.#leftChildIdx(idx);
    }

    if (this.#data[this.#rightChildIdx(idx)].priority > this.#data[this.#leftChildIdx(idx)].priority) {
      return this.#rightChildIdx(idx);
    } else {
      return this.#leftChildIdx(idx);
    }
  }

  #calculateLesserChildIdx(idx) {
    if (this.#data[this.#rightChildIdx(idx)] === undefined) {
      return this.#leftChildIdx(idx);
    }

    if (this.#data[this.#rightChildIdx(idx)].priority < this.#data[this.#leftChildIdx(idx)].priority) {
      return this.#rightChildIdx(idx);
    } else {
      return this.#leftChildIdx(idx);
    }
  }

  #deleteMinHeap(trickleNodeIdx) {
    while (this.#hasLesserChild(trickleNodeIdx)) {
      const lesserChildIdx = this.#calculateLesserChildIdx(trickleNodeIdx);

      this.#swap(lesserChildIdx, trickleNodeIdx);

      trickleNodeIdx = lesserChildIdx;
    }
  }

  #deleteMaxHeap(trickleNodeIdx) {
    while (this.#hasGreaterChild(trickleNodeIdx)) {
      const largerChildIdx = this.#calculateLargerChildIdx(trickleNodeIdx);

      this.#swap(largerChildIdx, trickleNodeIdx);

      trickleNodeIdx = largerChildIdx;
    }
  }

  #swap(idx1, idx2) {
    [this.#data[idx2], this.#data[idx1]] = [this.#data[idx1], this.#data[idx2]];
  }
}

class PqNode {
  constructor(priority, key = null) {
    this.priority = priority;
    this.key = key;
  }
}