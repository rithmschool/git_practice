let grid = [];
let width = 100;
let height = 70;
for(let i = 0; i < height; i++){
    let row = [];
    for(let j = 0; j < width; j++){
        row.push("-");
    }
    grid.push(row);
}

function rect(x, y, w, h){
    for(let i = x; i < x+w; i++){
        grid[y][i] = "#";
    }
    for(let i = x; i < x+w; i++){
        grid[y+h-1][i] = "#";
    }
    for(let i = y; i < y+h; i++){
        grid[i][x] = "#";
    }
    for(let i = y; i < y+h; i++){
        grid[i][x+w-1] = "#";
    }
}

function drawGrid(){
    let str = "";
    for(let i = 0; i < grid.length; i++){
        let row = "";
        for(let j = 0; j < grid[i].length; j++){
            row+=grid[i][j];
        }
        row+="\n";
        str+=row;
    }
    console.log(str);
}

function draw(){
    rect(10, 10, 10, 10);
    rect(20, 30, 20, 20);
    drawGrid();
}
draw();