const {HashTable} = require('../../02-repeated-word/javascript/hashtable')

const findTarget = (root, k) =>{
    let ht = new HashTable(50);
    let arr = [];
    arr.push(root);
    
    while (arr.length > 0) {
      let curr = arr.shift();
      
      if (ht.contains(k - curr.value) === true) {
        return true;
      }
      
      ht.add(curr.value);
      
      if (curr.left != null) {
        arr.push(curr.left);
      }
      
      if (curr.right != null) {
        arr.push(curr.right);
      }
    }
    
    return false;
  };
  module.exports = findTarget;
