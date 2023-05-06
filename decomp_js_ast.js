const escodegen = require("escodegen");
const fs = require("fs");
file = process.argv[2];
let js_ast = JSON.parse(fs.readFileSync(file, "utf8"));
let p = escodegen.generate(js_ast);
console.log(p);
