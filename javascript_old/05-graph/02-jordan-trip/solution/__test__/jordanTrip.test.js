const graph = require('../../../01-graph-implementation/javascript/index');
let g = new graph();
const jordanTrip = require('../index');

node1 = g.addNode('Dead sea')
node2 = g.addNode('Kerak')
node3 = g.addNode('Wadi Musa')
node4 = g.addNode("Ma'an")
node5 = g.addNode('Aqaba')
node6 = g.addNode('Wadi Rum')


g.addEdge('Dead sea', 'Kerak', 82.2)
g.addEdge('Dead sea', 'Wadi Musa', 197)
g.addEdge('Kerak', 'Wadi Musa', 173)
g.addEdge('Kerak', "Ma'an", 144)
g.addEdge('Wadi Musa', "Ma'an", 35.6)
g.addEdge('Wadi Musa', 'Aqaba', 125)
g.addEdge('Wadi Musa', 'Wadi Rum', 118)
g.addEdge("Ma'an", 'Wadi Rum', 106)
g.addEdge('Aqaba', 'Wadi Rum', 73.9)


describe('Graph', () => {
    let g2 = new graph();
    it('should return the Graph is empty', () => {
        expect(jordanTrip(g, [])).toBe('There are no  weigth of the asked cities');
    })
    it('should return the weight of the graph', () => {
        expect(jordanTrip(g, ['Dead sea', 'Wadi Musa'])).toBe(197);
    })
    it('should return the weight of the graph', () => {
        expect(jordanTrip(g, ['Kerak', "Ma'an", 'Wadi Rum'])).toBe(250);
    })
})