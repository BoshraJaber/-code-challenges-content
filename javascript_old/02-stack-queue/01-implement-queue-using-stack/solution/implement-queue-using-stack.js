class MyQueue {
    constructor() {
        this.s1 = [];
        this.s2 = [];
    }

    enQueue(x) {
        while (this.s1.length != 0) {
            this.s2.push(this.s1.pop());
        }

        this.s1.push(x);

        while (this.s2.length != 0) {
            this.s1.push(this.s2.pop());
        }
    }

    deQueue() {
        if (this.s1.length == 0) {
            return null;
        }

        let x = this.s1[this.s1.length - 1];
        this.s1.pop();
        return x;
    }
    front() {
        if (this.s1.length == 0) {
            return null;
        }
        return this.s1[0]
    }
    isEmpty() {
        if (this.s1.length == 0) {
            return true;
        } else {
            return false
        }
    }

}

module.exports = MyQueue