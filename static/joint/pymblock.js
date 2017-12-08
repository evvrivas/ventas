
var graph = new joint.dia.Graph;

var paper = new joint.dia.Paper({ 
    el: $('#myholder-link'), 
    width: 800, 
    height: 600,
    gridSize: 1,
    model: graph,
    defaultLink: new joint.dia.Link({
            attrs: { '.marker-target': { d: 'M 10 0 L 0 5 L 10 10 z' } }
        }),
        validateConnection: function(cellViewS, magnetS, cellViewT, magnetT, end, linkView) {
            // Prevent linking from input ports.
            if (magnetS && magnetS.getAttribute('type') === 'input') return false;
            // Prevent linking from output ports to input ports within one element.
            if (cellViewS === cellViewT) return false;
            // Prevent linking to input ports.
            return magnetT && magnetT.getAttribute('type') === 'input';
        },
        // Enable marking available cells & magnets
        markAvailable: true


 });





var m1 = new joint.shapes.devs.Model({
    position: { x: 50, y: 50 },
    size: { width: 90, height: 90 },
    inPorts: ['in1'],
    outPorts: ['out1','out2'],
    attrs: {
        '.label': { text: 'Model', 'ref-x': .4, 'ref-y': .2 },
        rect: { fill: '#2ECC71' },
        '.inPorts circle': { fill: '#16A085' },
        '.outPorts circle': { fill: '#E74C3C' }
    }
});
graph.addCell(m1);




graph.on('change:source change:target', function(link) {
    var sourcePort = link.get('source').port;
    var sourceId = link.get('source').id;
    var targetPort = link.get('target').port;
    var targetId = link.get('target').id;

    var codigo = 'bla bla bla';

    var m = [
        'The port <b>' + sourcePort,
        '</b> of element with ID <b>' + sourceId,
        '</b> is connected to port <b>' + targetPort,
        '</b> hola <b>' + codigo,
        '</b> of elemnt with ID <b>' + targetId + '</b>'
    ].join('');
    
    out(m);
});

function out(m) {
    $('#myholder-link-out').html(m);
}





var member = function(x, y, rank, name, image, background, textColor) {

    textColor = textColor || "#000";

    var cell = new joint.shapes.devs.Model({
       position: { x: x, y: y },
    size: { width: 150, height: 45 },
    inPorts: ['in1'],
    outPorts: ['out1'],
    attrs: {
        '.label': { text: name, 'ref-x': .4, 'ref-y': .2 },
         rect: { fill: background },
        '.inPorts circle': { fill: '#16A085',magnet: 'passive', type: 'input' },
        '.outPorts circle': { fill: '#E74C3C',type: 'output' },
        '.card': { fill: background, stroke: 'none'},
              image: { 'xlink:href': '/static/'+ image, opacity: 0.7 },
            '.rank': { text: rank, fill: textColor, 'word-spacing': '-5px', 'letter-spacing': 0},
            '.name': { text: name, fill: textColor, 'font-size': 13, 'font-family': 'Arial', 'letter-spacing': 0 }
    }
    });
    graph.addCell(cell);
    return cell;
};





var bart = member(300,70,'CEO', 'INICIO', 'tronico.jpg', '#30d0c6');
var homer = member(90,200,'VP Marketing', 'Homer Simpson', 'tronico.jpg', '#7c68fd', '#f1f1f1');
var marge = member(300,200,'VP Sales', 'Marge Simpson', 'tronico.jpg', '#7c68fd', '#f1f1f1');
var lisa = member(500,200,'VP Production' , 'Lisa Simpson', 'tronico.jpg', '#7c68fd', '#f1f1f1');
var maggie = member(400,350,'Manager', 'Maggie Simpson', 'tronico.jpg', '#feb563');
var lenny = member(190,350,'Manager', 'Lenny Leonard', 'tronico.jpg', '#feb563');
var carl = member(190,500,'Manager', 'Carl Carlson', 'tronico.jpg', '#feb563');

graph.addCells([m1]);



// Show Halo immediately for the rectangle so that it is visible to the reader straight away.



