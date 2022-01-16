alert('hello world');

var shoping_list = ['milk', 'eggs', 'bread', 'chocolate'];
shoping_list.push('cheese');

var finder = function(item) {
  return item === 'cheese';
}

let h = shoping_list.find(finder);
console.log(h);