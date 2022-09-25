const { Stack } = require('../../01/javascript/index');

const isValid = (s) => {
    let newStack = new Stack();
    for (let i = 0; i < s.length; i++) {
        if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
            newStack.push(s[i]);
        } else {
            if (newStack.isEmpty()) {
                return false;
            } else {
                let top = newStack.peek();
                if (s[i] == ')' && top == '(' ||
                    s[i] == '}' && top == '{' ||
                    s[i] == ']' && top == '[') {
                    newStack.pop();
                } else {
                    return false;
                }
            }
        }
    }
    return true;
};
module.exports = isValid;