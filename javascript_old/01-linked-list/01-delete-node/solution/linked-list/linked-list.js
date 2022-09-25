'usr strict';

const Node = require('./node')

class LinkedList {
    constructor() {
        this.head = null;
    }
    append(node) {
        if (!this.head) {
            this.head = node;
            return this;
        }
        let currentNode = this.head;
        while (currentNode.next) {
            currentNode = currentNode.next;
        }
        currentNode.next = node;
    }
    include(value) {
        let current = this.head;
        while (current.next) {
            if (current.next.val === value) {
                return true;
            } else {
                current = current.next;
                return false;
            }
        }
    }
    toString() {
        let allNodes = [];
        let current = this.head;
        while (current.next) {
            allNodes.push(current.val);
            current = current.next;
        }
        allNodes.push(current.val);
        allNodes.push('null');
        let arrowNext = allNodes.join(' -> ');
        return arrowNext;
    }

}
module.exports = LinkedList;