class HashTable {
  constructor(size) {
    this.size = size;
    this.entries = new Array(size); 
  }
  hash(key) {
    key =1024
    return   key% this.size
     
  }
  add(key, value) {
    if (this.contains(key)) {
      return console.log("the key is exist before");
    }
    let hashIndex = this.hash(key);
    if (!this.entries[hashIndex]) {
      this.entries[hashIndex] = new Linkedlist();
    }
    let entry = { [key]: value };
    this.entries[hashIndex].append(entry); 
  }
  get(key) {
    return this.entries[this.hash(key)]
      ? this.entries[this.hash(key)].getBykeyName(key)
      : "NotFound";
  }
  contains(key) {
    console.log(",,,,,,,,,,,,,,,,,,,,,,,,", key);

    return this.entries[this.hash(key)]
      ? this.entries[this.hash(key)].includes(key)
      : false;
  }
}

class Node {
  constructor(value, left = null, right = null) {
    this.value = value === undefined ? 0 : value;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

class Linkedlist {
  constructor() {
    this.head = null;
  }
  includes(val) {
    let currentNode = this.head;
    while (currentNode) {
      if (typeof currentNode.value === 'object') {
        if (Object.keys(currentNode.value)[0] == val) {
          return true
        }
      } else if (currentNode.value == val) {
        return true;
      }
      currentNode = currentNode.next;
    }
    return false;
  }
  append(value) {
    let newNode = new Node(value);

    if (!this.head) {
      this.head = newNode;
      return this;
    }
    let node1 = this.head;
    while (node1.next) {
      node1 = node1.next;
    }
    node1.next = newNode;
    return this;
  }
}
module.exports = {HashTable,Node};
