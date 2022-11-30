const input = require('fs')
  .readFileSync(require('path').join(__dirname, 'input.txt'), 'utf8')
  .trim()

let basementIndex = false;
let result = input.split("").reduce((previous, current, index)=>{
  if(!basementIndex && previous==-1){
    basementIndex=index
    console.log(index)
  }
  if(current == "("){
    return previous+1
  }
  else {
    return previous-1
  }
},0)

console.log({ result: basementIndex+1 })
