const {HashTable} = require('./hashtable')

function findMostReaptedWord(str) {
    if (str) {
        let ht = new HashTable(50);
        let arr = str.split(' ')
        var maxWord;
        for (let i = 0; i <= arr.length; i++) {
          
            if (ht.contains(arr[i].toUpperCase())) {
                maxWord = arr[i]
                break;
            } else {
                ht.add(arr[i].toUpperCase(), 1)
            }
        }
        return maxWord;

} else {
    return 'PLEASE ADD ANY WORDS TO FIND THE MOST REAPETED WORD';
}
}
 
module.exports = findMostReaptedWord;
//  console.log(findMostReaptedWord("I am learning programming at ASAC and I love it"));