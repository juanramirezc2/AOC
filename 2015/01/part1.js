const input = require('fs')
  .readFileSync(require('path').join(__dirname, 'input.txt'), 'utf8')
  .trim()

let result = input.split("").reduce((previous, current)=>{
  if(current == "("){
    return previous+1
  }
  else {
    return previous-1
  }
},0)

console.log({ result })
