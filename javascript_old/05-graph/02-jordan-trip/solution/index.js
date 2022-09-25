function jordanTrip(graph, noCities) {
    if (graph.size() === 0) {
        return 'The Graph is empty';
    }
    if (noCities.length === 0) {
        return 'There are no  weigth of the asked cities';
    }
    let arr = [];

    let weightOfEachone = [];
    for (let i = 0; i < noCities.length; i++) {
        arr.push(noCities[i]);
    }
    for (let i = 0; i < arr.length; i++) {
        let weight = graph.getWeight(arr[i], arr[i + 1]);
        weightOfEachone.push(weight);
    }

    const result = weightOfEachone.reduce((a, b) => a + b, 0);
    return result;


}

module.exports = jordanTrip;
